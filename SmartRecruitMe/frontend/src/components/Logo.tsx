import React from 'react';

interface LogoProps {
  size?: number;
  showText?: boolean;
  className?: string;
}

const Logo: React.FC<LogoProps> = ({ size = 64, showText = true, className = '' }) => {
  return (
    <div className={`flex items-center gap-3 ${className}`}>
      <svg width={size} height={size} viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="32" cy="32" r="30" stroke="#1a6ef5" strokeWidth="2.5" strokeDasharray="6 3" opacity="0.25"/>
        <circle cx="32" cy="32" r="26" fill="url(#grad1)"/>
        <circle cx="32" cy="24" r="7" fill="white" opacity="0.95"/>
        <path d="M18 46 C18 38 24 34 32 34 C40 34 46 38 46 46" fill="white" opacity="0.95"/>
        <circle cx="46" cy="18" r="9" fill="#0d1b2a"/>
        <circle cx="46" cy="18" r="7.5" fill="#00c853"/>
        <path d="M42 18 L45 21 L50 15" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        <circle cx="17" cy="32" r="3" fill="#1a6ef5" opacity="0.5"/>
        <circle cx="47" cy="32" r="3" fill="#1a6ef5" opacity="0.5"/>
        <line x1="20" y1="32" x2="26" y2="32" stroke="#1a6ef5" strokeWidth="1.5" opacity="0.3"/>
        <line x1="38" y1="32" x2="44" y2="32" stroke="#1a6ef5" strokeWidth="1.5" opacity="0.3"/>
        <defs>
          <linearGradient id="grad1" x1="0" y1="0" x2="64" y2="64" gradientUnits="userSpaceOnUse">
            <stop offset="0%" stopColor="#1a6ef5"/>
            <stop offset="100%" stopColor="#0a4bc4"/>
          </linearGradient>
        </defs>
      </svg>
      {showText && (
        <div className="flex flex-col">
          <div className="text-2xl font-bold leading-none">
            <span className="text-gray-900">Smart</span>
            <span className="text-primary-600">Recruit</span>
            <span className="text-gray-900">Me</span>
          </div>
          <div className="text-[9px] uppercase tracking-widest text-gray-500 font-medium mt-0.5">
            Au-delà du CV
          </div>
        </div>
      )}
    </div>
  );
};

export default Logo;
