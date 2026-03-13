from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_candidate, get_current_recruiter
from app.schemas import ChatRequest, ChatResponse
from app.models import Candidate, Recruiter, MatchResult, JobOffer

router = APIRouter(prefix="/api/chat", tags=["Chat"])

@router.post("/candidate", response_model=ChatResponse)
def chat_candidate(
    payload: ChatRequest,
    current_user=Depends(get_current_candidate),
    db: Session = Depends(get_db),
):
    """A lightweight chatbot for candidates."""
    candidate = db.query(Candidate).filter(Candidate.user_id == current_user.id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate profile not found")

    message = payload.message.strip().lower()

    # Basic keyword-based responses
    if "score" in message or "améliorer" in message or "improve" in message:
        return ChatResponse(
            reply=(
                "Pour améliorer votre score, vérifiez que votre CV contient des mots-clés pertinents "
                "et détaillés, mettez à jour vos expériences récentes et ajoutez des projets concrets. "
                "N'oubliez pas de compléter votre profil GitHub et de montrer des contributions régulières."
            )
        )

    if "compétence" in message or "skills" in message or "missing" in message:
        # Fall back to generic answer if no analysis
        if candidate.cv_analysis:
            skills = candidate.cv_analysis.skills or []
            if skills:
                skill_list = ", ".join(skills[:5])
                return ChatResponse(
                    reply=(
                        f"Je vois que vous maîtrisez : {skill_list}. Pour progresser, pensez à renforcer "
                        "vos compétences techniques et à diversifier vos projets."
                    )
                )
        return ChatResponse(
            reply=(
                "Je n'ai pas encore analysé votre CV. Téléversez votre CV pour obtenir des conseils plus précis."
            )
        )

    return ChatResponse(
        reply=(
            "Je suis là pour vous aider ! Essayez de demander : 'Comment améliorer mon score ?' "
            "ou 'Quelles compétences me manquent ?'"
        )
    )


@router.post("/recruiter", response_model=ChatResponse)
def chat_recruiter(
    payload: ChatRequest,
    current_user=Depends(get_current_recruiter),
    db: Session = Depends(get_db),
):
    """A lightweight chatbot for recruiters."""
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")

    message = payload.message.strip().lower()

    if "top" in message and "candidat" in message:
        job_offers = db.query(JobOffer).filter(JobOffer.recruiter_id == recruiter.id).all()
        if not job_offers:
            return ChatResponse(reply="Vous n'avez pas encore de postes publiés. Créez une offre pour voir les meilleurs candidats.")

        # Collect top candidates across your jobs
        match_results = (
            db.query(MatchResult)
            .filter(MatchResult.job_offer_id.in_([j.id for j in job_offers]))
            .order_by(MatchResult.final_score.desc())
            .limit(3)
            .all()
        )
        if not match_results:
            return ChatResponse(reply="Aucun candidat n'a encore été analysé pour vos offres. Lancez des matching pour voir les meilleurs profils.")

        top_names = ", ".join([m.candidate.full_name for m in match_results if m.candidate][:3])
        return ChatResponse(reply=f"Les candidats les mieux notés sont {top_names}. Vous pouvez cliquer sur un profil pour en savoir plus.")

    if "moyenne" in message or "average" in message or "score" in message:
        match_results = (
            db.query(MatchResult)
            .join(JobOffer)
            .filter(JobOffer.recruiter_id == recruiter.id)
            .all()
        )
        if not match_results:
            return ChatResponse(reply="Aucun score disponible pour le moment. Supervisez vos offres pour générer des données.")

        avg = sum((m.final_score or 0) for m in match_results) / max(len(match_results), 1)
        return ChatResponse(reply=f"Le score moyen des candidats pour vos offres est de {avg:.0f}%."
                               " Essayez de lancer un matching pour enrichir les données.")

    return ChatResponse(
        reply=(
            "Je peux vous aider à trouver les meilleurs candidats ou à connaître vos scores moyens. "
            "Essayez : 'Montre-moi les top candidats' ou 'Quel est le score moyen ?'"
        )
    )
