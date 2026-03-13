import pdfplumber
from docx import Document
import re
from typing import Dict, List
import json

class CVAgent:
    def __init__(self):
        self.tech_skills = [
            "Python", "Java", "JavaScript", "TypeScript", "React", "Angular", "Vue.js",
            "Node.js", "Express", "FastAPI", "Django", "Flask", "Spring Boot",
            "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Elasticsearch",
            "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Git", "GitHub", "GitLab",
            "HTML", "CSS", "Tailwind", "Bootstrap", "REST API", "GraphQL",
            "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn",
            "C++", "C#", ".NET", "PHP", "Ruby", "Go", "Rust", "Kotlin", "Swift",
            "Jenkins", "CI/CD", "Terraform", "Ansible", "Linux", "Bash", "PowerShell",
            "Agile", "Scrum", "Jira", "Microservices", "DevOps", "Testing", "Jest", "Pytest",
            # ✅ Ajouts
            "OpenCV", "NLP", "LLM", "Sentence-BERT", "N8N", "Scikit", "Pandas", "NumPy",
            "Axios", "Redux", "Next.js", "Vite", "Firebase", "Supabase", "Prisma"
        ]
        
        self.soft_skills = [
            "Leadership", "Communication", "Teamwork", "Problem Solving", "Critical Thinking",
            "Adaptability", "Time Management", "Creativity", "Collaboration", "Initiative"
        ]
    
    def extract_text_from_pdf(self, file_path: str) -> str:
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            print(f"Error extracting PDF: {e}")
        return text
    
    def extract_text_from_docx(self, file_path: str) -> str:
        text = ""
        try:
            doc = Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            print(f"Error extracting DOCX: {e}")
        return text
    
    def extract_skills(self, text: str) -> List[str]:
        text_lower = text.lower()
        found_skills = []
        for skill in self.tech_skills:
            if skill.lower() in text_lower:
                found_skills.append(skill)
        return list(set(found_skills))
    
    def extract_experience_years(self, text: str) -> int:
        patterns = [
            # Anglais
            r'(\d+)\+?\s*(?:years?)\s*(?:of\s*)?(?:experience)',
            r'(?:experience)\s*(?:of\s*)?(\d+)\+?\s*(?:years?)',
            # Français
            r'(\d+)\+?\s*(?:ans?)\s*(?:d[e\']?\s*)?(?:expérience)',
            r'(?:expérience)\s*(?:de\s*)?(\d+)\+?\s*(?:ans?)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            if matches:
                return int(matches[0])
        
        # Calcul par les dates
        year_pattern = r'\b(19|20)\d{2}\b'
        years = re.findall(year_pattern, text)
        if len(years) >= 2:
            years_sorted = sorted([int(y) for y in years])
            return max(0, 2025 - years_sorted[0])
        
        return 0
    
    def extract_education(self, text: str) -> List[Dict]:
        education = []
        education_keywords = [
            # Français
            "master", "licence", "ingénieur", "doctorat", "bac", "diplôme",
            "école", "université",
            # Anglais
            "bachelor", "degree", "university", "college", "phd", "mba",
            "graduate", "undergraduate", "engineering", "computer science",
            "b.sc", "m.sc", "b.s.", "m.s.",
        ]
        
        lines = text.split('\n')
        for line in lines:
            line_lower = line.lower()
            for keyword in education_keywords:
                if keyword in line_lower:
                    education.append({
                        "degree": line.strip(),
                        "year": self._extract_year_from_line(line)
                    })
                    break
        
        return education[:3]
    
    def _extract_year_from_line(self, line: str) -> str:
        year_match = re.search(r'\b(19|20)\d{2}\b', line)
        return year_match.group(0) if year_match else ""
    
    def calculate_cv_score(self, skills: List[str], experience_years: int, education: List[Dict]) -> float:
        score = 0.0
        
        # Skills score (max 50 points)
        skills_score = min(len(skills) * 3, 50)
        score += skills_score
        
        # Experience score (max 30 points)
        experience_score = min(experience_years * 5, 30)
        score += experience_score
        
        # Education score (max 20 points)
        education_score = min(len(education) * 10, 20)
        score += education_score
        
        return min(score, 100)
    
    def analyze(self, file_path: str) -> Dict:
        if file_path.endswith('.pdf'):
            raw_text = self.extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            raw_text = self.extract_text_from_docx(file_path)
        else:
            return {
                "agent": "CV_AGENT",
                "status": "error",
                "message": "Unsupported file format"
            }
        
        if not raw_text:
            return {
                "agent": "CV_AGENT",
                "status": "error",
                "message": "Could not extract text from CV"
            }
        
        skills = self.extract_skills(raw_text)
        experience_years = self.extract_experience_years(raw_text)
        education = self.extract_education(raw_text)
        cv_score = self.calculate_cv_score(skills, experience_years, education)
        
        confidence = 0.85 if len(skills) > 5 else 0.65
        
        return {
            "agent": "CV_AGENT",
            "status": "done",
            "raw_text": raw_text,
            "skills": skills,
            "experience_years": experience_years,
            "education": education,
            "cv_score": cv_score,
            "confidence_score": confidence
        }