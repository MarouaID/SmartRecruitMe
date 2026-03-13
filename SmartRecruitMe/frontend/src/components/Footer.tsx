import React from 'react';
import { Link } from 'react-router-dom';
import { Github, Linkedin, Twitter } from 'lucide-react';
import Logo from './Logo';

const Footer: React.FC = () => (
  <footer className="bg-white border-t border-gray-200">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div>
          <div className="flex items-center space-x-3">
            <Logo size={40} showText={false} />
            <div>
              <h3 className="text-xl font-bold text-gray-900">SmartRecruitMe</h3>
              <p className="text-gray-600">Au-delà du CV</p>
            </div>
          </div>
          <p className="mt-6 text-gray-600 text-sm">
            Une plateforme IA qui aide les candidats et recruteurs à mieux se connecter grâce à une analyse intelligente.
          </p>
          <div className="flex items-center mt-6 space-x-4">
            <a href="https://github.com" target="_blank" rel="noreferrer" className="text-gray-500 hover:text-gray-900">
              <Github className="w-5 h-5" />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="text-gray-500 hover:text-gray-900">
              <Linkedin className="w-5 h-5" />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noreferrer" className="text-gray-500 hover:text-gray-900">
              <Twitter className="w-5 h-5" />
            </a>
          </div>
        </div>

        <div>
          <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wide">Navigation</h4>
          <ul className="mt-4 space-y-2 text-gray-600 text-sm">
            <li>
              <Link to="/" className="hover:text-gray-900">
                Accueil
              </Link>
            </li>
            <li>
              <Link to="/pricing" className="hover:text-gray-900">
                Tarifs
              </Link>
            </li>
            <li>
              <Link to="/pour-les-entreprises" className="hover:text-gray-900">
                Pour les entreprises
              </Link>
            </li>
            <li>
              <Link to="/login" className="hover:text-gray-900">
                Connexion
              </Link>
            </li>
          </ul>
        </div>

        <div>
          <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wide">Contact</h4>
          <p className="mt-4 text-gray-600 text-sm">
            Email: <a className="text-primary-600 hover:underline" href="mailto:contact@smartrecruitme.com">contact@smartrecruitme.com</a>
          </p>
          <p className="mt-2 text-gray-600 text-sm">Téléphone: +33 1 23 45 67 89</p>
          <p className="mt-4 text-gray-600 text-sm">© {new Date().getFullYear()} SmartRecruitMe. Tous droits réservés.</p>
        </div>
      </div>
    </div>
  </footer>
);

export default Footer;
