import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { recruiterAPI } from '../services/api';
import { ArrowLeft, BarChart2, TrendingUp } from 'lucide-react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts';
import toast from 'react-hot-toast';
import Footer from '../components/Footer';

const AnalyticsPage: React.FC = () => {
  const [analytics, setAnalytics] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const res = await recruiterAPI.getDashboardAnalytics();
        setAnalytics(res.data);
      } catch (error) {
        toast.error('Impossible de charger les analyses');
      } finally {
        setLoading(false);
      }
    };
    fetchAnalytics();
  }, []);

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

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Analytics</h1>
            <p className="text-gray-600 mt-1">
              Suivez l'évolution des candidatures et découvrez les compétences clés dans votre bassin.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <div className="bg-white rounded-xl shadow-md p-4 flex items-center gap-3">
              <div className="w-10 h-10 bg-primary-50 rounded-lg flex items-center justify-center">
                <TrendingUp className="w-5 h-5 text-primary-600" />
              </div>
              <div>
                <p className="text-xs text-gray-500">Score moyen</p>
                <p className="text-xl font-bold text-gray-900">
                  {loading ? '--' : `${analytics?.average_score ?? 0}%`}
                </p>
              </div>
            </div>
            <div className="bg-white rounded-xl shadow-md p-4 flex items-center gap-3">
              <div className="w-10 h-10 bg-primary-50 rounded-lg flex items-center justify-center">
                <BarChart2 className="w-5 h-5 text-primary-600" />
              </div>
              <div>
                <p className="text-xs text-gray-500">Skills les plus courants</p>
                <p className="text-xl font-bold text-gray-900">{loading ? '--' : analytics?.top_skills?.length ?? 0}</p>
              </div>
            </div>
          </div>
        </div>

        {loading ? (
          <div className="space-y-4">
            <div className="h-48 bg-white rounded-xl shadow-md animate-pulse" />
            <div className="h-64 bg-white rounded-xl shadow-md animate-pulse" />
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="bg-white rounded-xl shadow-md p-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Candidatures au fil du temps</h2>
              <div style={{ height: 320 }}>
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={analytics.applications_over_time || []}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="date" tick={{ fontSize: 12 }} />
                    <YAxis />
                    <Tooltip />
                    <Line type="monotone" dataKey="count" stroke="#0ea5e9" strokeWidth={2} dot={false} />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-md p-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Compétences les plus fréquentes</h2>
              <div style={{ height: 320 }}>
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={analytics.top_skills || []} layout="vertical">
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis type="number" />
                    <YAxis dataKey="skill" type="category" width={140} />
                    <Tooltip />
                    <Bar dataKey="count" fill="#6366f1" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        )}
      </div>
      <Footer />
    </div>
  );
};

export default AnalyticsPage;
