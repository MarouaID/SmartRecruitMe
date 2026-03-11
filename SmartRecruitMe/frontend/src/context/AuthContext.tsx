import React, { createContext, useContext, useState, useEffect } from 'react';
import { authAPI } from '../services/api';

interface AuthContextType {
  user: any;
  token: string | null;
  role: string | null;
  login: (email: string, password: string) => Promise<void>;
  register: (data: any) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<any>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem('token'));
  const [role, setRole] = useState<string | null>(localStorage.getItem('role'));

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }, [token]);

  const login = async (email: string, password: string) => {
    const response = await authAPI.login({ email, password });
    const { access_token, role: userRole, user_id } = response.data;
    setToken(access_token);
    setRole(userRole);
    setUser({ id: user_id, email });
    localStorage.setItem('token', access_token);
    localStorage.setItem('role', userRole);
    localStorage.setItem('userId', user_id);
  };

  const register = async (data: any) => {
    const response = await authAPI.register(data);
    const { access_token, role: userRole, user_id } = response.data;
    setToken(access_token);
    setRole(userRole);
    setUser({ id: user_id, email: data.email });
    localStorage.setItem('token', access_token);
    localStorage.setItem('role', userRole);
    localStorage.setItem('userId', user_id);
  };

  const logout = () => {
    setToken(null);
    setRole(null);
    setUser(null);
    localStorage.removeItem('token');
    localStorage.removeItem('role');
    localStorage.removeItem('userId');
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        role,
        login,
        register,
        logout,
        isAuthenticated: !!token,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};
