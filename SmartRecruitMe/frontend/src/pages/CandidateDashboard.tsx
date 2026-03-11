import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { candidateAPI } from '../services/api';
import { Upload, Github, Briefcase, Star, MapPin, LogOut, TrendingUp, Award } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, ResponsiveContainer } from 'recharts';
import toast from 'react-hot-toast';

const CandidateDashboard: React.FC = () => {
  const [profile, setProfile] = useState<any>(null);
  const [matchingJobs, setMatchingJobs] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const { logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [profileRes, jobsRes] = await Promise.all([
        candidateAPI.getProfile(),
        candidateAPI.getMatchingJobs(),
      ]);
      setProfile(profileRes.data);
      setMatchingJobs(jobsRes.data);
    } catch (error) {
      toast.error('Erreur lors du chargement des données');
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setUploading(true);
    try {
      await candidateAPI.uploadCV(file);
      toast.success('CV uploadé et analysé avec succès !');
      loadData();
    } catch (error) {
      toast.error('Erreur lors de l\'upload du CV');
    } finally {
      setUploading(false);
    }
  };

  const handleAnalyzeGitHub = async () => {
    try {
      await candidateAPI.analyzeGitHub();
      toast.success('Analyse GitHub effectuée !');
      loadData();
    } catch (error) {
      toast.error('Erreur lors de l\'analyse GitHub');
    }
  };

  const radarData = profile?.cv_analysis ? [
    { subject: 'Compétences', value: profile.cv_analysis.cv_score || 0 },
    { subject: 'Expérience', value: (profile.cv_analysis.experience_years || 0) * 10 },
    { subject: 'GitHub', value: profile.github_analysis?.github_score || 0 },
    { subject: 'Régularité', value: (profile.github_analysis?.regularity_score || 0) * 100 },
    { subject: 'Collaboration', value: (profile.github_analysis?.collaboration_score || 0) * 100 },
  ] : [];

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
                <Award className="w-6 h-6 text-white" />
              </div>
              <h1 className="text-2xl font-bold text-gray-900">SmartRecruitMe</h1>
            </div>
            <button
              onClick={logout}
              className="text-gray-600 hover:text-gray-900 transition-all"
            >
              <LogOut className="w-5 h-5" />
            </button>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-1 space-y-6">
            <div className="bg-white rounded-xl shadow-md p-6">
              <div className="text-center mb-6">
                <div className="w-24 h-24 bg-gradient-to-br from-primary-500 to-secondary-500 rounded-full mx-auto mb-4 flex items-center justify-center text-white text-3xl font-bold">
                  {profile?.full_name?.charAt(0) || 'U'}
                </div>
                <h2 className="text-2xl font-bold text-gray-900">{profile?.full_name}</h2>
                <p className="text-gray-600">{profile?.email}</p>
                {profile?.location && (
                  <div className="flex items-center justify-center space-x-1 text-gray-600 mt-2">
                    <MapPin className="w-4 h-4" />
                    <span>{profile.location}</span>
                  </div>
                )}
              </div>

              <div className="space-y-3">
                <label className="block">
                  <input
                    type="file"
                    accept=".pdf,.docx"
                    onChange={handleFileUpload}
                    className="hidden"
                    id="cv-upload"
                  />
                  <label
                    htmlFor="cv-upload"
                    className="flex items-center justify-center space-x-2 w-full bg-primary-600 hover:bg-primary-700 text-white font-semibold py-3 rounded-lg cursor-pointer transition-all"
                  >
                    {uploading ? (
                      <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                    ) : (
                      <>
                        <Upload className="w-5 h-5" />
                        <span>Uploader CV</span>
                      </>
                    )}
                  </label>
                </label>

                {profile?.github_username && (
                  <button
                    onClick={handleAnalyzeGitHub}
                    className="flex items-center justify-center space-x-2 w-full bg-gray-800 hover:bg-gray-900 text-white font-semibold py-3 rounded-lg transition-all"
                  >
                    <Github className="w-5 h-5" />
                    <span>Analyser GitHub</span>
                  </button>
                )}
              </div>

              {profile?.cv_analysis && (
                <div className="mt-6 pt-6 border-t border-gray-200">
                  <h3 className="font-semibold text-gray-900 mb-3">Scores</h3>
                  <div className="space-y-3">
                    <div>
                      <div className="flex justify-between text-sm mb-1">
                        <span className="text-gray-600">CV</span>
                        <span className="font-semibold">{Math.round(profile.cv_analysis.cv_score)}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div
                          className="bg-primary-600 h-2 rounded-full transition-all"
                          style={{ width: `${profile.cv_analysis.cv_score}%` }}
                        ></div>
                      </div>
                    </div>

                    {profile.github_analysis && (
                      <div>
                        <div className="flex justify-between text-sm mb-1">
                          <span className="text-gray-600">GitHub</span>
                          <span className="font-semibold">{Math.round(profile.github_analysis.github_score)}%</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                          <div
                            className="bg-green-600 h-2 rounded-full transition-all"
                            style={{ width: `${profile.github_analysis.github_score}%` }}
                          ></div>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>

            {profile?.cv_analysis && radarData.length > 0 && (
              <div className="bg-white rounded-xl shadow-md p-6">
                <h3 className="font-semibold text-gray-900 mb-4">Profil de compétences</h3>
                <ResponsiveContainer width="100%" height={250}>
                  <RadarChart data={radarData}>
                    <PolarGrid />
                    <PolarAngleAxis dataKey="subject" />
                    <PolarRadiusAxis angle={90} domain={[0, 100]} />
                    <Radar name="Score" dataKey="value" stroke="#0ea5e9" fill="#0ea5e9" fillOpacity={0.6} />
                  </RadarChart>
                </ResponsiveContainer>
              </div>
            )}
          </div>

          <div className="lg:col-span-2 space-y-6">
            {profile?.cv_analysis && (
              <div className="bg-white rounded-xl shadow-md p-6">
                <h3 className="text-xl font-bold text-gray-900 mb-4">Mes compétences</h3>
                <div className="flex flex-wrap gap-2">
                  {profile.cv_analysis.skills.map((skill: string, idx: number) => (
                    <span
                      key={idx}
                      className="px-4 py-2 bg-primary-100 text-primary-800 rounded-lg text-sm font-medium"
                    >
                      {skill}
                    </span>
                  ))}
                </div>

                {profile.github_analysis && (
                  <div className="mt-6">
                    <h4 className="font-semibold text-gray-900 mb-3">Soft Skills (GitHub)</h4>
                    <div className="flex flex-wrap gap-2">
                      {profile.github_analysis.inferred_softskills.map((skill: string, idx: number) => (
                        <span
                          key={idx}
                          className="px-4 py-2 bg-green-100 text-green-800 rounded-lg text-sm font-medium"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            <div className="bg-white rounded-xl shadow-md p-6">
              <h3 className="text-xl font-bold text-gray-900 mb-4">Offres compatibles</h3>
              <div className="space-y-4">
                {matchingJobs.length === 0 ? (
                  <div className="text-center py-12">
                    <Briefcase className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                    <p className="text-gray-500">Aucune offre compatible pour le moment</p>
                    <p className="text-sm text-gray-400 mt-2">Uploadez votre CV pour voir les offres</p>
                  </div>
                ) : (
                  matchingJobs.map((job) => (
                    <div
                      key={job.job_id}
                      className="border border-gray-200 rounded-lg p-5 hover:shadow-lg transition-all"
                    >
                      <div className="flex items-start justify-between mb-3">
                        <div>
                          <h4 className="text-lg font-bold text-gray-900">{job.title}</h4>
                          <p className="text-gray-600">{job.company}</p>
                        </div>
                        <div className="px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-sm font-bold">
                          {Math.round(job.match_score)}% match
                        </div>
                      </div>

                      {job.location && (
                        <div className="flex items-center space-x-1 text-gray-600 text-sm mb-3">
                          <MapPin className="w-4 h-4" />
                          <span>{job.location}</span>
                        </div>
                      )}

                      <div className="mb-3">
                        <p className="text-sm text-gray-600 mb-2">Compétences matchées:</p>
                        <div className="flex flex-wrap gap-2">
                          {job.matched_skills.slice(0, 5).map((skill: string, idx: number) => (
                            <span key={idx} className="px-2 py-1 bg-green-100 text-green-800 rounded text-xs font-medium">
                              {skill}
                            </span>
                          ))}
                        </div>
                      </div>

                      {job.missing_skills.length > 0 && (
                        <div>
                          <p className="text-sm text-gray-600 mb-2">À développer:</p>
                          <div className="flex flex-wrap gap-2">
                            {job.missing_skills.slice(0, 3).map((skill: string, idx: number) => (
                              <span key={idx} className="px-2 py-1 bg-orange-100 text-orange-800 rounded text-xs font-medium">
                                {skill}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  ))
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CandidateDashboard;
