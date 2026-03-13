import React, { useEffect, useState } from 'react';
import { MessageCircle, Send, X, MessageSquare } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { candidateAPI, recruiterAPI } from '../services/api';
import toast from 'react-hot-toast';

type Message = {
  id: string;
  from: 'user' | 'bot';
  text: string;
};

const ChatbotWidget: React.FC = () => {
  const { role } = useAuth();
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [sending, setSending] = useState(false);

  useEffect(() => {
    if (!open || !role) return;
    if (messages.length === 0) {
      setMessages([{
        id: 'welcome',
        from: 'bot',
        text: role === 'recruiter'
          ? 'Bonjour ! Je suis votre assistant recruteur. Posez-moi une question comme "Montre-moi les meilleurs candidats".'
          : 'Bonjour ! Je suis votre assistant. Posez-moi une question comme "Comment améliorer mon score ?".',
      }]);
    }
  }, [open, role, messages.length]);

  if (!role) return null;

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { id: `u-${Date.now()}`, from: 'user' as const, text: input.trim() };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setSending(true);
    try {
      const res = role === 'recruiter'
        ? await recruiterAPI.chatRecruiter({ message: userMessage.text })
        : await candidateAPI.chatCandidate({ message: userMessage.text });
      setMessages((prev) => [
        ...prev,
        { id: `b-${Date.now()}`, from: 'bot', text: res.data.reply },
      ]);
    } catch (error) {
      toast.error('Impossible de contacter le chatbot pour le moment.');
    } finally {
      setSending(false);
    }
  };

  return (
    <div className="fixed bottom-6 right-6 z-50">
      {open && (
        <div className="w-80 md:w-96 bg-white shadow-2xl rounded-2xl overflow-hidden border border-gray-200 flex flex-col mb-4">
          <div className="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-primary-600 to-secondary-600 text-white">
            <div className="flex items-center gap-2">
              <MessageSquare className="w-5 h-5" />
              <span className="font-semibold">Assistant IA</span>
            </div>
            <button onClick={() => setOpen(false)} className="rounded-full p-1 hover:bg-white/20">
              <X className="w-5 h-5" />
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-4 space-y-3" style={{ maxHeight: '340px' }}>
            {messages.map((msg) => (
              <div key={msg.id} className={`flex ${msg.from === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-sm ${
                  msg.from === 'user' ? 'bg-primary-600 text-white' : 'bg-gray-100 text-gray-800'
                }`}>
                  {msg.text}
                </div>
              </div>
            ))}
            {sending && (
              <div className="flex justify-start">
                <div className="bg-gray-100 rounded-2xl px-4 py-3 text-sm text-gray-500 italic">
                  En train d'écrire...
                </div>
              </div>
            )}
          </div>
          <div className="border-t border-gray-200 p-3">
            <div className="flex items-center gap-2">
              <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } }}
                placeholder="Posez une question..."
                className="flex-1 px-3 py-2 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <button onClick={sendMessage} disabled={sending || !input.trim()}
                className="bg-primary-600 hover:bg-primary-700 text-white rounded-xl p-2 disabled:opacity-50 transition">
                <Send className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      )}
      <button onClick={() => setOpen((o) => !o)}
        className="w-14 h-14 rounded-full bg-gradient-to-br from-primary-600 to-secondary-600 text-white shadow-xl flex items-center justify-center hover:shadow-2xl transition"
        aria-label="Ouvrir le chat">
        <MessageCircle className="w-6 h-6" />
      </button>
    </div>
  );
};

export default ChatbotWidget;