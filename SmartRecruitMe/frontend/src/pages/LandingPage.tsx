import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Brain, Github, Target, Sparkles, Users, TrendingUp, Shield, Zap, CheckCircle } from 'lucide-react';
import Logo from '../components/Logo';

const LandingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Navbar */}
      <nav className="bg-white/80 backdrop-blur-md shadow-sm fixed w-full z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <Logo size={48} showText={true} />
            <div className="flex items-center space-x-4">
              <Link
                to="/login"
                className="text-gray-700 hover:text-primary-600 font-medium transition-colors"
              >
                Connexion
              </Link>
              <Link
                to="/register"
                className="bg-gradient-to-r from-primary-600 to-secondary-600 text-white px-6 py-2 rounded-lg font-semibold hover:shadow-lg transition-all"
              >
                Commencer
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center bg-primary-50 text-primary-700 px-4 py-2 rounded-full mb-6 animate-fade-in">
            <Sparkles className="w-4 h-4 mr-2" />
            <span className="text-sm font-semibold">Plateforme IA de Recrutement Intelligent</span>
          </div>
          
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6 animate-fade-in-up">
            Recrutez <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600">au-delà du CV</span>
          </h1>
          
          <p className="text-xl text-gray-600 mb-10 max-w-3xl mx-auto animate-fade-in-up animation-delay-200">
            SmartRecruitMe combine l'analyse de CV et l'évaluation GitHub pour révéler le vrai potentiel des candidats grâce à l'intelligence artificielle.
          </p>
          
          <div className="flex flex-col sm:flex-row justify-center gap-4 mb-16 animate-fade-in-up animation-delay-400">
            <Link
              to="/register"
              className="bg-gradient-to-r from-primary-600 to-secondary-600 text-white px-8 py-4 rounded-xl font-semibold text-lg hover:shadow-2xl transition-all transform hover:scale-105 flex items-center justify-center"
            >
              Essai gratuit 30 jours
              <ArrowRight className="ml-2 w-5 h-5" />
            </Link>
            <a
              href="#features"
              className="bg-white text-gray-700 px-8 py-4 rounded-xl font-semibold text-lg hover:shadow-lg transition-all border-2 border-gray-200"
            >
              Découvrir les fonctionnalités
            </a>
          </div>

          {/* Hero Image/Illustration */}
          <div className="relative animate-fade-in-up animation-delay-600">
            <div className="bg-gradient-to-br from-primary-500 to-secondary-600 rounded-2xl shadow-2xl p-8 max-w-5xl mx-auto">
              <div className="bg-white rounded-xl p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="text-center p-4 bg-gradient-to-br from-blue-50 to-blue-100 rounded-lg">
                  <Brain className="w-12 h-12 text-primary-600 mx-auto mb-3" />
                  <h3 className="font-bold text-gray-900 mb-1">Analyse CV</h3>
                  <p className="text-sm text-gray-600">Extraction intelligente des compétences</p>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-purple-50 to-purple-100 rounded-lg">
                  <Github className="w-12 h-12 text-secondary-600 mx-auto mb-3" />
                  <h3 className="font-bold text-gray-900 mb-1">Évaluation GitHub</h3>
                  <p className="text-sm text-gray-600">Analyse de l'activité réelle</p>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-green-50 to-green-100 rounded-lg">
                  <Target className="w-12 h-12 text-green-600 mx-auto mb-3" />
                  <h3 className="font-bold text-gray-900 mb-1">Matching IA</h3>
                  <p className="text-sm text-gray-600">Correspondance sémantique avancée</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Pourquoi SmartRecruitMe ?
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Une plateforme complète qui révolutionne le recrutement avec l'IA
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-2xl hover:shadow-xl transition-all transform hover:-translate-y-2">
              <div className="bg-primary-600 w-14 h-14 rounded-xl flex items-center justify-center mb-4">
                <Brain className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">Analyse CV Intelligente</h3>
              <p className="text-gray-600 mb-4">
                Extraction automatique des compétences, expérience et formation avec scoring précis.
              </p>
              <ul className="space-y-2">
                <li className="flex items-start text-sm text-gray-700">
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                  Support PDF et DOCX
                </li>
                <li className="flex items-start text-sm text-gray-700">
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                  Détection de 50+ compétences techniques
                </li>
              </ul>
            </div>

            {/* Feature 2 */}
            <div className="bg-gradient-to-br from-purple-50 to-purple-100 p-8 rounded-2xl hover:shadow-xl transition-all transform hover:-translate-y-2">
              <div className="bg-secondary-600 w-14 h-14 rounded-xl flex items-center justify-center mb-4">
                <Github className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">Évaluation GitHub</h3>
              <p className="text-gray-600 mb-4">
                Analyse approfondie de l'activité GitHub pour évaluer les compétences réelles.
              </p>
              <ul className="space-y-2">
                <li className="flex items-start text-sm text-gray-700">
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                  Diversité des langages
                </li>
                <li className="flex items-start text-sm text-gray-700">
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                  Régularité et collaboration
                </li>
              </ul>
            </div>

            {/* Feature 3 */}
            <div className="bg-gradient-to-br from-green-50 to-green-100 p-8 rounded-2xl hover:shadow-xl transition-all transform hover:-translate-y-2">
              <div className="bg-green-600 w-14 h-14 rounded-xl flex items-center justify-center mb-4">
                <Target className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">Matching Sémantique</h3>
              <p className="text-gray-600 mb-4">
                IA avancée pour matcher candidats et offres avec précision.
              </p>
              <ul className="space-y-2">
                <li className="flex items-start text-sm text-gray-700">
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                  Sentence Transformers
                </li>
                <li className="flex items-start text-sm text-gray-700">
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                  Score de correspondance détaillé
                </li>
              </ul>
            </div>

            {/* Feature 4 */}
            <div className="bg-gradient-to-br from-orange-50 to-orange-100 p-8 rounded-2xl hover:shadow-xl transition-all transform hover:-translate-y-2">
              <div className="bg-orange-600 w-14 h-14 rounded-xl flex items-center justify-center mb-4">
                <TrendingUp className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">Analytics Avancés</h3>
              <p className="text-gray-600">
                Tableaux de bord et statistiques pour optimiser vos recrutements.
              </p>
            </div>

            {/* Feature 5 */}
            <div className="bg-gradient-to-br from-pink-50 to-pink-100 p-8 rounded-2xl hover:shadow-xl transition-all transform hover:-translate-y-2">
              <div className="bg-pink-600 w-14 h-14 rounded-xl flex items-center justify-center mb-4">
                <Zap className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">Temps Réel</h3>
              <p className="text-gray-600">
                Notifications instantanées et analyses en temps réel.
              </p>
            </div>

            {/* Feature 6 */}
            <div className="bg-gradient-to-br from-indigo-50 to-indigo-100 p-8 rounded-2xl hover:shadow-xl transition-all transform hover:-translate-y-2">
              <div className="bg-indigo-600 w-14 h-14 rounded-xl flex items-center justify-center mb-4">
                <Shield className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">Sécurisé & Conforme</h3>
              <p className="text-gray-600">
                Données chiffrées et conformité RGPD garantie.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 bg-gradient-to-r from-primary-600 to-secondary-600 text-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
            <div>
              <div className="text-5xl font-bold mb-2">95%</div>
              <div className="text-primary-100">Précision de matching</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">10x</div>
              <div className="text-primary-100">Plus rapide qu'un recrutement classique</div>
            </div>
            <div>
              <div className="text-5xl font-bold mb-2">50+</div>
              <div className="text-primary-100">Compétences techniques détectées</div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto text-center px-4">
          <h2 className="text-4xl font-bold text-gray-900 mb-6">
            Prêt à révolutionner vos recrutements ?
          </h2>
          <p className="text-xl text-gray-600 mb-8">
            Rejoignez les entreprises qui recrutent intelligemment avec l'IA
          </p>
          <Link
            to="/register"
            className="inline-flex items-center bg-gradient-to-r from-primary-600 to-secondary-600 text-white px-10 py-4 rounded-xl font-semibold text-lg hover:shadow-2xl transition-all transform hover:scale-105"
          >
            Commencer gratuitement
            <ArrowRight className="ml-2 w-5 h-5" />
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-12">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <div className="mb-4">
                <Logo size={48} showText={false} />
              </div>
              <p className="text-sm text-gray-400">
                Au-delà du CV - Recrutement intelligent par IA
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Produit</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#features" className="hover:text-white transition-colors">Fonctionnalités</a></li>
                <li><Link to="/pricing" className="hover:text-white transition-colors">Tarifs</Link></li>
                <li><a href="#" className="hover:text-white transition-colors">Documentation</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Entreprise</h4>
              <ul className="space-y-2 text-sm">
                <li><Link to="/pour-les-entreprises" className="hover:text-white transition-colors">Pour les entreprises</Link></li>
                <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Légal</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition-colors">Confidentialité</a></li>
                <li><a href="#" className="hover:text-white transition-colors">CGU</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 pt-8 text-center text-sm text-gray-400">
            <p>&copy; 2024 SmartRecruitMe - Team ARIA (Azar Aghrib & Maroua Idomar) - ENSA GI4</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
