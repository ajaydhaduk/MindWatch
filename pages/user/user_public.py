"""
MindWatch - Public Landing Page
Three states managed entirely in JS (no Streamlit rerun needed):
  STATE 1 — landing    : full public landing page
  STATE 2 — centered   : chat input centered, landing hidden (after Get Started)
  STATE 3 — chat       : messages above, input fixed at bottom (after first send)

RAG Integration:
  - JS sends user message directly to Flask API at http://localhost:8502/chat
  - Flask calls RAGChatbot.get_response() and returns JSON reply
  - JS displays the reply in the chat bubble
"""

import streamlit as st
import streamlit.components.v1 as components


def show():

    # ── Session state init ────────────────────────────────────────────────
    if "public_mode" not in st.session_state:
        st.session_state.public_mode = "landing"

    # ── Hide Streamlit chrome ─────────────────────────────────────────────
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer    {visibility: hidden;}
        header    {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            width: 100% !important;
            border: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ── Main HTML/JS page ─────────────────────────────────────────────────
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>MindWatch</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after { box-sizing:border-box; margin:0; padding:0; }

:root {
  --purple: #8b5cf6;
  --blue:   #3b82f6;
  --cyan:   #06b6d4;
  --pink:   #ec4899;
  --glass:  rgba(255,255,255,0.06);
  --glass2: rgba(255,255,255,0.10);
  --border: rgba(255,255,255,0.12);
  --text:   #ffffff;
  --muted:  rgba(255,255,255,0.60);
  --navbar-h: 62px;
}

html, body {
  height: 100%;
  font-family: 'DM Sans', sans-serif;
  color: var(--text);
  background: linear-gradient(135deg,#0a0118 0%,#1a0b2e 25%,#16123f 50%,#0e0a1f 75%,#050008 100%);
  overflow-x: hidden;
}

/* ─── ORBS ─── */
.orbs { position:fixed; inset:0; z-index:0; overflow:hidden; pointer-events:none; }
.orb  { position:absolute; border-radius:50%; filter:blur(72px); opacity:.28; animation:drift 22s infinite ease-in-out; }
.o1   { width:520px; height:520px; background:radial-gradient(circle,var(--purple),transparent 70%); top:-12%; left:-8%; }
.o2   { width:420px; height:420px; background:radial-gradient(circle,var(--blue),transparent 70%);   top:45%;  right:-8%; animation-delay:8s; }
.o3   { width:340px; height:340px; background:radial-gradient(circle,var(--cyan),transparent 70%);   bottom:-10%; left:35%; animation-delay:16s; }
@keyframes drift {
  0%,100% { transform:translate(0,0) scale(1); }
  25%     { transform:translate(60px,-60px) scale(1.12); }
  50%     { transform:translate(-40px,60px) scale(.9); }
  75%     { transform:translate(50px,35px) scale(1.06); }
}

/* ─── NAVBAR ─── */
.navbar {
  position:fixed; top:0; left:0; right:0; z-index:999;
  height:var(--navbar-h);
  background:rgba(10,1,24,.88);
  backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px);
  border-bottom:1px solid var(--border);
  padding:0 2rem;
  animation:slideDown .55s ease;
}
@keyframes slideDown {
  from { opacity:0; transform:translateY(-100%); }
  to   { opacity:1; transform:translateY(0); }
}
.nav-inner {
  height:100%; max-width:1320px; margin:0 auto;
  display:flex; align-items:center; justify-content:space-between;
}
.brand {
  display:flex; align-items:center; gap:.65rem;
  font-family:'Syne',sans-serif; font-size:1.25rem; font-weight:800;
  color:var(--text); text-decoration:none; cursor:pointer; border:none; background:none;
}
.brand-icon {
  width:36px; height:36px; border-radius:10px;
  background:linear-gradient(135deg,var(--purple),var(--blue));
  display:flex; align-items:center; justify-content:center; font-size:1.2rem;
  box-shadow:0 4px 18px rgba(139,92,246,.45);
  animation:pulseLogo 3s ease-in-out infinite;
}
@keyframes pulseLogo {
  0%,100% { box-shadow:0 4px 18px rgba(139,92,246,.45); }
  50%     { box-shadow:0 4px 32px rgba(59,130,246,.65); }
}
.nav-login-btn {
  font-family:'DM Sans',sans-serif; font-weight:600;
  padding:.45rem 1.2rem; border-radius:10px; font-size:.9rem;
  background:var(--glass); border:1px solid var(--border);
  color:var(--text); cursor:pointer;
  transition:all .25s ease;
}
.nav-login-btn:hover {
  background:var(--glass2); border-color:rgba(139,92,246,.5);
  transform:translateY(-1px);
}

/* ════ STATE 1 — LANDING PAGE ════ */
#landingPage {
  position:relative; z-index:1;
  transition:opacity .45s cubic-bezier(.4,0,.2,1), transform .45s cubic-bezier(.4,0,.2,1);
}
#landingPage.hiding {
  opacity:0; transform:scale(.97) translateY(-14px);
  pointer-events:none;
}
#landingPage.gone { display:none; }

.landing-hero {
  min-height:50vh;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  padding:5rem 2rem 2rem; text-align:center;
}
.landing-brain-icon {
  font-size:56px; margin-bottom:.85rem;
  animation:glowPulse 3s ease-in-out infinite;
}
@keyframes glowPulse {
  0%,100% { filter:drop-shadow(0 0 28px var(--purple)); transform:scale(1); }
  50%     { filter:drop-shadow(0 0 48px var(--blue));   transform:scale(1.05); }
}
.landing-title {
  font-family:'Syne',sans-serif;
  font-size:clamp(2rem,5vw,3.5rem); font-weight:800; margin-bottom:.5rem;
  background:linear-gradient(135deg,#fff,var(--purple),var(--blue));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  line-height:1.1;
}
.landing-subtitle {
  font-size:clamp(.95rem,1.8vw,1.2rem); color:var(--muted);
  max-width:600px; margin:0 auto 1.5rem; line-height:1.5;
}
.btn-row { display:flex; gap:.75rem; flex-wrap:wrap; justify-content:center; margin-bottom:1.5rem; }
.btn-primary {
  font-family:'DM Sans',sans-serif; font-weight:700;
  padding:.75rem 2rem; border-radius:12px; border:none; cursor:pointer;
  background:linear-gradient(135deg,var(--purple),var(--blue));
  color:#fff; font-size:.95rem;
  box-shadow:0 8px 25px rgba(139,92,246,.35);
  transition:all .3s cubic-bezier(.4,0,.2,1);
}
.btn-primary:hover { transform:translateY(-2px) scale(1.03); box-shadow:0 12px 35px rgba(139,92,246,.55); }
.btn-secondary {
  font-family:'DM Sans',sans-serif; font-weight:600;
  padding:.75rem 1.75rem; border-radius:12px;
  background:var(--glass); border:1px solid var(--border);
  color:var(--text); font-size:.95rem; cursor:pointer;
  backdrop-filter:blur(10px); transition:all .3s ease;
}
.btn-secondary:hover { background:var(--glass2); border-color:rgba(255,255,255,.3); transform:translateY(-2px); }

.welcome-card {
  max-width:620px; margin:0 auto;
  padding:1.25rem 1.75rem;
  background:var(--glass); backdrop-filter:blur(20px);
  border:1px solid var(--border); border-radius:16px;
  color:var(--muted); font-size:.93rem; line-height:1.65;
}

/* Features */
.features-section { padding:3rem 2rem; max-width:1200px; margin:0 auto; }
.section-title {
  font-family:'Syne',sans-serif;
  font-size:clamp(1.5rem,3vw,2.25rem); font-weight:700;
  text-align:center; margin-bottom:.4rem;
  background:linear-gradient(135deg,#fff,var(--purple));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.section-subtitle { text-align:center; color:var(--muted); font-size:.97rem; margin-bottom:2rem; }
.features-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.feature-card {
  padding:1.75rem; background:var(--glass); backdrop-filter:blur(20px);
  border:1px solid var(--border); border-radius:20px; transition:all .3s ease;
}
.feature-card:hover {
  transform:translateY(-8px); box-shadow:0 20px 50px rgba(139,92,246,.2);
  border-color:rgba(139,92,246,.3);
}
.feature-icon { font-size:2.5rem; margin-bottom:1rem; display:block; }
.feature-title { font-family:'Syne',sans-serif; font-size:1.15rem; font-weight:700; margin-bottom:.6rem; }
.feature-desc  { color:var(--muted); font-size:.88rem; line-height:1.65; }

/* Stats */
.stats-section { padding:2rem; max-width:1000px; margin:0 auto; }
.stats-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.stat-card {
  text-align:center; padding:1.5rem 1rem;
  background:var(--glass); backdrop-filter:blur(20px);
  border:1px solid var(--border); border-radius:16px; transition:all .3s ease;
}
.stat-card:hover { transform:translateY(-5px) scale(1.02); box-shadow:0 12px 35px rgba(139,92,246,.2); }
.stat-number {
  font-family:'Syne',sans-serif; font-size:clamp(2rem,4vw,2.75rem);
  font-weight:800; display:block;
  background:linear-gradient(135deg,var(--purple),var(--cyan));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  margin-bottom:.25rem; line-height:1.2;
}
.stat-label { color:var(--muted); font-size:.9rem; font-weight:500; }

/* Footer */
.footer-section {
  padding:1.5rem 2rem 1rem; text-align:center;
  border-top:1px solid rgba(255,255,255,.05);
}
.footer-msg { color:var(--muted); font-size:.97rem; margin-bottom:.85rem; }
.footer-badge {
  display:inline-flex; align-items:center; gap:.5rem;
  padding:.55rem 1.2rem; background:var(--glass);
  border:1px solid var(--border); border-radius:50px;
  font-size:.82rem; color:rgba(255,255,255,.55); margin-bottom:1rem;
}
.footer-copy { color:rgba(255,255,255,.4); font-size:.82rem; }

/* ════ STATE 2 — CENTERED CHAT ════ */
#chatShell {
  display:none;
  position:fixed;
  top:var(--navbar-h); left:0; right:0; bottom:0;
  z-index:2;
  flex-direction:column;
  overflow:hidden;
}
#chatShell.active { display:flex; }

#centeredView {
  flex:1;
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  padding:2rem 1.5rem;
  transition:opacity .38s cubic-bezier(.4,0,.2,1), transform .38s cubic-bezier(.4,0,.2,1);
}
#centeredView.hiding {
  opacity:0; transform:translateY(-18px);
  pointer-events:none;
}
#centeredView.gone { display:none; }

.chat-hero-icon {
  font-size:3.2rem; margin-bottom:1rem; line-height:1;
  animation:glowPulse 3s ease-in-out infinite;
}
.chat-hero-title {
  font-family:'Syne',sans-serif;
  font-size:clamp(1.5rem,3.5vw,2.2rem); font-weight:800; text-align:center;
  background:linear-gradient(135deg,#fff 0%,var(--purple) 55%,var(--cyan) 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  line-height:1.2; margin-bottom:.4rem;
}
.chat-hero-sub {
  color:var(--muted); font-size:.93rem; text-align:center;
  margin-bottom:2rem; max-width:420px;
}

.center-box {
  width:100%; max-width:640px;
  animation:riseUp .55s cubic-bezier(.4,0,.2,1) .05s both;
}
@keyframes riseUp {
  from { opacity:0; transform:translateY(22px) scale(.98); }
  to   { opacity:1; transform:translateY(0) scale(1); }
}

/* ─── INPUT BAR ─── */
.input-bar {
  display:flex; align-items:flex-end; gap:.45rem;
  background:rgba(255,255,255,.07);
  border:1px solid var(--border); border-radius:20px;
  padding:.65rem .65rem .65rem 1.1rem;
  transition:border-color .25s, box-shadow .25s;
  box-shadow:0 8px 32px rgba(0,0,0,.3);
}
.input-bar:focus-within {
  border-color:rgba(139,92,246,.6);
  box-shadow:0 0 0 3px rgba(139,92,246,.15), 0 8px 32px rgba(0,0,0,.3);
}
.input-text {
  flex:1; background:none; border:none; outline:none;
  color:var(--text); font-family:'DM Sans',sans-serif;
  font-size:.95rem; line-height:1.5;
  resize:none; min-height:24px; max-height:130px; overflow-y:auto; padding:0;
  scrollbar-width:none;
}
.input-text::placeholder { color:var(--muted); }
.input-text::-webkit-scrollbar { display:none; }
.input-actions { display:flex; align-items:center; gap:.35rem; flex-shrink:0; }
.mic-btn {
  width:38px; height:38px; border-radius:11px;
  display:flex; align-items:center; justify-content:center;
  border:none; cursor:pointer; font-size:1.1rem;
  color:var(--muted); background:transparent;
  transition:all .2s;
}
.mic-btn:hover { background:var(--glass2); color:var(--purple); }
.mic-btn.rec   { color:#f87171; background:rgba(248,113,113,.15); animation:micPulse 1.2s infinite; }
@keyframes micPulse {
  0%,100% { box-shadow:0 0 0 0 rgba(248,113,113,.4); }
  50%     { box-shadow:0 0 0 8px rgba(248,113,113,0); }
}
.send-btn {
  width:38px; height:38px; border-radius:11px;
  display:flex; align-items:center; justify-content:center;
  border:none; cursor:pointer;
  background:linear-gradient(135deg,var(--purple),var(--blue));
  color:#fff;
  box-shadow:0 3px 12px rgba(139,92,246,.4);
  transition:all .22s; flex-shrink:0;
}
.send-btn:hover    { transform:scale(1.08); box-shadow:0 5px 18px rgba(139,92,246,.6); }
.send-btn:disabled { opacity:.35; cursor:not-allowed; transform:none; }

.mic-status {
  text-align:center; font-size:.76rem; color:#f87171;
  height:16px; margin-top:.4rem; opacity:0; transition:opacity .3s;
}
.mic-status.on { opacity:1; }

/* Pills */
.pills {
  display:flex; flex-wrap:wrap; gap:.5rem;
  justify-content:center; margin-top:1rem;
  animation:riseUp .55s cubic-bezier(.4,0,.2,1) .2s both;
}
.pill {
  padding:.42rem .9rem;
  background:var(--glass); border:1px solid var(--border);
  border-radius:50px; font-size:.8rem; color:var(--muted);
  cursor:pointer; transition:all .2s; white-space:nowrap;
}
.pill:hover { background:var(--glass2); color:var(--text); border-color:var(--purple); transform:translateY(-1px); }

.guest-hint {
  margin-top:1.2rem; text-align:center;
  font-size:.8rem; color:var(--muted);
  animation:riseUp .55s cubic-bezier(.4,0,.2,1) .3s both;
}
.guest-hint a {
  color:var(--purple); text-decoration:none; font-weight:600;
  border-bottom:1px solid rgba(139,92,246,.3);
  transition:color .2s;
}
.guest-hint a:hover { color:var(--cyan); }

/* ════ STATE 3 — ACTIVE CHAT ════ */
#activeChatView {
  flex:1; display:flex; flex-direction:column;
  overflow:hidden;
  opacity:0; pointer-events:none;
  position:absolute; inset:0;
  transition:opacity .4s ease;
}
#activeChatView.visible {
  opacity:1; pointer-events:all; position:relative;
}

.msgs-wrap {
  flex:1; overflow-y:auto; overflow-x:hidden;
  padding:.75rem 1rem 0;
  display:flex; flex-direction:column; justify-content:flex-end;
  scrollbar-width:thin;
  scrollbar-color:rgba(139,92,246,.4) transparent;
}
.msgs-wrap::-webkit-scrollbar { width:4px; }
.msgs-wrap::-webkit-scrollbar-thumb { background:rgba(139,92,246,.4); border-radius:4px; }
.msgs-inner {
  display:flex; flex-direction:column; gap:.85rem;
  max-width:720px; width:100%; margin:0 auto; padding-bottom:.5rem;
}

.msg { display:flex; gap:.65rem; align-items:flex-start; animation:msgIn .32s ease; }
@keyframes msgIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
.msg.user { flex-direction:row-reverse; }
.msg-av {
  width:34px; height:34px; border-radius:10px; flex-shrink:0;
  display:flex; align-items:center; justify-content:center; font-size:1.1rem;
}
.msg-av.ai  { background:linear-gradient(135deg,var(--purple),var(--blue)); box-shadow:0 3px 12px rgba(139,92,246,.4); }
.msg-av.usr { background:rgba(255,255,255,.1); border:1px solid var(--border); }

.bubble {
  max-width:72%; padding:.7rem 1rem;
  border-radius:16px; font-size:.91rem; line-height:1.6;
  word-break:break-word;
}
.msg.ai   .bubble { background:var(--glass); border:1px solid var(--border); border-radius:16px 16px 16px 4px; }
.msg.user .bubble {
  background:linear-gradient(135deg,rgba(139,92,246,.3),rgba(59,130,246,.25));
  border:1px solid rgba(139,92,246,.3); border-radius:16px 16px 4px 16px;
}

/* Typing dots */
.typing { display:flex; gap:5px; align-items:center; height:20px; padding:2px 4px; }
.typing span {
  width:7px; height:7px; border-radius:50%;
  background:var(--purple); display:block;
  animation:bounce 1.2s infinite ease-in-out;
}
.typing span:nth-child(2) { animation-delay:.18s; }
.typing span:nth-child(3) { animation-delay:.36s; }
@keyframes bounce {
  0%,80%,100% { transform:scale(.7); opacity:.5; }
  40%         { transform:scale(1);   opacity:1; }
}

/* Bottom bar */
.bottom-bar {
  border-top:1px solid var(--border);
  padding:.7rem 1rem .9rem;
  background:rgba(10,1,24,.75);
  backdrop-filter:blur(24px);
}
.bottom-inner { max-width:720px; margin:0 auto; }
.bottom-pills {
  display:flex; flex-wrap:nowrap; gap:.5rem; overflow-x:auto;
  padding-bottom:.5rem; scrollbar-width:none;
  transition:opacity .4s, height .4s; margin-bottom:.5rem;
}
.bottom-pills::-webkit-scrollbar { display:none; }

.bottom-bar .swoosh { animation:swoosh .5s cubic-bezier(.4,0,.2,1); }
@keyframes swoosh {
  0%   { transform:translateY(40px); opacity:0; }
  100% { transform:translateY(0);    opacity:1; }
}

@media(max-width:600px) {
  .features-grid,.stats-grid { grid-template-columns:1fr; }
  .center-box { max-width:100%; }
  .msgs-wrap  { padding:.5rem .6rem 0; }
  .bottom-bar { padding:.5rem .6rem .7rem; }
  .bottom-pills { display:none; }
}
</style>
</head>
<body>

<!-- ─── ORBS ─── -->
<div class="orbs">
  <div class="orb o1"></div>
  <div class="orb o2"></div>
  <div class="orb o3"></div>
</div>

<!-- ─── NAVBAR ─── -->
<nav class="navbar">
  <div class="nav-inner">
    <button class="brand" onclick="goHome()">
      <div class="brand-icon">&#x1F9E0;</div>
      MindWatch
    </button>
    <button class="nav-login-btn" onclick="window.open('http://localhost:5500/login.html','_blank')">Login</button>
  </div>
</nav>

<!-- ════ STATE 1 — LANDING PAGE ════ -->
<div id="landingPage">

  <div class="landing-hero">
    <div class="landing-brain-icon">&#x1F9E0;</div>
    <h1 class="landing-title">MindWatch</h1>
    <p class="landing-subtitle">A calm space to reflect on how you feel</p>
    <div class="btn-row">
      <button class="btn-primary" onclick="activateChat()">Get Started</button>
      <button class="btn-secondary" onclick="window.open('http://localhost:5500/login.html','_blank')">Login</button>
    </div>
    <div class="welcome-card">
      Welcome to MindWatch — your personal mental wellness companion.
      Take a moment to check in with yourself, track your emotional journey,
      and gain insights powered by AI. Your mental health matters. &#x1F49C;
    </div>
  </div>

  <div class="features-section">
    <h2 class="section-title">Features</h2>
    <p class="section-subtitle">Powerful tools to support your mental wellness journey</p>
    <div class="features-grid">
      <div class="feature-card">
        <span class="feature-icon" style="color:#8b5cf6;">&#x1F3A4;</span>
        <div class="feature-title">Voice Check-in</div>
        <div class="feature-desc">Express your thoughts and feelings naturally through voice. Our AI listens and understands your emotional state without judgment.</div>
      </div>
      <div class="feature-card">
        <span class="feature-icon" style="color:#3b82f6;">&#x1F4CA;</span>
        <div class="feature-title">Emotional Analytics</div>
        <div class="feature-desc">Track your emotional patterns over time. Visualize your mental health journey with beautiful, insightful charts and trends.</div>
      </div>
      <div class="feature-card">
        <span class="feature-icon" style="color:#06b6d4;">&#x2728;</span>
        <div class="feature-title">AI Insights</div>
        <div class="feature-desc">Receive personalized recommendations. Our AI helps you understand your emotions and suggests ways to improve your wellbeing.</div>
      </div>
    </div>
  </div>

  <div class="stats-section">
    <div class="stats-grid">
      <div class="stat-card"><span class="stat-number">10K+</span><div class="stat-label">Active Users</div></div>
      <div class="stat-card"><span class="stat-number">50K+</span><div class="stat-label">Check-ins Completed</div></div>
      <div class="stat-card"><span class="stat-number">95%</span><div class="stat-label">Satisfaction Rate</div></div>
    </div>
  </div>

  <div class="footer-section">
    <div class="footer-msg">&#x1F512; Your privacy matters to us</div>
    <div class="footer-badge">&#x1F6E1;&#xFE0F; End-to-end encrypted &bull; HIPAA compliant</div>
    <div class="footer-copy">&copy; 2024 MindWatch. All rights reserved.</div>
  </div>

</div>

<!-- ════ STATES 2 & 3 — CHAT SHELL ════ -->
<div id="chatShell">

  <!-- STATE 2 — CENTERED INPUT -->
  <div id="centeredView">
    <div class="chat-hero-icon">&#x1F9E0;</div>
    <div class="chat-hero-title">How are you feeling today?</div>
    <div class="chat-hero-sub">Share anything on your mind — no account needed to start.</div>

    <div class="center-box">
      <div class="input-bar" id="centerBar">
        <textarea class="input-text" id="centerInp"
          placeholder="Share how you're feeling..."
          rows="1"
          oninput="resize(this); toggleSend('centerInp','centerSend');"
          onkeydown="handleKey(event,'centerInp')"></textarea>
        <div class="input-actions">
          <button class="mic-btn" id="micBtn" title="Voice input" onclick="toggleMic('centerInp','centerSend')">&#x1F399;&#xFE0F;</button>
          <button class="send-btn" id="centerSend" onclick="sendFirst()" disabled>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"/>
              <polygon points="22 2 15 22 11 13 2 9 22 2"/>
            </svg>
          </button>
        </div>
      </div>
      <div class="mic-status" id="micStatus">&#x1F534; Listening... speak now</div>

      <div class="pills" id="centerPills">
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">&#x1F614; Feeling anxious</div>
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">&#x1F60A; Having a good day</div>
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">&#x1F634; Feeling tired</div>
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">&#x1F624; Stressed out</div>
      </div>

      <div class="guest-hint">
        Want to save your progress?
        <a href="#" onclick="window.open('http://localhost:5500/login.html','_blank'); return false;">Sign in or create a free account</a>
      </div>
    </div>
  </div>

  <!-- STATE 3 — ACTIVE CHAT -->
  <div id="activeChatView">
    <div class="msgs-wrap" id="msgsWrap">
      <div class="msgs-inner" id="msgs"></div>
    </div>

    <div class="bottom-bar">
      <div class="bottom-inner">
        <div class="bottom-pills" id="bottomPills">
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">&#x1F614; Anxious</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">&#x1F60A; Good day</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">&#x1F634; Tired</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">&#x1F624; Stressed</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">&#x1F615; Confused</div>
        </div>
        <div class="input-bar" id="bottomBar">
          <textarea class="input-text" id="bottomInp"
            placeholder="Share how you're feeling..."
            rows="1"
            oninput="resize(this); toggleSend('bottomInp','bottomSend');"
            onkeydown="handleKey(event,'bottomInp')"></textarea>
          <div class="input-actions">
            <button class="mic-btn" id="micBtn2" title="Voice input" onclick="toggleMic('bottomInp','bottomSend')">&#x1F399;&#xFE0F;</button>
            <button class="send-btn" id="bottomSend" onclick="sendMsg()" disabled>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"/>
                <polygon points="22 2 15 22 11 13 2 9 22 2"/>
              </svg>
            </button>
          </div>
        </div>
        <div style="text-align:center; margin-top:.45rem;">
          <span style="font-size:.75rem; color:var(--muted);">
            &#x1F4A1; <a href="#" onclick="window.open('http://localhost:5500/login.html','_blank'); return false;"
               style="color:var(--purple); text-decoration:none; border-bottom:1px solid rgba(139,92,246,.3);">
               Sign in</a> to save your conversation &amp; unlock full features
          </span>
        </div>
      </div>
    </div>
  </div>

</div><!-- /#chatShell -->


<script>

/* ══════════════════════════════════════════
   RAG BRIDGE — calls Flask API at port 8502
   ══════════════════════════════════════════ */
function sendToRAG(text) {
  fetch("http://localhost:8502/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text })
  })
  .then(function(res) { return res.json(); })
  .then(function(data) {
    removeTyping();
    addMsg(data.reply, 'ai');
  })
  .catch(function(err) {
    removeTyping();
    addMsg("Sorry, I could not connect to the AI. Please try again.", 'ai');
    console.error('RAG API error:', err);
  });
}

/* ══════════════════════════════════════════
   STATE TRANSITIONS
   ══════════════════════════════════════════ */
function activateChat() {
  var landing = document.getElementById('landingPage');
  var shell   = document.getElementById('chatShell');
  landing.classList.add('hiding');
  setTimeout(function() {
    landing.classList.add('gone');
    shell.classList.add('active');
    document.getElementById('centerInp').focus();
  }, 420);
}

function goHome() {
  var landing = document.getElementById('landingPage');
  var shell   = document.getElementById('chatShell');
  if (chatStarted) return;
  shell.classList.remove('active');
  landing.classList.remove('gone');
  requestAnimationFrame(function() {
    requestAnimationFrame(function() {
      landing.classList.remove('hiding');
    });
  });
}

var chatStarted = false;
function switchToActiveChat() {
  if (chatStarted) return;
  chatStarted = true;
  var centered = document.getElementById('centeredView');
  var active   = document.getElementById('activeChatView');
  centered.classList.add('hiding');
  setTimeout(function() {
    centered.classList.add('gone');
    active.classList.add('visible');
    var bb = document.getElementById('bottomBar');
    bb.classList.add('swoosh');
    setTimeout(function() { bb.classList.remove('swoosh'); }, 500);
  }, 320);
}

/* ══════════════════════════════════════════
   INPUT HELPERS
   ══════════════════════════════════════════ */
function resize(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 130) + 'px';
}
function toggleSend(inpId, btnId) {
  document.getElementById(btnId).disabled =
    !document.getElementById(inpId).value.trim();
}
function handleKey(e, inpId) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    if (inpId === 'centerInp') { sendFirst(); } else { sendMsg(); }
  }
}
function usePill(el, inpId, btnId) {
  var inp = document.getElementById(inpId);
  inp.value = el.textContent.trim();
  resize(inp);
  toggleSend(inpId, btnId);
  inp.focus();
}

/* ══════════════════════════════════════════
   SEND LOGIC
   ══════════════════════════════════════════ */
function sendFirst() {
  var inp  = document.getElementById('centerInp');
  var text = inp.value.trim();
  if (!text) return;
  switchToActiveChat();
  setTimeout(function() {
    addMsg(text, 'user');
    inp.value = '';
    showTyping();
    sendToRAG(text);
    document.getElementById('bottomInp').focus();
  }, 380);
}

function sendMsg() {
  var inp  = document.getElementById('bottomInp');
  var text = inp.value.trim();
  if (!text) return;
  addMsg(text, 'user');
  inp.value = '';
  inp.style.height = 'auto';
  document.getElementById('bottomSend').disabled = true;
  hidePills();
  showTyping();
  sendToRAG(text);
}

function hidePills() {
  var p = document.getElementById('bottomPills');
  if (p) {
    p.style.opacity       = '0';
    p.style.height        = '0';
    p.style.margin        = '0';
    p.style.overflow      = 'hidden';
    p.style.pointerEvents = 'none';
  }
}

/* ══════════════════════════════════════════
   DOM HELPERS
   ══════════════════════════════════════════ */
function addMsg(text, role) {
  var c  = document.getElementById('msgs');
  var d  = document.createElement('div');
  d.className = 'msg ' + role;
  var av = role === 'ai'
    ? '<div class="msg-av ai">&#x1F9E0;</div>'
    : '<div class="msg-av usr">&#x1F464;</div>';
  d.innerHTML = av + '<div class="bubble">' + esc(text) + '</div>';
  c.appendChild(d);
  scrollBottom();
}
function showTyping() {
  var c = document.getElementById('msgs');
  var d = document.createElement('div');
  d.className = 'msg ai';
  d.id = 'typing';
  d.innerHTML = '<div class="msg-av ai">&#x1F9E0;</div><div class="bubble"><div class="typing"><span></span><span></span><span></span></div></div>';
  c.appendChild(d);
  scrollBottom();
}
function removeTyping() {
  var e = document.getElementById('typing');
  if (e) e.remove();
}
function scrollBottom() {
  var w = document.getElementById('msgsWrap');
  if (w) w.scrollTop = w.scrollHeight;
}
function esc(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

/* ══════════════════════════════════════════
   MICROPHONE (Web Speech API)
   ══════════════════════════════════════════ */
var recog = null, isRec = false;

function toggleMic(inpId, btnId) {
  if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    alert('Voice input requires Chrome or Edge browser.'); return;
  }
  if (isRec) { stopMic(); } else { startMic(inpId, btnId); }
}
function startMic(inpId, btnId) {
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  recog = new SR();
  recog.continuous = false; recog.interimResults = true; recog.lang = 'en-US';
  recog.onstart = function() {
    isRec = true;
    var mb = document.getElementById(btnId === 'centerSend' ? 'micBtn' : 'micBtn2');
    if (mb) mb.classList.add('rec');
    var ms = document.getElementById('micStatus');
    if (ms) ms.classList.add('on');
  };
  recog.onresult = function(e) {
    var tr = '';
    for (var i = e.resultIndex; i < e.results.length; i++) tr += e.results[i][0].transcript;
    var inp = document.getElementById(inpId);
    if (inp) { inp.value = tr; resize(inp); toggleSend(inpId, btnId); }
  };
  recog.onend   = function() { stopMic(); };
  recog.onerror = function() { stopMic(); };
  recog.start();
}
function stopMic() {
  if (recog) { recog.stop(); recog = null; }
  isRec = false;
  ['micBtn','micBtn2'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.classList.remove('rec');
  });
  var ms = document.getElementById('micStatus');
  if (ms) ms.classList.remove('on');
}
</script>

</body>
</html>"""

    components.html(html_code, height=820, scrolling=False)