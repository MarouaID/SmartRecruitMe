import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Building2, Mail, Phone, CheckCircle } from 'lucide-react';
import toast from 'react-hot-toast';

const EnterprisePage: React.FC = () => {
  const [form, setForm] = useState({ name: '', email: '', company: '', message: '' });
  const [submitting, setSubmitting] = useState(false);

  const handleChange = (key: string, value: string) => {
    setForm((prev) => ({ ...prev, [key]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      // Placeholder: send to backend when available.
      await new Promise((resolve) => setTimeout(resolve, 800));
      toast.success('Votre demande a bien été envoyée, nous revenons vers vous rapidement.');
      setForm({ name: '', email: '', company: '', message: '' });
    } catch (error) {
      toast.error('Une erreur est survenue, veuillez réessayer.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <nav className="bg-white/80 backdrop-blur-md shadow-sm fixed w-full z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <Link to="/" className="flex items-center gap-3">
              <Building2 className="w-8 h-8 text-primary-600" />
              <span className="text-xl font-bold text-gray-900">SmartRecruitMe</span>
            </Link>
            <div className="flex items-center space-x-4">
              <Link to="/pricing" className="text-gray-700 hover:text-primary-600 font-medium">
                Tarifs
              </Link>
              <Link to="/login" className="bg-primary-600 text-white px-5 py-2 rounded-lg font-semibold hover:shadow-lg transition-all">
                Connexion
              </Link>
            </div>
          </div>
        </div>
      </nav>

      <header className="pt-28 pb-20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Solutions entreprise pour recruter plus vite et mieux
          </h1>
          <p className="text-lg text-gray-600 mb-8">
            Des outils intelligents pour analyser des milliers de candidatures, générer des rapports PDF et collaborer en équipe.
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <Link
              to="/register"
              className="bg-gradient-to-r from-primary-600 to-secondary-600 text-white px-8 py-4 rounded-xl font-semibold hover:shadow-2xl transition-all"
            >
              Commencer l'essai gratuit
            </Link>
            <a
              href="#contact"
              className="bg-white text-gray-800 px-8 py-4 rounded-xl font-semibold border border-gray-200 hover:shadow-lg transition-all"
            >
              Nous contacter
            </a>
          </div>
        </div>
      </header>

      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-10 items-center">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-4">Pourquoi choisir SmartRecruitMe ?</h2>
              <ul className="space-y-4 text-gray-600">
                <li className="flex items-start gap-3">
                  <CheckCircle className="w-6 h-6 text-primary-600 mt-1" />
                  <span>Analyse automatisée des CV avec extraction de compétences et scoring.</span>
                </li>
                <li className="flex items-start gap-3">
                  <CheckCircle className="w-6 h-6 text-primary-600 mt-1" />
                  <span>Tableaux de bord et métriques en temps réel pour piloter vos recrutements.</span>
                </li>
                <li className="flex items-start gap-3">
                  <CheckCircle className="w-6 h-6 text-primary-600 mt-1" />
                  <span>Export PDF professionnel pour partager les profils avec les décideurs.</span>
                </li>
                <li className="flex items-start gap-3">
                  <CheckCircle className="w-6 h-6 text-primary-600 mt-1" />
                  <span>Support dédié et accompagnement à l'intégration.</span>
                </li>
              </ul>
            </div>
            <div className="bg-white rounded-2xl shadow-xl p-10">
              <h3 className="text-2xl font-bold text-gray-900 mb-6">Contactez notre équipe Enterprise</h3>
              <form onSubmit={handleSubmit} className="space-y-4" id="contact">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Nom complet</label>
                  <input
                    type="text"
                    value={form.name}
                    onChange={(e) => handleChange('name', e.target.value)}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
                  <input
                    type="email"
                    value={form.email}
                    onChange={(e) => handleChange('email', e.target.value)}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Entreprise</label>
                  <input
                    type="text"
                    value={form.company}
                    onChange={(e) => handleChange('company', e.target.value)}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Message</label>
                  <textarea
                    value={form.message}
                    onChange={(e) => handleChange('message', e.target.value)}
                    rows={4}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    required
                  />
                </div>
                <button
                  type="submit"
                  disabled={submitting}
                  className="w-full bg-primary-600 hover:bg-primary-700 text-white font-semibold py-3 rounded-lg transition-all disabled:opacity-50"
                >
                  {submitting ? 'Envoi...' : 'Envoyer ma demande'}
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-gray-900 text-center mb-10">Ils nous font confiance</h2>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-10 items-center">
            <div className="bg-gray-50 p-6 rounded-2xl flex items-center justify-center">
              <span className="text-xl font-bold text-gray-400">Logo</span>
            </div>
            <div className="bg-gray-50 p-6 rounded-2xl flex items-center justify-center">
              <span className="text-xl font-bold text-gray-400">Logo</span>
            </div>
            <div className="bg-gray-50 p-6 rounded-2xl flex items-center justify-center">
              <span className="text-xl font-bold text-gray-400">Logo</span>
            </div>
            <div className="bg-gray-50 p-6 rounded-2xl flex items-center justify-center">
              <span className="text-xl font-bold text-gray-400">Logo</span>
            </div>
          </div>
        </div>
      </section>

      <footer className="bg-gray-800 text-white py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-sm">© {new Date().getFullYear()} SmartRecruitMe — Tous droits réservés.</p>
        </div>
      </footer>
    </div>
  );
};

export default EnterprisePage;
