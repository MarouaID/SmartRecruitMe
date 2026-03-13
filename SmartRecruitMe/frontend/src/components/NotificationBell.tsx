import React, { useEffect, useState } from 'react';
import { Bell, Check, X } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { candidateAPI, recruiterAPI } from '../services/api';
import toast from 'react-hot-toast';

type Notification = {
  id: number;
  message: string;
  is_read: boolean;
  created_at: string;
};

const NotificationBell: React.FC = () => {
  const { role } = useAuth();
  const [open, setOpen] = useState(false);
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchNotifications = async () => {
    if (!role) return;
    setLoading(true);
    try {
      const res = role === 'recruiter'
        ? await recruiterAPI.getNotifications()
        : await candidateAPI.getNotifications();
      setNotifications(res.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const markAllRead = async () => {
    if (!role) return;
    const unread = notifications.filter((n) => !n.is_read).map((n) => n.id);
    if (!unread.length) return;
    try {
      role === 'recruiter'
        ? await recruiterAPI.markNotificationsRead(unread)
        : await candidateAPI.markNotificationsRead(unread);
      setNotifications((prev) => prev.map((n) => ({ ...n, is_read: true })));
    } catch (error) {
      toast.error('Impossible de marquer les notifications comme lues');
    }
  };

  useEffect(() => {
    fetchNotifications();
    const interval = setInterval(fetchNotifications, 15000);
    return () => clearInterval(interval);
  }, [role]);

  if (!role) return null;

  const unreadCount = notifications.filter((n) => !n.is_read).length;

  return (
    <div className="relative">
      <button
        onClick={() => { setOpen((o) => !o); if (!open) markAllRead(); }}
        className="relative p-2 rounded-full hover:bg-gray-100 transition"
        aria-label="Notifications"
      >
        <Bell className="w-5 h-5 text-gray-700" />
        {unreadCount > 0 && (
          <span className="absolute -top-1 -right-1 bg-red-600 text-white text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center">
            {unreadCount > 9 ? '9+' : unreadCount}
          </span>
        )}
      </button>
      {open && (
        <div className="absolute right-0 mt-2 w-80 bg-white border border-gray-200 rounded-2xl shadow-xl z-50">
          <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100">
            <span className="font-semibold text-gray-900">
              Notifications {unreadCount > 0 && (
                <span className="text-xs text-primary-600 font-normal ml-1">({unreadCount} non lues)</span>
              )}
            </span>
            <button onClick={() => setOpen(false)} className="text-gray-500 hover:text-gray-700">
              <X className="w-4 h-4" />
            </button>
          </div>
          <div className="max-h-64 overflow-y-auto">
            {loading ? (
              <div className="p-4 text-sm text-gray-500">Chargement...</div>
            ) : notifications.length === 0 ? (
              <div className="p-4 text-sm text-gray-500 text-center">Aucune notification 🔔</div>
            ) : (
              notifications.map((notif) => (
                <div key={notif.id} className={`px-4 py-3 border-b border-gray-100 text-sm ${notif.is_read ? 'bg-white' : 'bg-primary-50'}`}>
                  <div className="flex items-start justify-between gap-2">
                    <p className="text-gray-700">{notif.message}</p>
                    {!notif.is_read && <Check className="w-4 h-4 text-green-600 shrink-0" />}
                  </div>
                  <p className="text-xs text-gray-400 mt-1">{new Date(notif.created_at).toLocaleString('fr-FR')}</p>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default NotificationBell;