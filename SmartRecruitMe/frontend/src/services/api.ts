import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export const authAPI = {
  register: (data: any) => api.post('/api/auth/register', data),
  login: (data: any) => api.post('/api/auth/login', data),
};

export const candidateAPI = {
  uploadCV: (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    return api.post('/api/candidates/upload-cv', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
  getProfile: () => api.get('/api/candidates/profile'),
  getMatchingJobs: () => api.get('/api/candidates/matching-jobs'),
  analyzeGitHub: () => api.post('/api/candidates/analyze-github'),
  chatCandidate: (data: { message: string }) => api.post('/api/chat/candidate', data),
  getNotifications: () => api.get('/api/notifications/candidate'),
  markNotificationsRead: (ids: number[]) => api.post('/api/notifications/mark-read', ids),
};

export const recruiterAPI = {
  createJobOffer: (data: any) => api.post('/api/recruiters/job-offers', data),
  getJobOffers: () => api.get('/api/recruiters/job-offers'),
  getCandidatesForJob: (jobId: number) => api.get(`/api/recruiters/job-offers/${jobId}/candidates`),
  matchCandidates: (jobId: number) => api.post(`/api/recruiters/job-offers/${jobId}/match-candidates`),
  getCandidateDetail: (candidateId: number) => api.get(`/api/recruiters/candidates/${candidateId}`),
  getDashboardStats: () => api.get('/api/recruiters/dashboard/stats'),
  getDashboardAnalytics: () => api.get('/api/recruiters/dashboard/analytics'),
  chatRecruiter: (data: { message: string }) => api.post('/api/chat/recruiter', data),
  getNotifications: () => api.get('/api/notifications/recruiter'),
  markNotificationsRead: (ids: number[]) => api.post('/api/notifications/mark-read', ids),
};

export default api;