import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import { Toaster } from 'react-hot-toast';
import LandingPage from './pages/LandingPage';
import PricingPage from './pages/PricingPage';
import EnterprisePage from './pages/EnterprisePage';
import Login from './pages/Login';
import Register from './pages/Register';
import CandidateDashboard from './pages/CandidateDashboard';
import RecruiterDashboard from './pages/RecruiterDashboard';
import CreateJobOffer from './pages/CreateJobOffer';
import AnalyticsPage from './pages/AnalyticsPage';
import CandidateDetail from './pages/CandidateDetail';

const PrivateRoute: React.FC<{ children: React.ReactNode; role?: string }> = ({ children, role }) => {
  const { isAuthenticated, role: userRole } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  if (role && userRole !== role) {
    return <Navigate to={userRole === 'candidate' ? '/candidate/dashboard' : '/recruiter/dashboard'} />;
  }

  return <>{children}</>;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <Toaster
          position="top-right"
          toastOptions={{
            duration: 3000,
            style: {
              background: '#363636',
              color: '#fff',
            },
            success: {
              duration: 3000,
              iconTheme: {
                primary: '#10b981',
                secondary: '#fff',
              },
            },
            error: {
              duration: 4000,
              iconTheme: {
                primary: '#ef4444',
                secondary: '#fff',
              },
            },
          }}
        />
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/pricing" element={<PricingPage />} />
          <Route path="/pour-les-entreprises" element={<EnterprisePage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route
            path="/candidate/dashboard"
            element={
              <PrivateRoute role="candidate">
                <CandidateDashboard />
              </PrivateRoute>
            }
          />

          <Route
            path="/recruiter/dashboard"
            element={
              <PrivateRoute role="recruiter">
                <RecruiterDashboard />
              </PrivateRoute>
            }
          />

          <Route
            path="/recruiter/analytics"
            element={
              <PrivateRoute role="recruiter">
                <AnalyticsPage />
              </PrivateRoute>
            }
          />

          <Route
            path="/recruiter/candidate/:candidateId"
            element={
              <PrivateRoute role="recruiter">
                <CandidateDetail />
              </PrivateRoute>
            }
          />

          <Route
            path="/recruiter/create-job"
            element={
              <PrivateRoute role="recruiter">
                <CreateJobOffer />
              </PrivateRoute>
            }
          />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
