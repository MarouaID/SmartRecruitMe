import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Check, X, Sparkles, Zap, Crown } from 'lucide-react';
import Logo from '../components/Logo';
import Footer from '../components/Footer';

const PricingPage: React.FC = () => {
  const [billingCycle, setBillingCycle] = useState<'monthly' | 'yearly'>('monthly');

  const plans = [
    {
      name: 'Free',
      icon: Sparkles,
      price: { monthly: 0, yearly: 0 },
      description: 'Pour découvrir la plateforme',
      features: [
        { text: '5 analyses CV/mois', included: true },
        { text: '2 analyses GitHub/mois', included: true },
        { text: 'Matching basique', included: true },
        { text: '1 offre d\'emploi active', included: true },
        { text: 'Support email', included: true },
        { text: 'Analytics avancés', included: false },
        { text: 'Export PDF', included: false },
        { text: 'API Access', included: false },
      ],
      cta: 'Commencer gratuitement',
      popular: false,
      gradient: 'from-gray-500 to-gray-600',
    },
    {
      name: 'Pro',
      icon: Zap,
      price: { monthly: 49, yearly: 490 },
      description: 'Pour les recruteurs actifs',
      trial: '30 jours gratuits',
      features: [
        { text: 'Analyses CV illimitées', included: true },
        { text: 'Analyses GitHub illimitées', included: true },
        { text: 'Matching IA avancé', included: true },
        { text: '10 offres d\'emploi actives', included: true },
        { text: 'Support prioritaire', included: true },
        { text: 'Analytics avancés', included: true },
        { text: 'Export PDF illimité', included: true },
        { text: 'Chatbot IA', included: true },
      ],
      cta: 'Essayer 30 jours gratuits',
      popular: true,
      gradient: 'from-primary-600 to-secondary-600',
    },
    {
      name: 'Enterprise',
      icon: Crown,
      price: { monthly: null, yearly: null },
      description: 'Pour les grandes entreprises',
      features: [
        { text: 'Tout du plan Pro', included: true },
        { text: 'Offres illimitées', included: true },
        { text: 'Multi-utilisateurs', included: true },
        { text: 'API complète', included: true },
        { text: 'Support dédié 24/7', included: true },
        { text: 'Formation personnalisée', included: true },
        { text: 'Intégration sur mesure', included: true },
        { text: 'SLA garanti', included: true },
      ],
      cta: 'Contactez-nous',
      popular: false,
      gradient: 'from-purple-600 to-pink-600',
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Navbar */}
      <nav className="bg-white/80 backdrop-blur-md shadow-sm fixed w-full z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <Link to="/">
              <Logo size={48} showText={true} />
            </Link>
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
      <section className="pt-32 pb-12 px-4">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            Tarifs simples et transparents
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Choisissez le plan qui correspond à vos besoins
          </p>

          {/* Billing Toggle */}
          <div className="inline-flex items-center bg-white rounded-full p-1 shadow-md mb-12">
            <button
              onClick={() => setBillingCycle('monthly')}
              className={`px-6 py-2 rounded-full font-semibold transition-all ${
                billingCycle === 'monthly'
                  ? 'bg-gradient-to-r from-primary-600 to-secondary-600 text-white'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Mensuel
            </button>
            <button
              onClick={() => setBillingCycle('yearly')}
              className={`px-6 py-2 rounded-full font-semibold transition-all ${
                billingCycle === 'yearly'
                  ? 'bg-gradient-to-r from-primary-600 to-secondary-600 text-white'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Annuel
              <span className="ml-2 text-xs bg-green-100 text-green-700 px-2 py-1 rounded-full">
                -17%
              </span>
            </button>
          </div>
        </div>
      </section>

      {/* Pricing Cards */}
      <section className="pb-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {plans.map((plan, index) => {
              const Icon = plan.icon;
              const price = plan.price[billingCycle];
              
              return (
                <div
                  key={index}
                  className={`relative bg-white rounded-2xl shadow-xl overflow-hidden transform transition-all hover:scale-105 ${
                    plan.popular ? 'ring-4 ring-primary-500' : ''
                  }`}
                >
                  {plan.popular && (
                    <div className="absolute top-0 right-0 bg-gradient-to-r from-primary-600 to-secondary-600 text-white px-4 py-1 text-sm font-semibold rounded-bl-lg">
                      Le plus populaire
                    </div>
                  )}

                  <div className={`bg-gradient-to-r ${plan.gradient} p-8 text-white`}>
                    <Icon className="w-12 h-12 mb-4" />
                    <h3 className="text-2xl font-bold mb-2">{plan.name}</h3>
                    <p className="text-white/80 mb-4">{plan.description}</p>
                    
                    {price !== null ? (
                      <div className="flex items-baseline">
                        <span className="text-5xl font-bold">{price}€</span>
                        <span className="ml-2 text-white/80">
                          /{billingCycle === 'monthly' ? 'mois' : 'an'}
                        </span>
                      </div>
                    ) : (
                      <div className="text-3xl font-bold">Sur devis</div>
                    )}

                    {plan.trial && (
                      <div className="mt-2 text-sm bg-white/20 inline-block px-3 py-1 rounded-full">
                        🎁 {plan.trial}
                      </div>
                    )}
                  </div>

                  <div className="p-8">
                    <ul className="space-y-4 mb-8">
                      {plan.features.map((feature, idx) => (
                        <li key={idx} className="flex items-start">
                          {feature.included ? (
                            <Check className="w-5 h-5 text-green-600 mr-3 flex-shrink-0 mt-0.5" />
                          ) : (
                            <X className="w-5 h-5 text-gray-300 mr-3 flex-shrink-0 mt-0.5" />
                          )}
                          <span className={feature.included ? 'text-gray-700' : 'text-gray-400'}>
                            {feature.text}
                          </span>
                        </li>
                      ))}
                    </ul>

                    <Link
                      to="/register"
                      className={`block w-full text-center py-3 rounded-lg font-semibold transition-all ${
                        plan.popular
                          ? 'bg-gradient-to-r from-primary-600 to-secondary-600 text-white hover:shadow-xl'
                          : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                      }`}
                    >
                      {plan.cta}
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-4">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
            Questions fréquentes
          </h2>
          <div className="space-y-6">
            <div className="bg-gray-50 p-6 rounded-xl">
              <h3 className="font-bold text-gray-900 mb-2">
                Puis-je changer de plan à tout moment ?
              </h3>
              <p className="text-gray-600">
                Oui, vous pouvez upgrader ou downgrader votre plan à tout moment. Les changements prennent effet immédiatement.
              </p>
            </div>
            <div className="bg-gray-50 p-6 rounded-xl">
              <h3 className="font-bold text-gray-900 mb-2">
                Comment fonctionne l'essai gratuit de 30 jours ?
              </h3>
              <p className="text-gray-600">
                Aucune carte bancaire requise. Vous avez accès à toutes les fonctionnalités Pro pendant 30 jours. Vous pouvez annuler à tout moment.
              </p>
            </div>
            <div className="bg-gray-50 p-6 rounded-xl">
              <h3 className="font-bold text-gray-900 mb-2">
                Quels moyens de paiement acceptez-vous ?
              </h3>
              <p className="text-gray-600">
                Nous acceptons les cartes bancaires (Visa, Mastercard, Amex) et les virements bancaires pour les plans Enterprise.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-primary-600 to-secondary-600 text-white">
        <div className="max-w-4xl mx-auto text-center px-4">
          <h2 className="text-4xl font-bold mb-6">
            Prêt à commencer ?
          </h2>
          <p className="text-xl mb-8 text-primary-100">
            Rejoignez des centaines d'entreprises qui recrutent intelligemment
          </p>
          <Link
            to="/register"
            className="inline-block bg-white text-primary-600 px-10 py-4 rounded-xl font-semibold text-lg hover:shadow-2xl transition-all transform hover:scale-105"
          >
            Essayer gratuitement
          </Link>
        </div>
      </section>
      <Footer />
    </div>
  );
};

export default PricingPage;
