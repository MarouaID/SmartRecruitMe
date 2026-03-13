import React, { useEffect, useRef, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { recruiterAPI } from '../services/api';
import { ArrowLeft, Download } from 'lucide-react';
import toast from 'react-hot-toast';
import Footer from '../components/Footer';

const CandidateDetail: React.FC = () => {
  const { candidateId } = useParams<{ candidateId: string }>();
  const navigate = useNavigate();
  const [candidate, setCandidate] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const printableRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const fetchCandidate = async () => {
      try {
        const res = await recruiterAPI.getCandidateDetail(Number(candidateId));
        setCandidate(res.data);
      } catch (error) {
        toast.error('Impossible de récupérer le profil du candidat');
      } finally {
        setLoading(false);
      }
    };

    if (candidateId) {
      fetchCandidate();
    }
  }, [candidateId]);

  const handleExportPdf = () => {
    if (!printableRef.current) return;
    window.print();
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center h-16">
            <button
              onClick={() => navigate('/recruiter/dashboard')}
              className="flex items-center space-x-2 text-gray-600 hover:text-gray-900 transition-all"
            >
              <ArrowLeft className="w-5 h-5" />
              <span>Retour</span>
            </button>
          </div>
        </div>
      </nav>

      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        {loading ? (
          <div className="space-y-4">
            <div className="h-12 bg-white rounded-xl shadow-md animate-pulse" />
            <div className="h-64 bg-white rounded-xl shadow-md animate-pulse" />
          </div>
        ) : (
          candidate && (
            <div className="space-y-6">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                <div>
                  <h1 className="text-3xl font-bold text-gray-900">{candidate.full_name}</h1>
                  <p className="text-gray-600">{candidate.email}</p>
                </div>
                <button
                  onClick={handleExportPdf}
                  className="inline-flex items-center gap-2 bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-xl font-semibold transition-all"
                >
                  <Download className="w-4 h-4" />
                  Exporter en PDF
                </button>
              </div>

              <div ref={printableRef} className="bg-white rounded-2xl shadow-md p-8">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Résumé du candidat</h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <h3 className="text-sm font-semibold text-gray-700 mb-2">Compétences</h3>
                    <div className="flex flex-wrap gap-2">
                      {candidate.cv_analysis?.skills?.map((skill: string, idx: number) => (
                        <span key={idx} className="px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-xs font-medium">
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div>
                    <h3 className="text-sm font-semibold text-gray-700 mb-2">Score</h3>
                    <div className="grid grid-cols-2 gap-4">
                      <div className="bg-gray-50 rounded-xl p-4">
                        <p className="text-xs text-gray-500">CV</p>
                        <p className="text-2xl font-bold text-gray-900">{Math.round(candidate.cv_analysis?.cv_score || 0)}%</p>
                      </div>
                      <div className="bg-gray-50 rounded-xl p-4">
                        <p className="text-xs text-gray-500">GitHub</p>
                        <p className="text-2xl font-bold text-gray-900">{Math.round(candidate.github_analysis?.github_score || 0)}%</p>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="mt-8">
                  <h3 className="text-sm font-semibold text-gray-700 mb-2">Détails GitHub</h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="bg-gray-50 rounded-xl p-4">
                      <p className="text-xs text-gray-500">Projets</p>
                      <p className="text-xl font-bold text-gray-900">{candidate.github_analysis?.total_repos ?? 0}</p>
                    </div>
                    <div className="bg-gray-50 rounded-xl p-4">
                      <p className="text-xs text-gray-500">Commits</p>
                      <p className="text-xl font-bold text-gray-900">{candidate.github_analysis?.total_commits ?? 0}</p>
                    </div>
                    <div className="bg-gray-50 rounded-xl p-4">
                      <p className="text-xs text-gray-500">Langages</p>
                      <p className="text-xl font-bold text-gray-900">{candidate.github_analysis?.top_languages?.slice(0, 3).join(', ') || '—'}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )
        )}
      </div>
      <Footer />
    </div>
  );
};

export default CandidateDetail;
