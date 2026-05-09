import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="Chat with Biswajith",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

/* Custom Premium Loading Screen */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(ellipse at center, rgba(191,148,79,0.15) 0%, transparent 50%),
        linear-gradient(160deg, #0d0f14 0%, #0a0b0f 100%);
    z-index: 99999;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: hideLoader 0.4s ease-out 2.5s forwards;
    pointer-events: none;
}

/* Animated Logo/Icon */
.stApp::after {
    content: '';
    position: fixed;
    top: 45%;
    left: 50%;
    width: 120px;
    height: 120px;
    transform: translate(-50%, -50%);
    z-index: 100001;
    animation: 
        fadeInScale 1.2s ease-out forwards,
        hideLoader 0.4s ease-out 2.5s forwards;
    pointer-events: none;
    background: radial-gradient(circle at 30% 30%, rgba(100, 200, 255, 0.8), rgba(0, 150, 255, 0.4));
    border-radius: 50%;
    filter: blur(25px);
    box-shadow: 0 0 60px rgba(0, 102, 255, 0.6);
}

/* Brand Name */
html::after {
    content: none !important;
}

/* Spinning Ring */
body::before {
    content: '';
    position: fixed;
    top: 45%;
    left: 50%;
    width: 80px;
    height: 80px;
    margin: -40px 0 0 -40px;
    border: 3px solid transparent;
    border-top-color: #d5af67;
    border-right-color: #d5af67;
    border-radius: 50%;
    z-index: 100000;
    animation: 
        spin 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite,
        hideLoader 0.4s ease-out 2.5s forwards;
    pointer-events: none;
    box-shadow: 
        0 0 20px rgba(191,148,79,0.4),
        inset 0 0 20px rgba(191,148,79,0.2);
}

/* Tagline */
nav::before {
    content: none !important;
}

/* Loading Text */
body::after {
    content: none !important;
}

@keyframes textPulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

/* Progress Bar */
html::before {
    content: '';
    position: fixed;
    bottom: 0;
    left: 0;
    width: 0%;
    height: 3px;
    background: linear-gradient(90deg, #d5af67, #f4dd9f);
    z-index: 100002;
    animation: 
        progressBar 2.5s cubic-bezier(0.4, 0, 0.2, 1) forwards,
        hideLoader 0.4s ease-out 2.5s forwards;
    box-shadow: 0 0 10px rgba(191,148,79,0.6);
}

@keyframes progressBar {
    0% { width: 0%; }
    100% { width: 100%; }
}

/* Floating particles effect */
@keyframes float {
    0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.3; }
    50% { transform: translateY(-20px) translateX(10px); opacity: 0.6; }
}

/* Mobile optimizations for loading screen */
@media (max-width: 768px) {
    .stApp::after {
        font-size: 2.5rem !important;
        top: 40% !important;
    }
    
    html::after {
        font-size: 1.3rem !important;
        top: 48% !important;
    }
    
    nav::before {
        font-size: 0.65rem !important;
        top: 53% !important;
    }
    
    body::after {
        font-size: 0.7rem !important;
        top: 60% !important;
    }
    
    body::before {
        width: 60px !important;
        height: 60px !important;
        margin: -30px 0 0 -30px !important;
        border-width: 2.5px !important;
        top: 40% !important;
    }
    
    html::before {
        height: 2px !important;
    }
    
    .stApp > div:first-child::before,
    .stApp > div:first-child::after {
        display: none !important;
    }
}

.stApp > div:first-child::before {
    content: '✨';
    position: absolute;
    top: 30%;
    left: 20%;
    font-size: 1.5rem;
    opacity: 0;
    animation: float 3s ease-in-out infinite, hideLoader 0.4s ease-out 2.5s forwards;
    z-index: 100000;
}

.stApp > div:first-child::after {
    content: '💫';
    position: absolute;
    top: 40%;
    right: 25%;
    font-size: 1.2rem;
    opacity: 0;
    animation: float 3s ease-in-out 0.5s infinite, hideLoader 0.4s ease-out 2.5s forwards;
    z-index: 100000;
}

@keyframes logoFloat {
    0%, 100% { transform: translate(-50%, -50%) translateY(0px); }
    50% { transform: translate(-50%, -50%) translateY(-10px); }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes hideLoader {
    to {
        opacity: 0;
        visibility: hidden;
    }
}

/* Hide Streamlit default skeleton */
[data-testid="stAppViewContainer"] > div:first-child > div:first-child {
    background: transparent !important;
}

div[data-testid="stVerticalBlock"] > div:empty,
div[class*="skeleton"],
.element-container:empty {
    display: none !important;
    opacity: 0 !important;
}

html, body { background: #02050c !important; }

body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stHeader"],
section.main, .main > div, .block-container, [class^="css"], [class*=" css"] {
    background: #02050c !important;
    color: #e8eaf0 !important;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stApp {
    background: radial-gradient(circle at top left, rgba(50, 115, 255, 0.08), transparent 18%),
                radial-gradient(circle at 80% 20%, rgba(0, 180, 255, 0.08), transparent 18%),
                linear-gradient(180deg, #040a14 0%, #04070f 100%) !important;
    min-height: 100vh;
    background-image: linear-gradient(rgba(100,150,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(100,150,255,0.05) 1px, transparent 1px), radial-gradient(circle at 20% 20%, rgba(100,150,255,0.06), transparent 5%), radial-gradient(circle at 80% 10%, rgba(100,150,255,0.06), transparent 4%);
    background-size: 80px 80px, 80px 80px, 320px 320px, 260px 260px;
    background-blend-mode: screen, screen, normal, normal;
}

[data-testid="stHeader"], footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {
    display: none !important;
}

/* Smooth animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
    from { transform: translateX(-100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

@keyframes slideInRight {
    from { transform: translateX(50px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.8; transform: scale(1.05); }
}

@keyframes shimmer {
    0% { background-position: -1000px 0; }
    100% { background-position: 1000px 0; }
}

@keyframes shimmer {
    0% { background-position: -1000px 0; }
    100% { background-position: 1000px 0; }
}

/* Loading skeleton effect */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, 
        transparent 0%, 
        rgba(191,148,79,0.05) 50%, 
        transparent 100%);
    background-size: 1000px 100%;
    animation: shimmer 2s infinite;
    pointer-events: none;
    z-index: -1;
    opacity: 0.3;
}

/* Apply animations with delay to sync with loading */
.stApp {
    animation: fadeInScale 0.8s cubic-bezier(0.16, 1, 0.3, 1) 2.9s backwards;
}

@keyframes fadeInScale {
    from { 
        opacity: 0; 
        transform: scale(0.95);
    }
    to { 
        opacity: 1; 
        transform: scale(1);
    }
}

.main, [data-testid="stMain"] {
    animation: slideInRight 0.6s cubic-bezier(0.16, 1, 0.3, 1) 3s backwards;
}

.block-container { max-width: 100% !important; padding: 0.6rem 0.9rem 0.5rem !important; }

/* Force sidebar to always be visible on Render */
[data-testid="stSidebar"] {
    background: rgba(8, 14, 28, 0.92) !important;
    border-right: 1px solid rgba(100, 150, 255, 0.16) !important;
    box-shadow: 0 40px 100px rgba(0,0,0,0.35) !important;
    backdrop-filter: blur(18px) !important;
    display: block !important;
    visibility: visible !important;
    width: 320px !important;
    min-width: 320px !important;
    max-width: 320px !important;
    position: relative !important;
    opacity: 1 !important;
    animation: slideInLeft 0.6s cubic-bezier(0.16, 1, 0.3, 1) 2.9s backwards;
}
[data-testid="stSidebar"] * { color: #e8eaf0 !important; }
[data-testid="stSidebar"] > div:first-child { padding: 1.2rem 0.9rem !important; }

/* Hide sidebar close button to keep sidebar visible */
[data-testid="stSidebarNav"] button,
.stSidebarNav button,
[aria-label="Close sidebar"],
[data-testid="stSidebarNav"] [aria-label*="Close"],
[data-testid="stSidebarNav"] [aria-label*="collapse"] {
    display: none !important;
}

/* Force sidebar content to be visible */
[data-testid="stSidebar"] > div {
    display: block !important;
    visibility: visible !important;
}

/* Additional Render-specific sidebar fixes */
.css-1lcbmhc, .css-1d391kg, .css-17eqqhr {
    display: block !important;
    visibility: visible !important;
}

/* More aggressive sidebar targeting */
section[data-testid="stSidebar"],
div[data-testid="stSidebar"],
.stSidebar,
.streamlit-sidebar,
.sidebar {
    display: block !important;
    visibility: visible !important;
    width: 320px !important;
    min-width: 320px !important;
    max-width: 320px !important;
    position: relative !important;
    opacity: 1 !important;
}

/* Emergency sidebar fix - force visibility */
[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    width: 320px !important;
    min-width: 320px !important;
    max-width: 320px !important;
    position: fixed !important;
    left: 0 !important;
    top: 0 !important;
    height: 100vh !important;
    z-index: 9999 !important;
    background: rgba(8, 14, 28, 0.92) !important;
    border-right: 1px solid rgba(100, 150, 255, 0.16) !important;
    box-shadow: 0 40px 100px rgba(0,0,0,0.35) !important;
    backdrop-filter: blur(18px) !important;
    transform: translateX(0) !important;
    opacity: 1 !important;
}

/* Chrome-specific sidebar fixes */
@media screen and (-webkit-min-device-pixel-ratio:0) and (min-resolution:.001dpcm) {
    [data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
        width: 320px !important;
        min-width: 320px !important;
        max-width: 320px !important;
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        height: 100vh !important;
        z-index: 9999 !important;
        background: #0d0f14 !important;
        border-right: 1px solid rgba(255,255,255,0.07) !important;
        transform: translateX(0) !important;
        opacity: 1 !important;
        -webkit-transform: translateX(0) !important;
        -webkit-opacity: 1 !important;
    }
}

/* Firefox fallback */
@-moz-document url-prefix() {
    [data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
        width: 320px !important;
        min-width: 320px !important;
        max-width: 320px !important;
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        height: 100vh !important;
        z-index: 9999 !important;
        background: #0d0f14 !important;
        border-right: 1px solid rgba(255,255,255,0.07) !important;
        transform: translateX(0) !important;
        opacity: 1 !important;
    }
}

/* Adjust main content to account for fixed sidebar */
.main,
[data-testid="stMain"] {
    margin-left: 320px !important;
    width: calc(100% - 320px) !important;
}

/* Hide any collapse buttons */
button[aria-label*="sidebar"],
button[aria-label*="collapse"],
.stSidebar button {
    display: none !important;
}

.avatar {
    width: 90px; height: 90px;
    border-radius: 24px;
    background: rgba(12, 20, 40, 0.78);
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 1rem;
    box-shadow: 0 24px 60px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.08);
    position: relative;
    border: 1px solid rgba(100, 150, 255, 0.18);
    overflow: hidden;
}

.avatar::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top left, rgba(100,200,255,0.18), transparent 42%);
    border-radius: inherit;
    pointer-events: none;
}

.avatar-badge {
    width: 70px; height: 70px;
    display: flex; align-items: center; justify-content: center;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(0,120,255,0.94), rgba(0,80,210,0.95));
    color: #ffffff;
    font-size: 2.5rem;
    font-weight: 900;
    letter-spacing: -0.06rem;
    box-shadow: 0 18px 34px rgba(0,100,255,0.35);
}

.avatar:hover {
    transform: translateY(-3px);
    box-shadow: 0 28px 70px rgba(0,0,0,0.42), inset 0 1px 0 rgba(255,255,255,0.08);
}

.profile-name {
    font-size: 1.25rem;
    font-weight: 900;
    color: #ffffff !important;
    text-align: center;
    margin-bottom: 0.3rem;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
    letter-spacing: -0.015em;
    background: linear-gradient(135deg, #ffffff, #64c8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.profile-role {
    font-size: 0.75rem;
    color: #7fa8d1 !important;
    text-align: center;
    margin-bottom: 1rem;
    font-weight: 700;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}

.profile-bio {
    font-size: 0.85rem;
    color: #b8cde8 !important;
    text-align: center;
    line-height: 1.7;
    font-weight: 500;
    letter-spacing: 0.2px;
}

.section-label {
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.15em;
    color: #64c8ff !important;
    text-transform: uppercase;
    margin: 1.2rem 0 0.7rem;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.info-card {
    background: rgba(100, 150, 200, 0.06);
    border: 1px solid rgba(100, 150, 200, 0.12);
    border-radius: 12px;
    padding: 0.75rem 0.9rem;
    margin-bottom: 0.55rem;
    font-size: 0.82rem;
    color: #c5d8f0 !important;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.320, 1);
    animation: fadeIn 0.5s ease-out backwards;
    font-weight: 500;
    letter-spacing: 0.2px;
}

.info-card:hover {
    background: rgba(100, 200, 255, 0.12);
    border-color: rgba(100, 200, 255, 0.25);
    transform: translateX(4px);
    box-shadow: 0 6px 16px rgba(0, 102, 200, 0.15);
}

.info-card:nth-child(1) { animation-delay: 0.1s; }
.info-card:nth-child(2) { animation-delay: 0.2s; }
.info-card:nth-child(3) { animation-delay: 0.3s; }
.info-card:nth-child(4) { animation-delay: 0.4s; }
.info-card:nth-child(5) { animation-delay: 0.5s; }

.info-card strong { color: #edf2f7 !important; }

.tags-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-top: 0.1rem;
}

.tag {
    display: inline-block;
    background: rgba(100, 150, 200, 0.1);
    border: 1px solid rgba(100, 150, 200, 0.2);
    border-radius: 999px;
    padding: 0.35rem 0.75rem;
    font-size: 0.75rem;
    color: #7fa8d1 !important;
    font-weight: 500;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stButton > button {
    background: rgba(100, 150, 200, 0.12) !important;
    border: 1px solid rgba(100, 150, 200, 0.2) !important;
    color: #c5d8f0 !important;
    border-radius: 10px !important;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: 0.82rem !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.320, 1) !important;
    width: 100%;
    font-weight: 500 !important;
}

.stButton > button:hover {
    background: rgba(0, 150, 255, 0.18) !important;
    border-color: rgba(0, 150, 255, 0.3) !important;
    color: #64c8ff !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 102, 200, 0.2) !important;
}

.header-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 0 0.6rem;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    gap: 0.5rem;
    flex-wrap: wrap;
}

.header-left { min-width: 0; flex: 1; }

.header-title {
    font-size: clamp(1.6rem, 4vw, 2.6rem);
    font-weight: 900;
    color: #ffffff !important;
    letter-spacing: -0.025em;
    margin: 0;
    line-height: 1.15;
    word-break: break-word;
    background: linear-gradient(135deg, #ffffff, #64c8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.header-sub {
    font-size: clamp(0.82rem, 2.2vw, 0.97rem);
    color: #8fa5c2 !important;
    margin-top: 0.45rem;
    font-weight: 500;
    letter-spacing: 0.3px;
}

.online-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    background: rgba(0, 150, 255, 0.12);
    border: 1px solid rgba(0, 150, 255, 0.3);
    color: #64c8ff !important;
    font-size: 0.75rem;
    white-space: nowrap;
    flex-shrink: 0;
    font-weight: 500;
}

.online-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00d4ff;
    display: inline-block;
    animation: pulse 2s ease-in-out infinite;
    box-shadow: 0 0 12px rgba(0, 212, 255, 0.6);
}

.chips-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    padding: 0.55rem 0 0.1rem;
    overflow: hidden;
}

.chip {
    padding: 0.5rem 1.1rem;
    border-radius: 20px;
    background: rgba(100, 150, 200, 0.08);
    border: 1px solid rgba(100, 150, 200, 0.2);
    color: #c5d8f0 !important;
    font-size: 0.82rem;
    white-space: nowrap;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.320, 1);
    animation: fadeIn 0.6s ease-out backwards;
    font-weight: 500;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.chip:hover {
    background: rgba(100, 200, 255, 0.15);
    border-color: rgba(100, 200, 255, 0.4);
    color: #64c8ff !important;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 102, 200, 0.2);
}

.chip:nth-child(1) { animation-delay: 0.1s; }
.chip:nth-child(2) { animation-delay: 0.2s; }
.chip:nth-child(3) { animation-delay: 0.3s; }
.chip:nth-child(4) { animation-delay: 0.4s; }
.chip:nth-child(5) { animation-delay: 0.5s; }

.chat-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 0 0.3rem;
    overflow: hidden;
}

.chat-meta-name {
    font-size: 0.85rem;
    font-weight: 600;
    color: #d5dce6 !important;
    white-space: nowrap;
}

[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    margin-bottom: 1.2rem !important;
    animation: fadeIn 0.5s ease-out;
}

[data-testid="chatAvatarIcon-assistant"] {
    background: linear-gradient(135deg, #0066ff, #0099ff) !important;
    color: #fff !important;
    border-radius: 12px !important;
    box-shadow: 0 6px 20px rgba(0, 102, 255, 0.3) !important;
    border: 1px solid rgba(0, 150, 255, 0.2) !important;
}

[data-testid="chatAvatarIcon-user"] {
    background: rgba(100, 150, 200, 0.15) !important;
    color: #64c8ff !important;
    border-radius: 12px !important;
    border: 1px solid rgba(100, 150, 200, 0.2) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
}

[data-testid="stChatMessageContent"], [data-testid="stChatMessageContent"] p, [data-testid="stChatMessageContent"] * {
    color: #e8eaf0 !important;
}

[data-testid="stChatMessageContent"] {
    background: rgba(20, 30, 50, 0.4) !important;
    border: 1px solid rgba(100, 150, 200, 0.15) !important;
    border-radius: 16px !important;
    padding: 1.2rem 1.4rem !important;
    font-size: 0.96rem !important;
    line-height: 1.85 !important;
    max-width: 100% !important;
    word-break: break-word !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.05) !important;
    backdrop-filter: blur(8px) !important;
    -webkit-backdrop-filter: blur(8px) !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
}

[data-testid="stChatInputContainer"], [data-testid="stChatInput"] {
    margin-top: 0 !important;
    border-top: none !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
}

[data-testid="stChatInputContainer"] > div, [data-testid="stChatInput"] > div,
[data-testid="stChatInputContainer"] form, [data-testid="stChatInput"] form {
    margin: 0 !important;
    padding: 0 !important;
}

[data-testid="stChatInputContainer"] form, [data-testid="stChatInput"] form,
[data-testid="stChatInputContainer"] [data-testid="stChatInputForm"],
[data-testid="stChatInput"] [data-testid="stChatInputForm"] {
    display: flex !important;
    align-items: flex-end !important;
    gap: 0.65rem !important;
    width: 100% !important;
}

[data-testid="stChatInputContainer"] form > div:first-child,
[data-testid="stChatInput"] form > div:first-child,
[data-testid="stChatInputContainer"] [data-testid="stChatInputForm"] > div:first-child,
[data-testid="stChatInput"] [data-testid="stChatInputForm"] > div:first-child {
    flex: 1 1 auto !important;
    min-width: 0 !important;
}

[data-testid="stChatInputContainer"] p, [data-testid="stChatInput"] p {
    margin: 0 !important;
}

[data-testid="stChatInput"] textarea, [data-testid="stChatInputContainer"] textarea,
div[data-testid="stChatInput"] > div > div > textarea, div[data-testid="stChatInput"] div div textarea,
.stChatInput textarea, textarea[aria-label], textarea[placeholder="Ask about Biswajith..."] {
    background: rgba(15, 25, 45, 0.3) !important;
    border: 1.5px solid rgba(100, 150, 200, 0.2) !important;
    color: #f0f2f6 !important;
    -webkit-text-fill-color: #f0f2f6 !important;
    border-radius: 20px !important;
    font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: 0.95rem !important;
    line-height: 1.8 !important;
    min-height: 56px !important;
    padding: 1rem 1.3rem !important;
    caret-color: #64c8ff !important;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.320, 1) !important;
    opacity: 1 !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.05) !important;
    resize: none !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
}

[data-testid="stChatInput"] textarea::placeholder, [data-testid="stChatInputContainer"] textarea::placeholder,
textarea[placeholder="Ask about Biswajith..."]::placeholder {
    color: #6a7d99 !important;
    -webkit-text-fill-color: #6a7d99 !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] textarea:focus, [data-testid="stChatInputContainer"] textarea:focus,
textarea[placeholder="Ask about Biswajith..."]:focus {
    border-color: rgba(0, 150, 255, 0.5) !important;
    box-shadow: 0 0 0 4px rgba(100, 200, 255, 0.12), 0 8px 24px rgba(0,102,255,0.25) !important;
    outline: none !important;
    background: rgba(15, 25, 50, 0.5) !important;
}

[data-testid="stChatInput"] button, [data-testid="stChatInputContainer"] button {
    background: linear-gradient(135deg, #0066ff, #0099ff) !important;
    color: #ffffff !important;
    border-radius: 16px !important;
    border: none !important;
    width: 48px !important;
    height: 48px !important;
    min-width: 48px !important;
    flex: 0 0 48px !important;
    align-self: flex-end !important;
    margin: 0 0 4px 0 !important;
    box-shadow: 0 8px 24px rgba(0, 102, 255, 0.35) !important;
    transition: all 0.2s cubic-bezier(0.23, 1, 0.320, 1) !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

[data-testid="stChatInput"] button:hover, [data-testid="stChatInputContainer"] button:hover {
    opacity: 0.9 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 32px rgba(0, 102, 255, 0.45) !important;
}

[data-testid="stChatInput"] button:active, [data-testid="stChatInputContainer"] button:active {
    transform: scale(0.95) !important;
}

.stSpinner > div { border-top-color: #0066ff !important; }

@media (max-width: 768px) {
    /* Hide sidebar completely on mobile - show only chat */
    [data-testid="stSidebar"],
    [data-testid="stSidebarNav"],
    section[data-testid="stSidebar"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        min-width: 0 !important;
        max-width: 0 !important;
    }
    
    /* Mobile main content adjustments - full width */
    .main,
    [data-testid="stMain"],
    section.main {
        margin-left: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        padding: 0 !important;
    }
    
    .block-container { 
        padding: 0.5rem 0.8rem 0.75rem !important; 
        max-width: 100% !important;
        width: 100% !important;
        box-sizing: border-box !important;
        margin: 0 !important;
    }
    
    .header-bar { padding: 0.5rem 0 0.6rem; }
    .header-title { font-size: 1.5rem !important; }
    .header-sub { font-size: 0.8rem !important; }
    
    [data-testid="stChatMessageContent"] { 
        padding: 0.7rem 0.85rem !important; 
        border-radius: 14px !important; 
        font-size: 0.9rem !important;
    }
    
    .chips-row { gap: 0.3rem; padding: 0.5rem 0; }
    .chip { padding: 0.35rem 0.65rem; font-size: 0.7rem; }
    .online-badge { font-size: 0.7rem; padding: 0.3rem 0.6rem; }
    
    [data-testid="stChatInput"] textarea, [data-testid="stChatInputContainer"] textarea,
    div[data-testid="stChatInput"] > div > div > textarea, div[data-testid="stChatInput"] div div textarea,
    .stChatInput textarea, textarea[aria-label], textarea[placeholder="Ask about Biswajith..."] {
        font-size: 16px !important;
        min-height: 60px !important;
        padding: 1rem 1.1rem !important;
        border-radius: 20px !important;
    }
    
    [data-testid="stChatInput"] button, [data-testid="stChatInputContainer"] button {
        width: 48px !important;
        height: 48px !important;
        min-width: 48px !important;
        flex: 0 0 48px !important;
        margin: 0 0 6px 0 !important;
    }
    
    /* Extra small mobile devices */
    @media (max-width: 480px) {
        [data-testid="stSidebar"] {
            width: 250px !important;
            min-width: 250px !important;
            max-width: 250px !important;
        }
        
        .main,
        [data-testid="stMain"] {
            margin-left: 250px !important;
            width: calc(100% - 250px) !important;
        }
    }
    
    /* Ultra small mobile devices */
    @media (max-width: 400px) {
        [data-testid="stSidebar"] {
            width: 240px !important;
            min-width: 240px !important;
            max-width: 240px !important;
        }
        
        .main,
        [data-testid="stMain"] {
            margin-left: 240px !important;
            width: calc(100% - 240px) !important;
        }
    }
}
</style>

<script>
// Cross-browser sidebar fix for Render
document.addEventListener('DOMContentLoaded', function() {
    const isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
    const isFirefox = /Firefox/.test(navigator.userAgent);
    
    const crossBrowserFix = () => {
        // Force sidebar with browser-specific fixes
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            // Responsive sidebar width based on screen size
            let sidebarWidth = '320px';
            if (window.innerWidth <= 400) {
                sidebarWidth = '240px';
            } else if (window.innerWidth <= 480) {
                sidebarWidth = '250px';
            } else if (window.innerWidth <= 640) {
                sidebarWidth = '280px';
            }
            
            // Base styles for all browsers
            sidebar.style.position = 'fixed !important';
            sidebar.style.left = '0 !important';
            sidebar.style.top = '0 !important';
            sidebar.style.width = sidebarWidth + ' !important';
            sidebar.style.height = '100vh !important';
            sidebar.style.zIndex = '9999 !important';
            sidebar.style.display = 'block !important';
            sidebar.style.visibility = 'visible !important';
            sidebar.style.background = '#0d0f14 !important';
            sidebar.style.borderRight = '1px solid rgba(255,255,255,0.07) !important';
            sidebar.style.transform = 'translateX(0) !important';
            sidebar.style.opacity = '1 !important';
            sidebar.style.overflowY = 'auto !important';
            sidebar.style.overflowX = 'hidden !important';
            
            // Chrome-specific fixes
            if (isChrome) {
                sidebar.style.setProperty('display', 'block', 'important');
                sidebar.style.setProperty('visibility', 'visible', 'important');
                sidebar.style.setProperty('position', 'fixed', 'important');
                sidebar.style.setProperty('left', '0', 'important');
                sidebar.style.setProperty('top', '0', 'important');
                sidebar.style.setProperty('width', sidebarWidth, 'important');
                sidebar.style.setProperty('height', '100vh', 'important');
                sidebar.style.setProperty('z-index', '9999', 'important');
                sidebar.style.setProperty('background', '#0d0f14', 'important');
                sidebar.style.setProperty('transform', 'translateX(0)', 'important');
                sidebar.style.setProperty('opacity', '1', 'important');
                sidebar.style.setProperty('-webkit-transform', 'translateX(0)', 'important');
                sidebar.style.setProperty('-webkit-opacity', '1', 'important');
                sidebar.style.setProperty('overflow-y', 'auto', 'important');
                sidebar.style.setProperty('overflow-x', 'hidden', 'important');
            }
            
            // Firefox-specific fixes
            if (isFirefox) {
                sidebar.style.setProperty('display', 'block', 'important');
                sidebar.style.setProperty('visibility', 'visible', 'important');
                sidebar.style.setProperty('position', 'fixed', 'important');
            }
        }
        
        // Adjust main content for fixed sidebar
        const mainContent = document.querySelector('[data-testid="stMain"]');
        if (mainContent) {
            // Responsive margin based on sidebar width
            const mainMargin = sidebarWidth;
            const mainWidth = `calc(100% - ${sidebarWidth})`;
            
            mainContent.style.marginLeft = mainMargin + ' !important';
            mainContent.style.width = mainWidth + ' !important';
            
            if (isChrome) {
                mainContent.style.setProperty('margin-left', mainMargin, 'important');
                mainContent.style.setProperty('width', mainWidth, 'important');
            }
        }
        
        // Force all sidebar elements visible with browser-specific methods
        const allSidebarElements = document.querySelectorAll('[data-testid="stSidebar"], .css-1lcbmhc, .css-1d391kg, .css-17eqqhr');
        allSidebarElements.forEach(el => {
            el.style.display = 'block !important';
            el.style.visibility = 'visible !important';
            
            if (isChrome) {
                el.style.setProperty('display', 'block', 'important');
                el.style.setProperty('visibility', 'visible', 'important');
            }
        });
    };
    
    // Run aggressively with more frequent checks for Chrome
    crossBrowserFix();
    setTimeout(crossBrowserFix, 10);
    setTimeout(crossBrowserFix, 50);
    setTimeout(crossBrowserFix, 100);
    setTimeout(crossBrowserFix, 200);
    setTimeout(crossBrowserFix, 500);
    setTimeout(crossBrowserFix, 1000);
    setTimeout(crossBrowserFix, 2000);
    
    // Additional checks for Chrome
    if (isChrome) {
        setInterval(crossBrowserFix, 3000);
    }
});
</script>
""", unsafe_allow_html=True)

KNOWLEDGE_BASE = """
You are a chatbot that represents Biswajith PN. Answer questions naturally as if you are him or know him deeply.
Use only the confirmed facts below. If something is not in the knowledge base, say I don't have that detail yet.

CONFIRMED FACTS ABOUT BISWAJITH PN:

IDENTITY:
- Full Name: Biswajith PN
- Location: Sivakasi, Tamil Nadu, India
- Phone: 81100 61566
- Email: pnbiswajith@gmail.com
- LinkedIn: linkedin.com/in/biswajithpn
- GitHub: github.com/BiswajithPN
- Instagram edits page: @ig._.obito._.edits

EDUCATION:
- Engineering student specializing in Artificial Intelligence and Data Science
- College: Mepco Schlenk Engineering College

TECHNICAL INTERESTS:
- Artificial Intelligence, Data Science, Software Development
- Chatbot Development, RAG Systems, App Development, Web Development
- LangChain, Streamlit, PDF-based knowledge retrieval, Python

PROJECTS:
1. Life Tracker App - Futuristic mobile app for expense tracking, budget control, habit and productivity tracking
2. PDF RAG Chatbot - AI chatbot using LangChain and Streamlit for answering from uploaded PDFs
3. Prabhu Swathi Wedding Website - A refined digital invitation website with modern elegant design
4. BISWAJITH CONNECT - Professional private messaging app with invite-only friendship system
5. Resume and Internship Prep - Actively applying for software/IT internships
6. Forex Basics PPT - Learning and presenting Forex trading basics
7. MSEC E-SPORTS Poster - Designed a Free Fire esports poster

SKILLS:
- Video Editing, Chatbot building, App development, Content creation, Practical learning
- Python, Java, Streamlit, Flutter

CAREER GOALS:
- Seeking software/IT internship
- Career direction: AI, Data Science, Software Development, App development, Web development

PERSONALITY:
- Prefers practical outputs over theory
- Hands-on project-based learner
- Curious about AI tools, tech, and Trading
- Enjoys creative work like video editing and design

RULES:
- First respond to the user's latest message directly
- If user says only a short greeting, reply with a short greeting and one follow-up question
- Do not randomly introduce biography unless asked
- Speak naturally and personally
- Only state confirmed facts
- Be friendly, direct, and practical
- Keep answers concise
"""

with st.sidebar:
    st.markdown('<div class="avatar"><div class="avatar-badge">B</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-name">Biswajith PN</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-role">AI & Data Science Student</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-bio">Practical builder focused on AI products and applied software work.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Quick Facts</div>', unsafe_allow_html=True)
    facts = [
        ("📍", "Location", "Sivakasi, Tamil Nadu"),
        ("🎓", "Degree", "AI & Data Science Engg."),
        ("✂️", "Skill", "Video Editing"),
        ("🌐", "GitHub", "github.com/BiswajithPN"),
        ("📧", "Email", "pnbiswajith@gmail.com"),
    ]
    for icon, label, val in facts:
        st.markdown(f'<div class="info-card"><strong>{icon} {label}</strong><br><span>{val}</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Core Skills</div>', unsafe_allow_html=True)
    skills = [
        ("Python", 92),
        ("Streamlit", 88),
        ("Chatbot Dev", 90),
        ("App Development", 82),
        ("Video Editing", 86),
        ("Web Development", 80),
    ]
    for skill_name, level in skills:
        st.markdown(f'<div style="margin-bottom: 0.6rem;"><div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;"><span style="font-size: 0.78rem; font-weight: 600; color: #f3f4f6;">{skill_name}</span><span style="font-size: 0.72rem; color: #d9bb78;">{level}%</span></div><div style="height: 6px; border-radius: 999px; background: rgba(255,255,255,0.08); overflow: hidden;"><div style="height: 100%; width: {level}%; background: linear-gradient(90deg, #d5af67, #f4dd9f); border-radius: inherit; box-shadow: 0 0 12px rgba(213,175,103,0.2);"></div></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Interests</div>', unsafe_allow_html=True)
    tags = ["AI/ML", "RAG", "LangChain", "Streamlit", "App Dev", "Video Editing", "Chatbots", "Trading", "Web Dev"]
    st.markdown('<div class="tags-wrap">' + "".join(f'<span class="tag">{t}</span>' for t in tags) + '</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Tech Stack</div>', unsafe_allow_html=True)
    tech_stack = [
        ("🐍", "Python", "Primary Language"),
        ("☕", "Java", "Backend Dev"),
        ("📱", "Flutter", "Mobile Apps"),
        ("🎨", "Streamlit", "Web Apps"),
        ("🤖", "LangChain", "AI/LLM"),
        ("🔥", "Firebase", "Backend"),
    ]
    for icon, tech, desc in tech_stack:
        st.markdown(f'<div class="info-card"><strong>{icon} {tech}</strong><br><span>{desc}</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Creative</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">📷 <strong>Edits:</strong> @ig._.obito._.edits<br><span>Video edits & creative content</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Connect</div>', unsafe_allow_html=True)
    connect = [
        ("💼", "LinkedIn", "linkedin.com/in/biswajithpn"),
        ("📱", "Phone", "81100 61566"),
    ]
    for icon, label, val in connect:
        st.markdown(f'<div class="info-card"><strong>{icon} {label}</strong><br><span style="font-size: 0.75rem;">{val}</span></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    with col2:
        if st.button("⭐ About", use_container_width=True):
            st.info("🤖 Biswajith's AI Assistant - Ask me anything about his projects, skills, and career!")

st.markdown("""
<div class="header-bar">
    <div class="header-left">
        <div class="header-title">Chat with Biswajith</div>
        <div class="header-sub">Ask about projects, skills, career goals, or creative work.</div>
    </div>
    <div class="online-badge">
        <span class="online-dot"></span> Online
    </div>
</div>
<div class="chips-row">
    <span class="chip">Projects</span>
    <span class="chip">Skills</span>
    <span class="chip">Career</span>
    <span class="chip">Creative Work</span>
    <span class="chip">Tech Stack</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-meta"><span class="chat-meta-name">🤖 Biswajith AI</span></div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hi! I'm Biswajith's AI. Ask me about his projects, skills, internship goals, or creative work 👋"
    }]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask about Biswajith..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": KNOWLEDGE_BASE},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                    ],
                    max_tokens=1024,
                    temperature=0.25,
                )
                reply = response.choices[0].message.content
                st.write(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error("Something went wrong: " + str(e))