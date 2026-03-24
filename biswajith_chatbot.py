import os
import streamlit as st
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="Chat with Biswajith",
    page_icon=":robot_face:",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Manrope:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    background:
        radial-gradient(circle at 14% 12%, rgba(191, 148, 79, 0.12), transparent 20%),
        radial-gradient(circle at 82% 10%, rgba(191, 148, 79, 0.08), transparent 18%),
        linear-gradient(180deg, #0a0b0f 0%, #0d1016 100%);
    color: #e7eaf0;
    font-family: 'Manrope', sans-serif;
}
.stApp {
    background: transparent;
}
[data-testid="stAppViewContainer"] {
    background: transparent;
}
[data-testid="stHeader"],
footer,
#MainMenu {
    display: none !important;
}
.block-container {
    max-width: none;
    padding-top: 0.9rem;
    padding-bottom: 1.1rem;
    padding-left: 1.25rem;
    padding-right: 1.25rem;
}
.main-shell {
    display: grid;
    grid-template-columns: minmax(0, 1fr);
    gap: 0.9rem;
    margin-bottom: 0.7rem;
}
.topbar-shell {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.2rem;
    padding: 1.1rem 1.2rem 0.95rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.title-stack {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
}
.eyebrow {
    color: #d4ac63;
    font-size: 0.76rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-family: 'Space Grotesk', sans-serif;
    display: inline-flex;
    align-items: center;
    width: fit-content;
    gap: 0.5rem;
    padding: 0.45rem 0.8rem;
    border-radius: 999px;
    border: 1px solid rgba(191, 148, 79, 0.28);
    background: rgba(191, 148, 79, 0.07);
}
.eyebrow::before {
    content: "•";
    font-size: 0.9rem;
}
.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem;
    line-height: 0.98;
    color: #f5f7fb;
    letter-spacing: -0.03em;
    margin-top: 0.9rem;
}
.page-subtitle {
    color: #9dabbe;
    font-size: 0.98rem;
    max-width: 760px;
    margin-top: 0.7rem;
}
.status-badge {
    padding: 0.55rem 0.8rem;
    border-radius: 999px;
    background: rgba(191, 148, 79, 0.09);
    border: 1px solid rgba(191, 148, 79, 0.22);
    color: #e3c58e;
    font-size: 0.8rem;
    white-space: nowrap;
}
.prompt-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    padding: 0 0.1rem;
}
.prompt-chip {
    padding: 0.72rem 0.98rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.09);
    color: #e2e7ee;
    font-size: 0.88rem;
    line-height: 1;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
}
.avatar-ring {
    width: 44px; height: 44px; border-radius: 14px;
    background: linear-gradient(135deg, #d5af67, #a9813f);
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 0.9rem; font-size: 1.2rem;
    box-shadow: 0 12px 30px rgba(3, 10, 18, 0.28);
}
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    margin-bottom: 0.9rem;
    padding: 0.05rem 0;
}
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] {
    background: linear-gradient(135deg, #d5af67, #a9813f);
    color: #111318;
}
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"] {
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff;
}
[data-testid="stChatMessageAvatarAssistant"],
[data-testid="stChatMessageAvatarUser"] {
    margin-top: 0.1rem;
}
[data-testid="stChatMessageContent"] {
    color: #edf2f7;
    font-size: 0.98rem;
    line-height: 1.8;
    background: #121722;
    border: 1px solid rgba(120, 141, 180, 0.18);
    border-radius: 22px;
    padding: 1rem 1.15rem;
    max-width: 720px;
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
}
[data-testid="stChatInput"] textarea {
    background: rgba(18, 21, 29, 0.98) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #ececec !important;
    border-radius: 24px !important;
    font-family: 'Manrope', sans-serif;
    min-height: 62px !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #8da0bc !important;
}
[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #d5af67, #b58b47) !important;
    color: #111318 !important;
    border-radius: 18px !important;
    border: none !important;
    width: 52px !important;
    height: 52px !important;
}
[data-testid="stChatInput"] button:hover {
    background: linear-gradient(135deg, #ddb771, #be934d) !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: rgba(191, 148, 79, 0.42) !important;
    box-shadow: 0 0 0 1px rgba(191, 148, 79, 0.22) !important;
}
[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(16, 19, 24, 0.99), rgba(13, 16, 20, 0.99)) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.07);
}
.info-card {
    background: rgba(255, 255, 255, 0.022);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 0.85rem 0.9rem;
    margin-bottom: 0.55rem;
    font-size: 0.83rem;
}
.info-card strong { color: #f4f4f5; }
.tag {
    display: inline-block;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 999px;
    padding: 0.38rem 0.75rem;
    font-size: 0.75rem;
    margin: 0.18rem;
    color: #d7dbe2;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    color: #d4ac63;
    text-transform: uppercase;
    margin: 1rem 0 0.5rem;
}
div[data-testid="stChatInput"] {
    margin-top: 0.75rem;
    padding-top: 0.4rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}
.sidebar-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.18rem;
    font-weight: 700;
    color: #f3f4f6;
}
.sidebar-role {
    font-size: 0.82rem;
    color: #a4adba;
}
.sidebar-intro {
    color: #c6ccd6;
    font-size: 0.84rem;
    line-height: 1.6;
}
.chat-frame {
    padding: 0.8rem 0.8rem 0.35rem;
    border-radius: 0;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    background:
        radial-gradient(circle at top center, rgba(191, 148, 79, 0.04), transparent 26%),
        linear-gradient(180deg, rgba(9, 11, 16, 0.88), rgba(9, 11, 16, 0.92));
    min-height: 66vh;
}
.chat-body {
    padding: 0.5rem 0.1rem 0.2rem;
}
.chat-caption {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 0 0 0.75rem;
    margin-bottom: 0.35rem;
}
.chat-caption-title {
    font-family: 'Space Grotesk', sans-serif;
    color: #f4f4f5;
    font-size: 0.96rem;
}
.chat-caption-copy {
    color: #a1a1aa;
    font-size: 0.8rem;
}
@media (max-width: 760px) {
    .block-container {
        padding-top: 0.75rem;
        padding-left: 0.75rem;
        padding-right: 0.75rem;
    }
    .topbar-shell,
    .chat-caption {
        flex-direction: column;
        align-items: flex-start;
    }
    .topbar-shell {
        padding: 0.7rem 0 0.85rem;
    }
    .page-title {
        font-size: 2.2rem;
    }
    .page-subtitle {
        font-size: 0.92rem;
    }
}
</style>
""", unsafe_allow_html=True)

KNOWLEDGE_BASE = """
You are a chatbot that represents Biswajith PN. Answer questions naturally as if you are him or know him deeply.
Use only the confirmed facts below. If something is not in the knowledge base, say I don't have that detail yet.

CONFIRMED FACTS ABOUT BISWAJITH PN:

IDENTITY:
- Full Name: Biswajith PN
- Location: 2/1707, Sasi Nagar, Vembakottai Road, Sivakasi, Tamil Nadu, India
- Phone: 81100 61566
- Email: pnbiswajith@gmail.com
- LinkedIn: linkedin.com/in/biswajithpn
- GitHub: github.com/BiswajithPN
- Instagram edits page: @ig._.obito._.edits

EDUCATION:
- Engineering student specializing in Artificial Intelligence and Data Science
- Connected to Mepco college

TECHNICAL INTERESTS:
- Artificial Intelligence, Data Science, Software Development
- Chatbot Development, RAG Systems, App Development
- LangChain, Streamlit, PDF-based knowledge retrieval, Python

PROJECTS:
1. Life Tracker App - Futuristic mobile app for expense tracking, budget control, habit and productivity tracking
2. PDF RAG Chatbot - AI chatbot using LangChain and Streamlit for answering from uploaded PDFs
3. Resume and Internship Prep - Actively applying for software/IT internships
4. Forex Basics PPT - Learning and presenting Forex trading basics
5. MSEC E-SPORTS Poster - Designed a Free Fire esports poster

SKILLS:
- Video Editing: Strong skill
- Time available: around 2 hours per day
- Chatbot building, app development, content creation, practical learning

GAMING:
- Interested in design and digital creative work

CONTENT CREATION:
- Editing Instagram: @ig._.obito._.edits
- Good at video editing

CAREER GOALS:
- Seeking software/IT internship
- Career direction: AI, Data Science, Software Development

PERSONALITY:
- Prefers practical outputs over theory
- Hands-on project-based learner
- Curious about AI tools, tech, and gaming

RULES:
- Speak naturally and personally
- Only state confirmed facts
- Be friendly, direct, and practical
- Keep answers concise
"""

# SIDEBAR
with st.sidebar:
    st.markdown('<div class="section-title">Profile</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; margin-bottom:1rem;">
        <div class="avatar-ring">&#129504;</div>
        <div class="sidebar-name">Biswajith PN</div>
        <div class="sidebar-role">AI &amp; Data Science Student</div>
        <div class="sidebar-intro" style="margin-top:0.9rem;">
            Practical builder focused on AI products, applied software work, and visually polished creative output.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Quick Facts</div>', unsafe_allow_html=True)
    facts = [
        ("&#128205;", "Location", "Sivakasi, Tamil Nadu"),
        ("&#127891;", "Degree", "AI &amp; Data Science Engg."),
        ("&#9986;", "Skill", "Video Editing"),
        ("&#127760;", "GitHub", "github.com/BiswajithPN"),
        ("&#128231;", "Email", "pnbiswajith@gmail.com"),
    ]
    for icon, label, val in facts:
        st.markdown(f"""
        <div class="info-card">
            <strong>{icon} {label}</strong><br>
            <span style="color:#cbd5e1;">{val}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Interests</div>', unsafe_allow_html=True)
    tags = ["AI/ML", "RAG Systems", "LangChain", "Streamlit", "App Dev", "BGMI", "Video Editing", "Chatbots", "Content Creation"]
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    st.markdown(tag_html, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Creative Work</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        &#128247; <strong>Edits:</strong> @ig._.obito._.edits<br>
        <span style="color:#cbd5e1;">Video edits and creative content</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# MAIN CHAT
    st.markdown("""
    <div class="main-shell">
        <div class="topbar-shell">
            <div class="title-stack">
            <div class="eyebrow">Personal AI Profile Powered By Groq</div>
            <div class="page-title">Chat with Biswajith's AI</div>
            <div class="page-subtitle">Ask about projects, skills, internship goals, creative work, or anything about Biswajith.</div>
            </div>
        <div class="status-badge">Online now</div>
        </div>
        <div class="prompt-row">
        <div class="prompt-chip">Projects</div>
        <div class="prompt-chip">Skills</div>
        <div class="prompt-chip">Career Goals</div>
        <div class="prompt-chip">Creative Work</div>
        <div class="prompt-chip">Tech Stack</div>
        </div>
        <div class="chat-frame">
            <div class="chat-caption">
            <div class="chat-caption-title">Biswajith AI</div>
            <div class="chat-caption-copy">Ask concise questions for stronger answers</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi! I'm Biswajith's AI profile. Ask me about his projects, skills, internship goals, or creative work."
    })

st.markdown('<div class="chat-body">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
st.markdown('</div>', unsafe_allow_html=True)

if prompt := st.chat_input("Ask about Biswajith..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # client is already initialized globally at the top

    api_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": KNOWLEDGE_BASE},
                        *api_messages
                    ],
                    max_tokens=1024,
                    temperature=0.7,
                )
                reply = response.choices[0].message.content
                st.write(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error("Something went wrong: " + str(e))
