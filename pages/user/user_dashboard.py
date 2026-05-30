"""
MindWatch - User Dashboard
Shows after successful login. Displays user info in navbar and chat input.
"""

import streamlit as st
import streamlit.components.v1 as components
from auth.auth_handler import AuthHandler

auth = AuthHandler()


def show():
    user = auth.get_user()
    user_name     = user.get("name", "User")    if user else "User"
    user_email    = user.get("email", "")        if user else ""
    user_picture  = user.get("picture", "")      if user else ""
    first_name    = user_name.split()[0]          if user_name else "there"
    avatar_letter = user_name[0].upper()          if user_name else "U"

    st.markdown("""
        <style>
        #MainMenu {visibility: hidden !important;}
        footer    {visibility: hidden !important;}
        header    {visibility: hidden !important;}
        .stApp    {background: transparent !important;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        .element-container {margin:0 !important; padding:0 !important;}
        iframe {display:block; width:100% !important; border:none !important;}
        </style>
    """, unsafe_allow_html=True)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>MindWatch – Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}

:root{{
  --purple:#8b5cf6; --blue:#3b82f6; --cyan:#06b6d4; --pink:#ec4899;
  --glass:rgba(255,255,255,0.06); --glass2:rgba(255,255,255,0.10);
  --border:rgba(255,255,255,0.12); --text:#fff; --muted:rgba(255,255,255,0.60);
  --navbar-h:62px;
}}

html,body{{
  height:100%; font-family:'DM Sans',sans-serif; color:var(--text);
  background:linear-gradient(135deg,#0a0118 0%,#1a0b2e 30%,#16123f 60%,#050008 100%);
  overflow:hidden;
}}

/* ── ORBS ── */
.orbs{{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none;}}
.orb{{position:absolute;border-radius:50%;filter:blur(72px);opacity:.28;animation:drift 22s infinite ease-in-out;}}
.o1{{width:520px;height:520px;background:radial-gradient(circle,var(--purple),transparent 70%);top:-12%;left:-8%;}}
.o2{{width:420px;height:420px;background:radial-gradient(circle,var(--blue),transparent 70%);top:45%;right:-8%;animation-delay:8s;}}
.o3{{width:340px;height:340px;background:radial-gradient(circle,var(--cyan),transparent 70%);bottom:-10%;left:35%;animation-delay:16s;}}
@keyframes drift{{
  0%,100%{{transform:translate(0,0) scale(1);}}
  25%{{transform:translate(60px,-60px) scale(1.12);}}
  50%{{transform:translate(-40px,60px) scale(.9);}}
  75%{{transform:translate(50px,35px) scale(1.06);}}
}}

/* ── NAVBAR ── */
.navbar{{
  position:fixed;top:0;left:0;right:0;z-index:999;height:var(--navbar-h);
  background:rgba(10,1,24,.88);
  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border-bottom:1px solid var(--border);
  padding:0 2rem;
  animation:slideDown .55s ease;
}}
@keyframes slideDown{{from{{opacity:0;transform:translateY(-100%);}}to{{opacity:1;transform:translateY(0);}}}}
.nav-inner{{height:100%;max-width:1320px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;}}
.brand{{display:flex;align-items:center;gap:.65rem;font-family:'Syne',sans-serif;font-size:1.25rem;font-weight:800;color:var(--text);text-decoration:none;}}
.brand-icon{{
  width:36px;height:36px;border-radius:10px;
  background:linear-gradient(135deg,var(--purple),var(--blue));
  display:flex;align-items:center;justify-content:center;font-size:1.2rem;
  box-shadow:0 4px 18px rgba(139,92,246,.45);
  animation:pulseLogo 3s ease-in-out infinite;
}}
@keyframes pulseLogo{{
  0%,100%{{box-shadow:0 4px 18px rgba(139,92,246,.45);}}
  50%{{box-shadow:0 4px 32px rgba(59,130,246,.65);}}
}}

/* User chip */
.user-chip{{
  display:flex;align-items:center;gap:.6rem;
  padding:.35rem .85rem .35rem .4rem;
  background:var(--glass);border:1px solid var(--border);border-radius:50px;
  cursor:pointer;position:relative;
  transition:background .25s,border-color .25s;
  animation:fadeUp .7s ease .3s both;
}}
.user-chip:hover{{background:var(--glass2);border-color:rgba(139,92,246,.45);}}
@keyframes fadeUp{{from{{opacity:0;transform:scale(.9);}}to{{opacity:1;transform:scale(1);}}}}
.av-wrap{{position:relative;width:34px;height:34px;flex-shrink:0;}}
.av-img{{width:34px;height:34px;border-radius:50%;object-fit:cover;animation:avatarGlow 3s ease-in-out infinite;}}
.av-fallback{{
  width:34px;height:34px;border-radius:50%;
  background:linear-gradient(135deg,var(--purple),var(--cyan));
  display:flex;align-items:center;justify-content:center;
  font-size:.95rem;font-weight:700;color:#fff;
  animation:avatarGlow 3s ease-in-out infinite;
}}
@keyframes avatarGlow{{
  0%,100%{{box-shadow:0 0 0 2px var(--purple),0 0 14px rgba(139,92,246,.5);}}
  50%{{box-shadow:0 0 0 2px var(--cyan),0 0 20px rgba(6,182,212,.6);}}
}}
.online-dot{{
  position:absolute;bottom:1px;right:1px;
  width:9px;height:9px;border-radius:50%;
  background:#22c55e;border:2px solid #0a0118;
  animation:blink 2.5s infinite;
}}
@keyframes blink{{0%,100%{{opacity:1;}}50%{{opacity:.4;}}}}
.uname{{font-family:'Syne',sans-serif;font-size:.88rem;font-weight:600;color:var(--text);white-space:nowrap;max-width:130px;overflow:hidden;text-overflow:ellipsis;}}
.chevron{{color:var(--muted);font-size:.7rem;transition:transform .2s;}}
.user-chip:hover .chevron{{transform:rotate(180deg);}}
.dropdown{{
  position:absolute;top:calc(100% + 10px);right:0;
  background:rgba(15,5,30,.97);backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:14px;
  padding:.5rem;min-width:200px;
  opacity:0;pointer-events:none;transform:translateY(-8px);
  transition:opacity .2s,transform .2s;
  box-shadow:0 16px 48px rgba(0,0,0,.5);
}}
.user-chip:hover .dropdown{{opacity:1;pointer-events:all;transform:translateY(0);}}
.dd-email{{padding:.5rem .75rem .75rem;color:var(--muted);font-size:.78rem;border-bottom:1px solid var(--border);margin-bottom:.4rem;}}
.dd-item{{
  display:flex;align-items:center;gap:.6rem;
  padding:.55rem .75rem;border-radius:8px;
  color:var(--text);font-size:.88rem;
  cursor:pointer;transition:background .2s;
  border:none;background:none;width:100%;text-align:left;
}}
.dd-item:hover{{background:var(--glass2);}}
.dd-item.danger{{color:#f87171;}}
.dd-item.danger:hover{{background:rgba(248,113,113,.1);}}

/* ══════════════════════════════════════
   LAYOUT — two states: centered / chat
   ══════════════════════════════════════ */

/* Full-page shell */
.shell{{
  position:fixed;
  top:var(--navbar-h);left:0;right:0;
  bottom:0;
  z-index:1;
  display:flex;
  flex-direction:column;
  overflow:hidden;
}}

/* ── CENTERED STATE ── */
.centered-view{{
  flex:1;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  padding:2rem 1.5rem;
  transition:opacity .35s ease, transform .35s ease;
}}
.centered-view.hidden{{
  opacity:0;
  transform:translateY(-20px);
  pointer-events:none;
  position:absolute;
  inset:0;
}}

.hero-icon{{
  font-size:3.2rem;
  margin-bottom:1rem;
  animation:glow-pulse 3s ease-in-out infinite;
  line-height:1;
}}
@keyframes glow-pulse{{
  0%,100%{{filter:drop-shadow(0 0 18px var(--purple));}}
  50%{{filter:drop-shadow(0 0 32px var(--cyan));}}
}}
.hero-greeting{{
  font-family:'Syne',sans-serif;
  font-size:clamp(1.6rem,4vw,2.4rem);
  font-weight:800;
  background:linear-gradient(135deg,#fff 0%,var(--purple) 50%,var(--cyan) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  text-align:center;
  line-height:1.2;
  margin-bottom:.4rem;
}}
.hero-sub{{
  color:var(--muted);
  font-size:.95rem;
  text-align:center;
  margin-bottom:2rem;
  max-width:400px;
}}

/* Center input box */
.center-box{{
  width:100%;
  max-width:640px;
  animation:riseUp .6s ease .2s both;
}}
@keyframes riseUp{{from{{opacity:0;transform:translateY(16px);}}to{{opacity:1;transform:translateY(0);}}}}

.input-bar{{
  display:flex;
  align-items:flex-end;
  gap:.45rem;
  background:rgba(255,255,255,.07);
  border:1px solid var(--border);
  border-radius:20px;
  padding:.65rem .65rem .65rem 1.1rem;
  transition:border-color .25s,box-shadow .25s;
  box-shadow:0 8px 32px rgba(0,0,0,.3);
}}
.input-bar:focus-within{{
  border-color:rgba(139,92,246,.6);
  box-shadow:0 0 0 3px rgba(139,92,246,.15), 0 8px 32px rgba(0,0,0,.3);
}}
.input-text{{
  flex:1;background:none;border:none;outline:none;
  color:var(--text);font-family:'DM Sans',sans-serif;font-size:.95rem;line-height:1.5;
  resize:none;min-height:24px;max-height:130px;overflow-y:auto;padding:0;
  scrollbar-width:none;
}}
.input-text::placeholder{{color:var(--muted);}}
.input-text::-webkit-scrollbar{{display:none;}}
.input-actions{{display:flex;align-items:center;gap:.35rem;flex-shrink:0;}}
.mic-btn{{
  width:38px;height:38px;border-radius:11px;
  display:flex;align-items:center;justify-content:center;
  border:none;cursor:pointer;font-size:1.1rem;
  color:var(--muted);background:transparent;
  transition:all .2s;
}}
.mic-btn:hover{{background:var(--glass2);color:var(--purple);}}
.mic-btn.rec{{color:#f87171;background:rgba(248,113,113,.15);animation:micPulse 1.2s infinite;}}
@keyframes micPulse{{
  0%,100%{{box-shadow:0 0 0 0 rgba(248,113,113,.4);}}
  50%{{box-shadow:0 0 0 8px rgba(248,113,113,0);}}
}}
.send-btn{{
  width:38px;height:38px;border-radius:11px;
  display:flex;align-items:center;justify-content:center;
  border:none;cursor:pointer;
  background:linear-gradient(135deg,var(--purple),var(--blue));
  color:#fff;font-size:1rem;
  box-shadow:0 3px 12px rgba(139,92,246,.4);
  transition:all .22s;flex-shrink:0;
}}
.send-btn:hover{{transform:scale(1.08);box-shadow:0 5px 18px rgba(139,92,246,.6);}}
.send-btn:disabled{{opacity:.35;cursor:not-allowed;transform:none;}}
.mic-status{{text-align:center;font-size:.76rem;color:#f87171;height:16px;margin-top:.4rem;opacity:0;transition:opacity .3s;}}
.mic-status.on{{opacity:1;}}

/* Suggestion pills */
.pills{{
  display:flex;flex-wrap:wrap;gap:.5rem;
  justify-content:center;
  margin-top:1rem;
  animation:riseUp .6s ease .35s both;
}}
.pill{{
  padding:.42rem .9rem;
  background:var(--glass);border:1px solid var(--border);
  border-radius:50px;font-size:.8rem;color:var(--muted);
  cursor:pointer;transition:all .2s;white-space:nowrap;
}}
.pill:hover{{background:var(--glass2);color:var(--text);border-color:var(--purple);transform:translateY(-1px);}}

/* ── CHAT STATE ── */
.chat-view{{
  flex:1;
  display:flex;
  flex-direction:column;
  overflow:hidden;
  opacity:0;
  pointer-events:none;
  position:absolute;
  inset:0;
  transition:opacity .4s ease;
}}
.chat-view.visible{{
  opacity:1;
  pointer-events:all;
  position:relative;
}}

/* Stats bar at top of chat */
.stats-bar{{
  display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap;
  padding:.75rem 1.5rem .5rem;
  flex-shrink:0;
}}
.stat-chip{{
  display:flex;align-items:center;gap:.45rem;
  padding:.38rem .85rem;border-radius:50px;
  background:var(--glass);border:1px solid var(--border);
  font-size:.78rem;color:var(--muted);
}}
.stat-chip b{{font-family:'Syne',sans-serif;font-weight:700;color:var(--text);}}

/* Scrollable message area */
.msgs-wrap{{
  flex:1;
  overflow-y:auto;
  overflow-x:hidden;
  padding:.75rem 1rem 0;
  display:flex;
  flex-direction:column;
  /* Push content to bottom */
  justify-content:flex-end;
  scrollbar-width:thin;
  scrollbar-color:rgba(139,92,246,.4) transparent;
}}
.msgs-wrap::-webkit-scrollbar{{width:4px;}}
.msgs-wrap::-webkit-scrollbar-thumb{{background:rgba(139,92,246,.4);border-radius:4px;}}
.msgs-inner{{
  display:flex;flex-direction:column;gap:.85rem;
  max-width:720px;width:100%;margin:0 auto;
  padding-bottom:.5rem;
}}

.msg{{display:flex;gap:.65rem;align-items:flex-start;animation:msgIn .32s ease;}}
@keyframes msgIn{{from{{opacity:0;transform:translateY(10px);}}to{{opacity:1;transform:translateY(0);}}}}
.msg.user{{flex-direction:row-reverse;}}
.msg-av{{width:30px;height:30px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;}}
.msg-av.ai{{background:linear-gradient(135deg,var(--purple),var(--blue));}}
.msg-av.usr{{background:linear-gradient(135deg,var(--cyan),var(--purple));}}
.bubble{{max-width:75%;padding:.7rem 1rem;border-radius:16px;font-size:.92rem;line-height:1.55;word-break:break-word;}}
.msg.ai  .bubble{{background:var(--glass);border:1px solid var(--border);border-top-left-radius:4px;}}
.msg.user .bubble{{background:linear-gradient(135deg,var(--purple),var(--blue));border-top-right-radius:4px;}}

/* Typing */
.typing{{display:flex;gap:5px;align-items:center;padding:.2rem 0;}}
.typing span{{width:7px;height:7px;border-radius:50%;background:var(--purple);animation:bounce 1.2s infinite;}}
.typing span:nth-child(2){{animation-delay:.2s;background:var(--blue);}}
.typing span:nth-child(3){{animation-delay:.4s;background:var(--cyan);}}
@keyframes bounce{{0%,80%,100%{{transform:translateY(0);}}40%{{transform:translateY(-8px);}}}}

/* ── BOTTOM INPUT (chat state) ── */
.bottom-bar{{
  flex-shrink:0;
  padding:.6rem 1rem .85rem;
  background:linear-gradient(to top, rgba(10,1,24,1) 70%, transparent);
}}
.bottom-inner{{
  max-width:720px;
  margin:0 auto;
}}
.bottom-pills{{
  display:flex;flex-wrap:wrap;gap:.45rem;
  margin-bottom:.55rem;
  justify-content:center;
}}

/* ── TRANSITION ANIMATION ── */
/* When switching: a brief "swoosh" effect on the input */
.input-bar.swoosh{{
  animation:swooshDown .45s cubic-bezier(.4,0,.2,1) both;
}}
@keyframes swooshDown{{
  0%{{transform:translateY(0) scale(1); opacity:1;}}
  40%{{transform:translateY(10px) scale(.98); opacity:.6;}}
  100%{{transform:translateY(0) scale(1); opacity:1;}}
}}

/* ── RESPONSIVE ── */
@media(max-width:640px){{
  .navbar{{padding:0 1rem;}}
  .uname{{display:none;}}
  .hero-greeting{{font-size:1.5rem;}}
  .center-box{{max-width:100%;}}
  .stats-bar{{display:none;}}
  .msgs-wrap{{padding:.5rem .6rem 0;}}
  .bottom-bar{{padding:.5rem .6rem .7rem;}}
  .bottom-pills{{display:none;}}
}}
</style>
</head>
<body>
<div class="orbs">
  <div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
</div>

<!-- NAVBAR -->
<nav class="navbar">
  <div class="nav-inner">
    <a class="brand" href="#">
      <div class="brand-icon">🧠</div>
      MindWatch
    </a>
    <div class="user-chip">
      <div class="av-wrap">
        {"<img class='av-img' src='" + user_picture + "' alt='avatar' onerror=\"this.style.display='none';document.getElementById('avf').style.display='flex';\"/>" if user_picture else ""}
        <div class="av-fallback" id="avf" style="{'display:none' if user_picture else 'display:flex'}">
          {avatar_letter}
        </div>
        <div class="online-dot"></div>
      </div>
      <span class="uname">{user_name}</span>
      <span class="chevron">▾</span>
      <div class="dropdown">
        <div class="dd-email">{user_email}</div>
        <button class="dd-item">👤 &nbsp;Profile</button>
        <button class="dd-item">⚙️ &nbsp;Settings</button>
        <button class="dd-item">📊 &nbsp;My History</button>
        <button class="dd-item danger" onclick="doLogout()">🚪 &nbsp;Sign out</button>
      </div>
    </div>
  </div>
</nav>

<!-- SHELL -->
<div class="shell">

  <!-- ① CENTERED STATE -->
  <div class="centered-view" id="centeredView">
    <div class="hero-icon">🧠</div>
    <div class="hero-greeting">Hey, {first_name} 👋</div>
    <div class="hero-sub">How are you feeling today? Share anything on your mind.</div>

    <div class="center-box">
      <div class="input-bar" id="centerBar">
        <textarea class="input-text" id="centerInp"
          placeholder="Share how you're feeling…"
          rows="1"
          oninput="resize(this);toggleSend('centerInp','centerSend');"
          onkeydown="handleKey(event,'centerInp')"></textarea>
        <div class="input-actions">
          <button class="mic-btn" id="micBtn" title="Voice input" onclick="toggleMic('centerInp','centerSend')">🎙️</button>
          <button class="send-btn" id="centerSend" onclick="sendFirst()" disabled>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
            </svg>
          </button>
        </div>
      </div>
      <div class="mic-status" id="micStatus">🔴 Listening… speak now</div>

      <div class="pills" id="centerPills">
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">😔 Feeling anxious</div>
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">😊 Having a good day</div>
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">😴 Feeling tired</div>
        <div class="pill" onclick="usePill(this,'centerInp','centerSend')">😤 Stressed out</div>
      </div>
    </div>
  </div>

  <!-- ② CHAT STATE -->
  <div class="chat-view" id="chatView">

    <div class="stats-bar">
      <div class="stat-chip">🔥 <b>7</b>&nbsp;day streak</div>
      <div class="stat-chip">💬 <b>24</b>&nbsp;check-ins</div>
      <div class="stat-chip">✨ <b>Good</b>&nbsp;avg mood</div>
    </div>

    <div class="msgs-wrap" id="msgsWrap">
      <div class="msgs-inner" id="msgs"></div>
    </div>

    <div class="bottom-bar">
      <div class="bottom-inner">
        <div class="bottom-pills" id="bottomPills">
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">😔 Anxious</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">😊 Good day</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">😴 Tired</div>
          <div class="pill" onclick="usePill(this,'bottomInp','bottomSend')">😤 Stressed</div>
        </div>
        <div class="input-bar" id="bottomBar">
          <textarea class="input-text" id="bottomInp"
            placeholder="Share how you're feeling…"
            rows="1"
            oninput="resize(this);toggleSend('bottomInp','bottomSend');"
            onkeydown="handleKey(event,'bottomInp')"></textarea>
          <div class="input-actions">
            <button class="mic-btn" id="micBtn2" title="Voice input" onclick="toggleMic('bottomInp','bottomSend')">🎙️</button>
            <button class="send-btn" id="bottomSend" onclick="sendMsg()" disabled>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

</div><!-- /shell -->

<script>
/* ── Helpers ── */
function resize(el){{
  el.style.height='auto';
  el.style.height=Math.min(el.scrollHeight,130)+'px';
}}
function toggleSend(inpId, btnId){{
  document.getElementById(btnId).disabled =
    !document.getElementById(inpId).value.trim();
}}
function handleKey(e, inpId){{
  if(e.key==='Enter'&&!e.shiftKey){{
    e.preventDefault();
    if(inpId==='centerInp') sendFirst(); else sendMsg();
  }}
}}
function usePill(el, inpId, btnId){{
  const inp=document.getElementById(inpId);
  inp.value=el.textContent.trim();
  resize(inp); toggleSend(inpId,btnId); inp.focus();
}}

/* ── State switch: centered → chat ── */
let chatStarted = false;

function switchToChatView(){{
  if(chatStarted) return;
  chatStarted = true;

  const cv = document.getElementById('centeredView');
  const chat = document.getElementById('chatView');

  // Fade out centered
  cv.classList.add('hidden');

  // Short delay then show chat (matches transition duration)
  setTimeout(()=>{{
    chat.classList.add('visible');
    // Add swoosh to bottom bar
    document.getElementById('bottomBar').classList.add('swoosh');
    setTimeout(()=>document.getElementById('bottomBar').classList.remove('swoosh'), 500);
  }}, 300);
}}

/* ── First send (from center box) ── */
function sendFirst(){{
  const inp = document.getElementById('centerInp');
  const text = inp.value.trim();
  if(!text) return;

  switchToChatView();

  // After chat view is visible, add the message
  setTimeout(()=>{{
    addMsg(text,'user');
    showTyping();
    setTimeout(()=>{{
      removeTyping();
      addMsg(reply(text),'ai');
    }}, 1400+Math.random()*700);
    // Focus bottom input
    document.getElementById('bottomInp').focus();
  }}, 380);
}}

/* ── Subsequent sends (from bottom bar) ── */
function sendMsg(){{
  const inp=document.getElementById('bottomInp');
  const text=inp.value.trim();
  if(!text) return;
  addMsg(text,'user');
  inp.value=''; inp.style.height='auto';
  document.getElementById('bottomSend').disabled=true;
  hidePills();
  showTyping();
  setTimeout(()=>{{removeTyping();addMsg(reply(text),'ai');}},1400+Math.random()*700);
}}

function hidePills(){{
  const p=document.getElementById('bottomPills');
  if(p){{ p.style.opacity='0'; p.style.pointerEvents='none'; p.style.height='0'; p.style.marginBottom='0'; }}
}}

/* ── DOM helpers ── */
function addMsg(text, role){{
  const c=document.getElementById('msgs');
  const d=document.createElement('div');
  d.className='msg '+role;
  const av = role==='ai'
    ? '<div class="msg-av ai">🧠</div>'
    : '<div class="msg-av usr">{avatar_letter}</div>';
  d.innerHTML = av+'<div class="bubble">'+esc(text)+'</div>';
  c.appendChild(d);
  scrollBottom();
}}
function showTyping(){{
  const c=document.getElementById('msgs');
  const d=document.createElement('div');
  d.className='msg ai'; d.id='typing';
  d.innerHTML='<div class="msg-av ai">🧠</div><div class="bubble"><div class="typing"><span></span><span></span><span></span></div></div>';
  c.appendChild(d); scrollBottom();
}}
function removeTyping(){{const e=document.getElementById('typing');if(e)e.remove();}}
function scrollBottom(){{
  const w=document.getElementById('msgsWrap');
  if(w) w.scrollTop=w.scrollHeight;
}}
function esc(s){{
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}}

/* ── AI replies ── */
function reply(t){{
  t=t.toLowerCase();
  if(/(anxious|anxiety|worried|nervous)/.test(t))
    return "I hear you — anxiety can feel really overwhelming. 💙 Take a slow breath with me. Can you tell me what's triggering it? Sometimes naming it out loud helps.";
  if(/(happy|great|wonderful|amazing|good day|excited)/.test(t))
    return "That's so great to hear! 🌟 Savoring positive moments really matters. What's been the highlight of your day?";
  if(/(sad|down|depressed|unhappy|miserable|lonely)/.test(t))
    return "I'm sorry you're feeling that way. 💜 You're not alone and it's okay to feel sad. Would you like to talk about what's weighing on you?";
  if(/(tired|exhausted|sleepy|no energy|fatigue)/.test(t))
    return "Rest is so important for mental health. 😴 Have you been sleeping okay? Fatigue can make everything feel heavier than it really is.";
  if(/(stress|overwhelm|too much|busy|pressure|work)/.test(t))
    return "It sounds like a lot is on your plate. 🌿 What's the biggest thing weighing on you right now? Let's try to break it down together.";
  if(/(angry|frustrated|mad|furious|irritated|annoyed)/.test(t))
    return "Those feelings are completely valid. 🔥 Anger usually points to something important. What happened that led you here?";
  return "Thank you for sharing that with me. 🧠 I'm here to help you reflect and understand your feelings. Can you tell me a bit more about what's going on?";
}}

/* ── Microphone ── */
let recog=null, isRec=false, activeMicInp='', activeMicBtn='';
function toggleMic(inpId, btnId){{
  if(!('webkitSpeechRecognition' in window)&&!('SpeechRecognition' in window)){{
    alert('Voice input needs Chrome or Edge browser.'); return;
  }}
  activeMicInp=inpId; activeMicBtn=btnId;
  isRec ? stopMic() : startMic(inpId, btnId);
}}
function startMic(inpId, btnId){{
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  recog=new SR();
  recog.continuous=false; recog.interimResults=true; recog.lang='en-US';
  recog.onstart=()=>{{
    isRec=true;
    document.getElementById(btnId==='centerSend'?'micBtn':'micBtn2').classList.add('rec');
    document.getElementById('micStatus').classList.add('on');
  }};
  recog.onresult=(e)=>{{
    let tr='';
    for(let i=e.resultIndex;i<e.results.length;i++) tr+=e.results[i][0].transcript;
    const inp=document.getElementById(inpId);
    inp.value=tr; resize(inp); toggleSend(inpId,btnId);
  }};
  recog.onend=()=>stopMic();
  recog.onerror=()=>stopMic();
  recog.start();
}}
function stopMic(){{
  if(recog){{recog.stop();recog=null;}}
  isRec=false;
  document.getElementById('micBtn').classList.remove('rec');
  document.getElementById('micBtn2').classList.remove('rec');
  document.getElementById('micStatus').classList.remove('on');
}}

/* ── Logout ── */
function doLogout(){{
  window.parent.location.href='http://localhost:8501/?logout=1';
}}
</script>
</body>
</html>"""

    components.html(html, height=820, scrolling=False)