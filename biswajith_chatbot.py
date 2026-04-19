import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="Chat with Biswajith",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body { background: #0a0b0f !important; }

body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stHeader"],
section.main, .main > div, .block-container, [class^="css"], [class*=" css"] {
    background: #0a0b0f !important;
    color: #e8eaf0 !important;
    font-family: 'Inter', sans-serif !important;
}

.stApp {
    background: radial-gradient(ellipse at top left, rgba(191,148,79,0.10) 0%, transparent 40%),
                linear-gradient(160deg, #0d0f14 0%, #0a0b0f 100%) !important;
    min-height: 100vh;
}

[data-testid="stHeader"], footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {
    display: none !important;
}

.block-container { max-width: 100% !important; padding: 0.6rem 0.9rem 0.5rem !important; }

/* Force sidebar to always be visible on Render */
[data-testid="stSidebar"] {
    background: #0d0f14 !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
    display: block !important;
    visibility: visible !important;
    width: 320px !important;
    min-width: 320px !important;
    max-width: 320px !important;
    position: relative !important;
    opacity: 1 !important;
}
[data-testid="stSidebar"] * { color: #e8eaf0 !important; }
[data-testid="stSidebar"] > div:first-child { padding: 1rem 0.8rem !important; }

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
    z-index: 999 !important;
    background: #0d0f14 !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
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
    width: 56px; height: 56px;
    border-radius: 18px;
    background: linear-gradient(135deg, #d5af67, #9a6f2e);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    margin: 0 auto 0.65rem;
    box-shadow: 0 8px 24px rgba(191,148,79,0.25);
}

.profile-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: #f3f4f6 !important;
    text-align: center;
    margin-bottom: 0.15rem;
}

.profile-role {
    font-size: 0.78rem;
    color: #8a98ac !important;
    text-align: center;
    margin-bottom: 0.8rem;
}

.profile-bio {
    font-size: 0.8rem;
    color: #b0bac7 !important;
    text-align: center;
    line-height: 1.5;
}

.section-label {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    color: #d4ac63 !important;
    text-transform: uppercase;
    margin: 1rem 0 0.4rem;
}

.info-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 0.6rem 0.75rem;
    margin-bottom: 0.4rem;
    font-size: 0.78rem;
    color: #c8d0db !important;
}

.info-card strong { color: #edf2f7 !important; }

.tags-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-top: 0.1rem;
}

.tag {
    display: inline-block;
    background: rgba(191,148,79,0.08);
    border: 1px solid rgba(191,148,79,0.2);
    border-radius: 999px;
    padding: 0.28rem 0.6rem;
    font-size: 0.7rem;
    color: #e3c97a !important;
}

.stButton > button {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #d0d5dd !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.18s !important;
    width: 100%;
}

.stButton > button:hover {
    background: rgba(191,148,79,0.1) !important;
    border-color: rgba(191,148,79,0.3) !important;
    color: #f5e6bc !important;
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
    font-size: clamp(1.25rem, 4vw, 2rem);
    font-weight: 700;
    color: #f0f2f5 !important;
    letter-spacing: -0.02em;
    margin: 0;
    line-height: 1.15;
    word-break: break-word;
}

.header-sub {
    font-size: clamp(0.75rem, 2.2vw, 0.88rem);
    color: #7a8799 !important;
    margin-top: 0.25rem;
}

.online-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.25);
    color: #86efac !important;
    font-size: 0.72rem;
    white-space: nowrap;
    flex-shrink: 0;
}

.online-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #22c55e;
    display: inline-block;
}

.chips-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    padding: 0.55rem 0 0.1rem;
    overflow: hidden;
}

.chip {
    padding: 0.38rem 0.75rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    color: #c8d0db !important;
    font-size: clamp(0.68rem, 1.8vw, 0.8rem);
    white-space: nowrap;
    cursor: pointer;
}

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
    margin-bottom: 0.65rem !important;
}

[data-testid="chatAvatarIcon-assistant"] {
    background: linear-gradient(135deg, #d5af67, #9a6f2e) !important;
    color: #111 !important;
    border-radius: 10px !important;
}

[data-testid="chatAvatarIcon-user"] {
    background: rgba(255,255,255,0.08) !important;
    color: #e0e6ef !important;
    border-radius: 10px !important;
}

[data-testid="stChatMessageContent"], [data-testid="stChatMessageContent"] p, [data-testid="stChatMessageContent"] * {
    color: #e8eaf0 !important;
}

[data-testid="stChatMessageContent"] {
    background: #141820 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 16px !important;
    padding: 0.75rem 1rem !important;
    font-size: clamp(0.84rem, 2.4vw, 0.95rem) !important;
    line-height: 1.7 !important;
    max-width: 100% !important;
    word-break: break-word !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
}

[data-testid="stChatInputContainer"], [data-testid="stChatInput"] {
    margin-top: 0 !important;
    border-top: none !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    background: transparent !important;
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
    background: #1a1e2a !important;
    border: 1.5px solid rgba(191,148,79,0.25) !important;
    color: #f0f2f6 !important;
    -webkit-text-fill-color: #f0f2f6 !important;
    border-radius: 18px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: clamp(0.85rem, 2.3vw, 0.95rem) !important;
    line-height: 1.6 !important;
    min-height: 52px !important;
    padding: 0.8rem 1rem !important;
    caret-color: #d5af67 !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    opacity: 1 !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.25) !important;
}

[data-testid="stChatInput"] textarea::placeholder, [data-testid="stChatInputContainer"] textarea::placeholder,
textarea[placeholder="Ask about Biswajith..."]::placeholder {
    color: #4e5d72 !important;
    -webkit-text-fill-color: #4e5d72 !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] textarea:focus, [data-testid="stChatInputContainer"] textarea:focus,
textarea[placeholder="Ask about Biswajith..."]:focus {
    border-color: rgba(191,148,79,0.6) !important;
    box-shadow: 0 0 0 3px rgba(191,148,79,0.12), 0 2px 16px rgba(0,0,0,0.3) !important;
    outline: none !important;
    background: #1e2330 !important;
}

[data-testid="stChatInput"] button, [data-testid="stChatInputContainer"] button {
    background: linear-gradient(135deg, #d5af67, #9a6f28) !important;
    color: #0d0f14 !important;
    border-radius: 14px !important;
    border: none !important;
    width: 44px !important;
    height: 44px !important;
    min-width: 44px !important;
    flex: 0 0 44px !important;
    align-self: flex-end !important;
    margin: 0 0 4px 0 !important;
    box-shadow: 0 4px 14px rgba(191,148,79,0.35) !important;
    transition: opacity 0.15s, transform 0.1s !important;
}

[data-testid="stChatInput"] button:hover, [data-testid="stChatInputContainer"] button:hover {
    opacity: 0.88 !important;
    transform: scale(1.04) !important;
}

.stSpinner > div { border-top-color: #d5af67 !important; }

@media (max-width: 640px) {
    .block-container { padding: 0.3rem 0.55rem 0.75rem !important; }
    .header-bar { padding: 0.3rem 0 0.45rem; }
    [data-testid="stChatMessageContent"] { padding: 0.6rem 0.75rem !important; border-radius: 13px !important; }
    .chips-row { gap: 0.28rem; }
    .chip { padding: 0.3rem 0.6rem; font-size: 0.68rem; }
    .online-badge { font-size: 0.68rem; padding: 0.28rem 0.55rem; }
    
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
}
</style>

<script>
// Emergency sidebar fix for Render
document.addEventListener('DOMContentLoaded', function() {
    const emergencyFix = () => {
        // Force sidebar with fixed positioning
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            sidebar.style.position = 'fixed !important';
            sidebar.style.left = '0 !important';
            sidebar.style.top = '0 !important';
            sidebar.style.width = '320px !important';
            sidebar.style.height = '100vh !important';
            sidebar.style.zIndex = '999 !important';
            sidebar.style.display = 'block !important';
            sidebar.style.visibility = 'visible !important';
            sidebar.style.background = '#0d0f14 !important';
            sidebar.style.borderRight = '1px solid rgba(255,255,255,0.07) !important';
        }
        
        // Adjust main content for fixed sidebar
        const mainContent = document.querySelector('[data-testid="stMain"]');
        if (mainContent) {
            mainContent.style.marginLeft = '320px !important';
            mainContent.style.width = 'calc(100% - 320px) !important';
        }
        
        // Force all sidebar elements visible
        const allSidebarElements = document.querySelectorAll('[data-testid="stSidebar"], .css-1lcbmhc, .css-1d391kg, .css-17eqqhr');
        allSidebarElements.forEach(el => {
            el.style.display = 'block !important';
            el.style.visibility = 'visible !important';
        });
    };
    
    // Run aggressively
    emergencyFix();
    setTimeout(emergencyFix, 50);
    setTimeout(emergencyFix, 200);
    setTimeout(emergencyFix, 500);
    setTimeout(emergencyFix, 1000);
    setTimeout(emergencyFix, 2000);
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
    st.markdown('<div class="avatar">🧠</div>', unsafe_allow_html=True)
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
