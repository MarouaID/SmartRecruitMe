import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { recruiterAPI } from '../services/api';
import { Users, Briefcase, TrendingUp, Search, Star, Github, MapPin, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import toast from 'react-hot-toast';

const RecruiterDashboard: React.FC = () => {
  const [jobOffers, setJobOffers] = useState<any[]>([]);
  const [selectedJob, setSelectedJob] = useState<any>(null);
  const [candidates, setCandidates] = useState<any[]>([]);
  const [stats, setStats] = useState<any>({});
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const { logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [jobsRes, statsRes] = await Promise.all([
        recruiterAPI.getJobOffers(),
        recruiterAPI.getDashboardStats(),
      ]);
      setJobOffers(jobsRes.data);
      setStats(statsRes.data);
      
      if (jobsRes.data.length > 0) {
        loadCandidatesForJob(jobsRes.data[0].id);
      }
    } catch (error) {
      toast.error('Erreur lors du chargement des données');
    } finally {
      setLoading(false);
    }
  };

  const loadCandidatesForJob = async (jobId: number) => {
    try {
      const job = jobOffers.find(j => j.id === jobId);
      setSelectedJob(job);
      
      const response = await recruiterAPI.getCandidatesForJob(jobId);
      setCandidates(response.data);
    } catch (error) {
      toast.error('Erreur lors du chargement des candidats');
    }
  };

  const handleMatchCandidates = async (jobId: number) => {
    try {
      await recruiterAPI.matchCandidates(jobId);
      toast.success('Matching des candidats effectué !');
      loadCandidatesForJob(jobId);
    } catch (error) {
      toast.error('Erreur lors du matching');
    }
  };

  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-green-600 bg-green-100';
    if (score >= 60) return 'text-blue-600 bg-blue-100';
    if (score >= 40) return 'text-yellow-600 bg-yellow-100';
    return 'text-red-600 bg-red-100';
  };

  const filteredCandidates = candidates.filter(c =>
    c.candidate_name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-16 h-16 border-4 border-primary-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center">
                <Briefcase className="w-6 h-6 text-white" />
              </div>
              <h1 className="text-2xl font-bold text-gray-900">SmartRecruitMe</h1>
            </div>
            <div className="flex items-center space-x-4">
              <button
                onClick={() => navigate('/recruiter/create-job')}
                className="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-lg font-semibold transition-all"
              >
                + Nouvelle offre
              </button>
              <button
                onClick={logout}
                className="text-gray-600 hover:text-gray-900 transition-all"
              >
                <LogOut className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white rounded-xl shadow-md p-6 border-l-4 border-primary-500">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-gray-600 text-sm font-medium">Offres actives</p>
                <p className="text-3xl font-bold text-gray-900 mt-2">{stats.active_job_offers || 0}</p>
              </div>
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center">
                <Briefcase className="w-6 h-6 text-primary-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-md p-6 border-l-4 border-green-500">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-gray-600 text-sm font-medium">Total candidats</p>
                <p className="text-3xl font-bold text-gray-900 mt-2">{stats.total_candidates || 0}</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                <Users className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-md p-6 border-l-4 border-purple-500">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-gray-600 text-sm font-medium">Taux de matching</p>
                <p className="text-3xl font-bold text-gray-900 mt-2">
                  {candidates.length > 0 ? Math.round(candidates.reduce((acc, c) => acc + c.final_score, 0) / candidates.length) : 0}%
                </p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                <TrendingUp className="w-6 h-6 text-purple-600" />
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-1 bg-white rounded-xl shadow-md p-6">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Mes offres</h2>
            <div className="space-y-3">
              {jobOffers.map((job) => (
                <div
                  key={job.id}
                  onClick={() => loadCandidatesForJob(job.id)}
                  className={`p-4 rounded-lg cursor-pointer transition-all ${
                    selectedJob?.id === job.id
                      ? 'bg-primary-50 border-2 border-primary-500'
                      : 'bg-gray-50 hover:bg-gray-100 border-2 border-transparent'
                  }`}
                >
                  <h3 className="font-semibold text-gray-900">{job.title}</h3>
                  <p className="text-sm text-gray-600 mt-1">{job.location}</p>
                  <div className="flex items-center justify-between mt-2">
                    <span className="text-xs text-gray-500">{job.required_skills.length} compétences</span>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleMatchCandidates(job.id);
                      }}
                      className="text-xs text-primary-600 hover:text-primary-700 font-semibold"
                    >
                      Matcher
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="lg:col-span-2 bg-white rounded-xl shadow-md p-6">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-gray-900">
                Candidats {selectedJob && `pour "${selectedJob.title}"`}
              </h2>
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  placeholder="Rechercher..."
                  className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                />
              </div>
            </div>

            <div className="space-y-4">
              {filteredCandidates.length === 0 ? (
                <div className="text-center py-12">
                  <Users className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                  <p className="text-gray-500">Aucun candidat trouvé</p>
                </div>
              ) : (
                filteredCandidates.map((candidate) => (
                  <div
                    key={candidate.candidate_id}
                    className="border border-gray-200 rounded-lg p-5 hover:shadow-lg transition-all cursor-pointer"
                    onClick={() => navigate(`/recruiter/candidate/${candidate.candidate_id}`)}
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-3 mb-3">
                          <h3 className="text-lg font-bold text-gray-900">{candidate.candidate_name}</h3>
                          <div className={`px-3 py-1 rounded-full text-sm font-bold ${getScoreColor(candidate.final_score)}`}>
                            {Math.round(candidate.final_score)}%
                          </div>
                        </div>

                        <div className="flex flex-wrap gap-2 mb-3">
                          {candidate.matched_skills.slice(0, 5).map((skill: string, idx: number) => (
                            <span key={idx} className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-xs font-medium">
                              {skill}
                            </span>
                          ))}
                        </div>

                        <div className="flex items-center space-x-4 text-sm text-gray-600">
                          <div className="flex items-center space-x-1">
                            <Github className="w-4 h-4" />
                            <span>{candidate.github_highlights.projects_count} projets</span>
                          </div>
                          <div className="flex items-center space-x-1">
                            <Star className="w-4 h-4" />
                            <span>CV: {Math.round(candidate.cv_score)}%</span>
                          </div>
                          <div className="flex items-center space-x-1">
                            <TrendingUp className="w-4 h-4" />
                            <span>GitHub: {Math.round(candidate.github_score)}%</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecruiterDashboard;
