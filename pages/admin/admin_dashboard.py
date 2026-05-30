"""
MindWatch – Admin Dashboard
Professional AI monitoring control panel for administrators.
Pages: pages/admin/admin_dashboard.py
"""

import streamlit as st
import streamlit.components.v1 as components


def show():

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

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>MindWatch – Admin Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}

:root{
  /* MindWatch core palette */
  --purple:#8b5cf6; --blue:#3b82f6; --cyan:#06b6d4; --pink:#ec4899;
  /* Admin accent overrides */
  --admin-blue:#4a9eff;
  --admin-purple:#6b5fff;
  --admin-cyan:#00d4ff;
  --admin-green:#00e5a0;
  --admin-amber:#ffb830;
  --admin-red:#ff4d6d;
  /* Glass system */
  --glass:rgba(255,255,255,0.04);
  --glass2:rgba(255,255,255,0.08);
  --glass3:rgba(255,255,255,0.12);
  --border:rgba(255,255,255,0.08);
  --border2:rgba(74,158,255,0.20);
  --text:#f0f4ff;
  --muted:rgba(240,244,255,0.50);
  --muted2:rgba(240,244,255,0.30);
  --navbar-h:62px;
}

html{scroll-behavior:smooth;}
body{
  font-family:'DM Sans',sans-serif;
  color:var(--text);
  background:
    radial-gradient(ellipse 80% 60% at 10% 0%,   rgba(74,158,255,0.12) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 90% 100%,  rgba(107,95,255,0.14) 0%, transparent 55%),
    radial-gradient(ellipse 50% 40% at 50% 50%,   rgba(0,212,255,0.05)  0%, transparent 70%),
    linear-gradient(160deg,#000308 0%,#030714 25%,#060b1a 55%,#04061a 80%,#020010 100%);
  min-height:100vh;
  overflow-x:hidden;
}

/* ── GRID NOISE TEXTURE ── */
body::before{
  content:'';
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(74,158,255,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(74,158,255,0.025) 1px, transparent 1px);
  background-size:48px 48px;
  mask-image:radial-gradient(ellipse 80% 80% at 50% 20%, black 40%, transparent 100%);
}

/* ── AMBIENT ORBS ── */
.orbs{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none;}
.orb{position:absolute;border-radius:50%;filter:blur(90px);opacity:.15;animation:drift 28s infinite ease-in-out;}
.o1{width:600px;height:600px;background:radial-gradient(circle,var(--admin-blue),transparent 70%);top:-15%;left:-10%;animation-duration:32s;}
.o2{width:480px;height:480px;background:radial-gradient(circle,var(--admin-purple),transparent 70%);bottom:-10%;right:-8%;animation-delay:10s;animation-duration:26s;}
.o3{width:300px;height:300px;background:radial-gradient(circle,var(--admin-cyan),transparent 70%);top:40%;left:42%;opacity:.08;animation-delay:18s;animation-duration:22s;}
@keyframes drift{
  0%,100%{transform:translate(0,0) scale(1);}
  25%{transform:translate(50px,-50px) scale(1.08);}
  50%{transform:translate(-35px,55px) scale(.94);}
  75%{transform:translate(45px,30px) scale(1.05);}
}

/* ══════════════════════════════════════════
   NAVBAR
   ══════════════════════════════════════════ */
.navbar{
  position:fixed;top:0;left:0;right:0;z-index:999;
  height:var(--navbar-h);
  background:rgba(3,7,20,.92);
  backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);
  border-bottom:1px solid rgba(74,158,255,0.15);
  padding:0 2rem;
  animation:navSlideDown .55s cubic-bezier(.22,.68,0,1.2);
}
@keyframes navSlideDown{from{opacity:0;transform:translateY(-100%);}to{opacity:1;transform:translateY(0);}}

.nav-inner{
  height:100%;max-width:1400px;margin:0 auto;
  display:flex;align-items:center;justify-content:space-between;
}

.brand{
  display:flex;align-items:center;gap:.65rem;
  font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:800;
  color:var(--text);text-decoration:none;
}
.brand-icon{
  width:36px;height:36px;border-radius:10px;
  background:linear-gradient(135deg,var(--admin-blue),var(--admin-purple));
  display:flex;align-items:center;justify-content:center;font-size:1.15rem;
  box-shadow:0 4px 18px rgba(74,158,255,.4);
  animation:pulseLogo 3.5s ease-in-out infinite;
}
@keyframes pulseLogo{
  0%,100%{box-shadow:0 4px 18px rgba(74,158,255,.4);}
  50%{box-shadow:0 4px 28px rgba(107,95,255,.6);}
}

.admin-badge{
  font-size:.65rem;font-weight:700;letter-spacing:.1em;
  font-family:'JetBrains Mono',monospace;
  color:var(--admin-blue);
  background:rgba(74,158,255,.12);
  border:1px solid rgba(74,158,255,.25);
  border-radius:4px;padding:.18rem .5rem;
  text-transform:uppercase;
}

.nav-right{display:flex;align-items:center;gap:1rem;}

.nav-status{
  display:flex;align-items:center;gap:.5rem;
  font-size:.78rem;color:var(--muted);
  font-family:'JetBrains Mono',monospace;
}
.status-dot{
  width:7px;height:7px;border-radius:50%;
  background:var(--admin-green);
  box-shadow:0 0 8px var(--admin-green);
  animation:blink 2.2s infinite;
}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:.35;}}

.admin-chip{
  display:flex;align-items:center;gap:.6rem;
  padding:.32rem .8rem .32rem .4rem;
  background:rgba(74,158,255,.07);
  border:1px solid rgba(74,158,255,.2);
  border-radius:50px;cursor:pointer;
  transition:background .25s,border-color .25s;
  animation:fadeUp .7s ease .3s both;
  position:relative;
}
.admin-chip:hover{background:rgba(74,158,255,.13);border-color:rgba(74,158,255,.4);}
@keyframes fadeUp{from{opacity:0;transform:scale(.9);}to{opacity:1;transform:scale(1);}}

.av-admin{
  width:32px;height:32px;border-radius:50%;
  background:linear-gradient(135deg,var(--admin-blue),var(--admin-purple));
  display:flex;align-items:center;justify-content:center;
  font-size:.85rem;font-weight:700;
  box-shadow:0 0 0 2px rgba(74,158,255,.4);
}
.chip-label{
  font-family:'Syne',sans-serif;font-size:.82rem;font-weight:700;
  color:var(--text);
}
.chip-chevron{color:var(--muted);font-size:.65rem;transition:transform .2s;}
.admin-chip:hover .chip-chevron{transform:rotate(180deg);}

.admin-dropdown{
  position:absolute;top:calc(100% + 10px);right:0;
  background:rgba(3,7,20,.98);backdrop-filter:blur(24px);
  border:1px solid rgba(74,158,255,.18);border-radius:14px;
  padding:.5rem;min-width:210px;
  opacity:0;pointer-events:none;transform:translateY(-8px);
  transition:opacity .22s,transform .22s;
  box-shadow:0 20px 56px rgba(0,0,0,.6),0 0 0 1px rgba(74,158,255,.05);
}
.admin-chip:hover .admin-dropdown{opacity:1;pointer-events:all;transform:translateY(0);}
.dd-role{
  padding:.5rem .75rem .7rem;
  font-size:.73rem;font-family:'JetBrains Mono',monospace;
  color:var(--admin-blue);border-bottom:1px solid var(--border);margin-bottom:.4rem;
  letter-spacing:.05em;
}
.dd-item{
  display:flex;align-items:center;gap:.6rem;
  padding:.5rem .75rem;border-radius:8px;
  color:var(--text);font-size:.85rem;
  cursor:pointer;transition:background .18s;
  border:none;background:none;width:100%;text-align:left;
}
.dd-item:hover{background:var(--glass2);}
.dd-item.danger{color:#ff4d6d;}
.dd-item.danger:hover{background:rgba(255,77,109,.1);}

/* ══════════════════════════════════════════
   PAGE SHELL
   ══════════════════════════════════════════ */
.page{
  position:relative;z-index:1;
  padding-top:calc(var(--navbar-h) + 2.5rem);
  padding-bottom:4rem;
  max-width:1400px;
  margin:0 auto;
  padding-left:2rem;
  padding-right:2rem;
}

/* ══════════════════════════════════════════
   SECTION 1 – WELCOME HEADER
   ══════════════════════════════════════════ */
.welcome-section{
  margin-bottom:2.5rem;
  opacity:0;
  transform:translateY(-18px);
  animation:headerReveal .65s cubic-bezier(.22,.68,0,1) .15s forwards;
}
@keyframes headerReveal{
  to{opacity:1;transform:translateY(0);}
}

.welcome-glass{
  position:relative;
  overflow:hidden;
  background:var(--glass);
  border:1px solid var(--border2);
  border-radius:20px;
  padding:2rem 2.5rem;
  display:flex;align-items:center;justify-content:space-between;gap:2rem;
  flex-wrap:wrap;
  box-shadow:
    0 0 0 1px rgba(74,158,255,.04),
    inset 0 1px 0 rgba(255,255,255,.05),
    0 8px 32px rgba(0,0,0,.3);
}
.welcome-glass::before{
  content:'';
  position:absolute;
  top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(74,158,255,.5),transparent);
}
.welcome-glass::after{
  content:'';
  position:absolute;
  inset:0;
  background:radial-gradient(ellipse 60% 80% at 0% 50%,rgba(74,158,255,.06),transparent);
  pointer-events:none;
}

.welcome-left{flex:1;min-width:220px;position:relative;z-index:1;}

.welcome-eyebrow{
  display:flex;align-items:center;gap:.5rem;
  margin-bottom:.6rem;
  font-size:.72rem;font-weight:600;letter-spacing:.12em;
  font-family:'JetBrains Mono',monospace;
  color:var(--admin-blue);text-transform:uppercase;
}
.eyebrow-line{width:24px;height:1px;background:var(--admin-blue);opacity:.6;}

.welcome-title{
  font-family:'Syne',sans-serif;
  font-size:clamp(1.6rem,3vw,2.2rem);
  font-weight:800;
  background:linear-gradient(120deg,#fff 0%,var(--admin-blue) 55%,var(--admin-cyan) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  line-height:1.18;
  margin-bottom:.4rem;
}
.welcome-sub{
  color:var(--muted);
  font-size:.92rem;
  max-width:420px;
}

.welcome-right{
  display:flex;align-items:center;gap:1.2rem;
  flex-wrap:wrap;
  position:relative;z-index:1;
}

.time-block{
  text-align:right;
  font-family:'JetBrains Mono',monospace;
}
.time-val{font-size:1.5rem;font-weight:500;color:var(--text);letter-spacing:.05em;line-height:1;}
.time-date{font-size:.72rem;color:var(--muted);margin-top:.2rem;}

.sys-pill{
  display:flex;align-items:center;gap:.5rem;
  padding:.45rem 1rem;
  background:rgba(0,229,160,.08);
  border:1px solid rgba(0,229,160,.22);
  border-radius:50px;
  font-size:.78rem;font-weight:600;
  font-family:'JetBrains Mono',monospace;
  color:var(--admin-green);
  white-space:nowrap;
}
.sys-pill-dot{
  width:6px;height:6px;border-radius:50%;
  background:var(--admin-green);
  box-shadow:0 0 6px var(--admin-green);
  animation:blink 2s infinite;
}

/* ══════════════════════════════════════════
   SECTION 2 – ANALYTICS CARDS
   ══════════════════════════════════════════ */
.section-label{
  display:flex;align-items:center;gap:.6rem;
  margin-bottom:1.2rem;
  font-size:.7rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  font-family:'JetBrains Mono',monospace;
  color:var(--muted);
}
.section-label::after{
  content:'';flex:1;height:1px;
  background:linear-gradient(90deg,var(--border),transparent);
}

.cards-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:1rem;
  margin-bottom:2.5rem;
}

.acard{
  position:relative;overflow:hidden;
  background:var(--glass);
  border:1px solid var(--border);
  border-radius:16px;
  padding:1.5rem;
  cursor:default;
  transition:border-color .3s, box-shadow .3s, transform .3s;
  /* Stagger animation set inline */
  opacity:0;transform:translateY(22px);
}
.acard.revealed{animation:cardReveal .55s cubic-bezier(.22,.68,0,1) forwards;}
@keyframes cardReveal{to{opacity:1;transform:translateY(0);}}

.acard::before{
  content:'';
  position:absolute;inset:0;
  background:radial-gradient(ellipse 80% 70% at 90% 10%, var(--card-glow,rgba(74,158,255,.06)),transparent);
  pointer-events:none;
  transition:opacity .3s;
  opacity:0;
}
.acard:hover{
  transform:translateY(-3px);
  border-color:var(--card-accent,rgba(74,158,255,.3));
  box-shadow:0 0 0 1px var(--card-accent,rgba(74,158,255,.1)),
             0 12px 32px rgba(0,0,0,.3),
             0 0 28px var(--card-shadow,rgba(74,158,255,.08));
}
.acard:hover::before{opacity:1;}

/* Card accent colors */
.acard.c-blue{--card-accent:rgba(74,158,255,.35);--card-glow:rgba(74,158,255,.08);--card-shadow:rgba(74,158,255,.1);}
.acard.c-purple{--card-accent:rgba(107,95,255,.35);--card-glow:rgba(107,95,255,.08);--card-shadow:rgba(107,95,255,.1);}
.acard.c-amber{--card-accent:rgba(255,184,48,.35);--card-glow:rgba(255,184,48,.08);--card-shadow:rgba(255,184,48,.1);}
.acard.c-green{--card-accent:rgba(0,229,160,.35);--card-glow:rgba(0,229,160,.08);--card-shadow:rgba(0,229,160,.1);}

.card-top{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:1rem;}

.card-icon-wrap{
  width:42px;height:42px;border-radius:12px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.2rem;flex-shrink:0;
}
.c-blue  .card-icon-wrap{background:rgba(74,158,255,.12);border:1px solid rgba(74,158,255,.2);}
.c-purple .card-icon-wrap{background:rgba(107,95,255,.12);border:1px solid rgba(107,95,255,.2);}
.c-amber  .card-icon-wrap{background:rgba(255,184,48,.12);border:1px solid rgba(255,184,48,.2);}
.c-green  .card-icon-wrap{background:rgba(0,229,160,.12);border:1px solid rgba(0,229,160,.2);}

.card-delta{
  font-size:.7rem;font-weight:600;
  font-family:'JetBrains Mono',monospace;
  padding:.2rem .5rem;border-radius:6px;
  white-space:nowrap;
}
.delta-up{color:var(--admin-green);background:rgba(0,229,160,.1);}
.delta-down{color:var(--admin-red);background:rgba(255,77,109,.1);}
.delta-stable{color:var(--admin-amber);background:rgba(255,184,48,.1);}

.card-value{
  font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;
  color:var(--text);line-height:1;margin-bottom:.3rem;
}
.card-label{font-size:.82rem;color:var(--muted);font-weight:500;margin-bottom:1rem;}

.card-bar-track{height:3px;background:rgba(255,255,255,.06);border-radius:2px;overflow:hidden;}
.card-bar-fill{
  height:100%;border-radius:2px;
  transition:width 1.2s cubic-bezier(.22,.68,0,1);
  width:0%;
}
.c-blue  .card-bar-fill{background:linear-gradient(90deg,var(--admin-blue),var(--admin-cyan));}
.c-purple .card-bar-fill{background:linear-gradient(90deg,var(--admin-purple),var(--admin-blue));}
.c-amber  .card-bar-fill{background:linear-gradient(90deg,var(--admin-amber),#ffd700);}
.c-green  .card-bar-fill{background:linear-gradient(90deg,var(--admin-green),#06f7d2);}

/* ══════════════════════════════════════════
   SECTION 3 – MONITORING PANELS
   ══════════════════════════════════════════ */
.monitor-grid{
  display:grid;
  grid-template-columns:1fr 380px;
  gap:1.25rem;
  margin-bottom:2.5rem;
}
@media(max-width:1024px){.monitor-grid{grid-template-columns:1fr;}}

.glass-panel{
  position:relative;overflow:hidden;
  background:var(--glass);
  border:1px solid var(--border);
  border-radius:18px;
  padding:1.6rem;
  opacity:0;transform:translateY(24px);
}
.glass-panel.revealed{animation:cardReveal .6s cubic-bezier(.22,.68,0,1) forwards;}
.glass-panel::before{
  content:'';position:absolute;
  top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(74,158,255,.35),transparent);
}

.panel-header{
  display:flex;align-items:center;justify-content:space-between;
  margin-bottom:1.4rem;
  flex-wrap:wrap;gap:.8rem;
}
.panel-title{
  font-family:'Syne',sans-serif;font-weight:700;font-size:1rem;color:var(--text);
}
.panel-sub{font-size:.78rem;color:var(--muted);margin-top:.15rem;}

.panel-tag{
  font-size:.68rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
  font-family:'JetBrains Mono',monospace;
  padding:.22rem .65rem;border-radius:5px;
}
.tag-live{color:var(--admin-green);background:rgba(0,229,160,.1);border:1px solid rgba(0,229,160,.2);}
.tag-ai{color:var(--admin-blue);background:rgba(74,158,255,.1);border:1px solid rgba(74,158,255,.2);}
.tag-warn{color:var(--admin-amber);background:rgba(255,184,48,.1);border:1px solid rgba(255,184,48,.2);}

/* ── ACTIVITY LOG ── */
.log-list{display:flex;flex-direction:column;gap:.6rem;}
.log-item{
  display:flex;align-items:flex-start;gap:.9rem;
  padding:.75rem 1rem;
  background:rgba(255,255,255,.025);
  border:1px solid var(--border);
  border-radius:10px;
  transition:background .2s,border-color .2s;
}
.log-item:hover{background:rgba(74,158,255,.05);border-color:rgba(74,158,255,.18);}

.log-dot{
  width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:.25rem;
}
.ld-green{background:var(--admin-green);box-shadow:0 0 8px var(--admin-green);}
.ld-blue{background:var(--admin-blue);box-shadow:0 0 8px var(--admin-blue);}
.ld-amber{background:var(--admin-amber);box-shadow:0 0 8px var(--admin-amber);}
.ld-red{background:var(--admin-red);box-shadow:0 0 8px var(--admin-red);}
.ld-purple{background:var(--admin-purple);box-shadow:0 0 8px var(--admin-purple);}

.log-content{flex:1;min-width:0;}
.log-msg{font-size:.84rem;color:var(--text);line-height:1.4;}
.log-meta{
  display:flex;align-items:center;gap:.6rem;margin-top:.2rem;
  font-size:.7rem;color:var(--muted);font-family:'JetBrains Mono',monospace;
}
.log-uid{
  padding:.1rem .4rem;background:rgba(255,255,255,.05);
  border-radius:4px;font-size:.65rem;
}
.log-time{margin-left:auto;white-space:nowrap;}

/* ── AI STATUS PANEL ── */
.ai-module{
  display:flex;flex-direction:column;gap:.75rem;
}
.ai-row{
  display:flex;align-items:center;justify-content:space-between;
  padding:.85rem 1rem;
  background:rgba(255,255,255,.025);
  border:1px solid var(--border);
  border-radius:10px;
  gap:1rem;
}
.ai-row-left{display:flex;align-items:center;gap:.75rem;}
.ai-icon{font-size:1.1rem;width:32px;text-align:center;}
.ai-label{font-size:.83rem;color:var(--text);font-weight:500;}
.ai-sub{font-size:.7rem;color:var(--muted);}

.status-badge{
  font-size:.68rem;font-weight:600;
  font-family:'JetBrains Mono',monospace;
  padding:.2rem .55rem;border-radius:5px;
  white-space:nowrap;
  letter-spacing:.05em;
}
.sb-online{color:var(--admin-green);background:rgba(0,229,160,.1);border:1px solid rgba(0,229,160,.2);}
.sb-idle{color:var(--admin-amber);background:rgba(255,184,48,.1);border:1px solid rgba(255,184,48,.2);}
.sb-alert{color:var(--admin-red);background:rgba(255,77,109,.1);border:1px solid rgba(255,77,109,.2);}

/* ── AI PROGRESS BARS ── */
.ai-perf-section{margin-top:1.2rem;}
.perf-row{display:flex;flex-direction:column;gap:.3rem;margin-bottom:.85rem;}
.perf-top{display:flex;justify-content:space-between;align-items:center;}
.perf-name{font-size:.78rem;color:var(--muted);}
.perf-val{font-size:.75rem;font-family:'JetBrains Mono',monospace;color:var(--text);}
.perf-track{height:4px;background:rgba(255,255,255,.06);border-radius:3px;overflow:hidden;}
.perf-fill{
  height:100%;border-radius:3px;
  transition:width 1.4s cubic-bezier(.22,.68,0,1);
  width:0%;
}
.pf-blue{background:linear-gradient(90deg,var(--admin-blue),var(--admin-cyan));}
.pf-purple{background:linear-gradient(90deg,var(--admin-purple),var(--admin-blue));}
.pf-green{background:linear-gradient(90deg,var(--admin-green),#06f7d2);}

/* ══════════════════════════════════════════
   SECTION 4 – BOTTOM ROW PANELS
   ══════════════════════════════════════════ */
.bottom-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:1.25rem;
}
@media(max-width:768px){.bottom-grid{grid-template-columns:1fr;}}

/* User table */
.user-table{width:100%;border-collapse:collapse;}
.user-table th{
  font-size:.68rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
  font-family:'JetBrains Mono',monospace;color:var(--muted);
  padding:.5rem .75rem;border-bottom:1px solid var(--border);
  text-align:left;
}
.user-table td{
  padding:.7rem .75rem;font-size:.82rem;color:var(--text);
  border-bottom:1px solid rgba(255,255,255,.03);
  vertical-align:middle;
}
.user-table tr:last-child td{border-bottom:none;}
.user-table tr:hover td{background:rgba(74,158,255,.04);}

.u-av{
  width:28px;height:28px;border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;
  font-size:.75rem;font-weight:700;
  margin-right:.5rem;vertical-align:middle;flex-shrink:0;
}
.uav1{background:linear-gradient(135deg,#4a9eff,#6b5fff);}
.uav2{background:linear-gradient(135deg,#ff4d6d,#ec4899);}
.uav3{background:linear-gradient(135deg,#00e5a0,#06b6d4);}
.uav4{background:linear-gradient(135deg,#ffb830,#ff4d6d);}
.uav5{background:linear-gradient(135deg,#8b5cf6,#ec4899);}

.mood-chip{
  display:inline-block;padding:.15rem .5rem;
  border-radius:5px;font-size:.72rem;font-weight:600;
  font-family:'JetBrains Mono',monospace;
}
.mood-stable{color:#00e5a0;background:rgba(0,229,160,.1);}
.mood-moderate{color:#ffb830;background:rgba(255,184,48,.1);}
.mood-critical{color:#ff4d6d;background:rgba(255,77,109,.1);}
.mood-low{color:#4a9eff;background:rgba(74,158,255,.1);}

/* Alert feed */
.alert-list{display:flex;flex-direction:column;gap:.55rem;}
.alert-item{
  display:flex;align-items:center;gap:.85rem;
  padding:.7rem .9rem;
  border-radius:10px;border-left:3px solid;
  background:rgba(255,255,255,.025);
}
.alert-item.sev-high{
  border-left-color:var(--admin-red);
  background:rgba(255,77,109,.05);
}
.alert-item.sev-medium{
  border-left-color:var(--admin-amber);
  background:rgba(255,184,48,.05);
}
.alert-item.sev-low{
  border-left-color:var(--admin-blue);
  background:rgba(74,158,255,.05);
}
.alert-icon{font-size:1rem;flex-shrink:0;}
.alert-content{flex:1;min-width:0;}
.alert-msg{font-size:.82rem;color:var(--text);line-height:1.3;}
.alert-time{font-size:.68rem;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-top:.1rem;}
.alert-sev{
  font-size:.65rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  font-family:'JetBrains Mono',monospace;
  padding:.18rem .45rem;border-radius:4px;white-space:nowrap;
}
.sev-high  .alert-sev{color:var(--admin-red);background:rgba(255,77,109,.12);}
.sev-medium .alert-sev{color:var(--admin-amber);background:rgba(255,184,48,.12);}
.sev-low   .alert-sev{color:var(--admin-blue);background:rgba(74,158,255,.12);}

/* ══════════════════════════════════════════
   SCROLL ANIMATION UTILITY
   ══════════════════════════════════════════ */
.scroll-reveal{
  opacity:0;
  transform:translateY(28px);
  transition:opacity .65s cubic-bezier(.22,.68,0,1), transform .65s cubic-bezier(.22,.68,0,1);
}
.scroll-reveal.visible{opacity:1;transform:translateY(0);}

/* ══════════════════════════════════════════
   RESPONSIVE
   ══════════════════════════════════════════ */
@media(max-width:768px){
  .page{padding-left:1rem;padding-right:1rem;padding-top:calc(var(--navbar-h) + 1.5rem);}
  .welcome-glass{padding:1.4rem 1.2rem;}
  .time-block{display:none;}
  .cards-grid{grid-template-columns:1fr 1fr;}
  .card-value{font-size:1.6rem;}
  .nav-status{display:none;}
}
@media(max-width:500px){
  .cards-grid{grid-template-columns:1fr;}
  .bottom-grid{grid-template-columns:1fr;}
  .chip-label{display:none;}
}

/* Scrollbar */
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-track{background:transparent;}
::-webkit-scrollbar-thumb{background:rgba(74,158,255,.3);border-radius:4px;}
</style>
</head>
<body>

<div class="orbs">
  <div class="orb o1"></div>
  <div class="orb o2"></div>
  <div class="orb o3"></div>
</div>

<!-- ══ NAVBAR ══ -->
<nav class="navbar">
  <div class="nav-inner">
    <a class="brand" href="#">
      <div class="brand-icon">🧠</div>
      MindWatch
      <span class="admin-badge">Admin</span>
    </a>

    <div class="nav-right">
      <div class="nav-status">
        <div class="status-dot"></div>
        All Systems Operational
      </div>
      <div class="admin-chip">
        <div class="av-admin">A</div>
        <span class="chip-label">Administrator</span>
        <span class="chip-chevron">▾</span>
        <div class="admin-dropdown">
          <div class="dd-role">ROLE: SUPER_ADMIN</div>
          <button class="dd-item">🛡️ &nbsp;Admin Profile</button>
          <button class="dd-item">⚙️ &nbsp;System Settings</button>
          <button class="dd-item">📋 &nbsp;Audit Logs</button>
          <button class="dd-item">🔐 &nbsp;Access Control</button>
          <button class="dd-item danger" onclick="doLogout()">🚪 &nbsp;Sign out</button>
        </div>
      </div>
    </div>
  </div>
</nav>

<!-- ══ PAGE ══ -->
<div class="page">

  <!-- ─── SECTION 1: WELCOME HEADER ─── -->
  <div class="welcome-section">
    <div class="welcome-glass">
      <div class="welcome-left">
        <div class="welcome-eyebrow">
          <div class="eyebrow-line"></div>
          Control Center
        </div>
        <div class="welcome-title">Admin Dashboard</div>
        <div class="welcome-sub">Monitor system activity, user insights, and AI performance in real time.</div>
      </div>
      <div class="welcome-right">
        <div class="time-block">
          <div class="time-val" id="clockVal">--:--</div>
          <div class="time-date" id="clockDate">Loading...</div>
        </div>
        <div class="sys-pill">
          <div class="sys-pill-dot"></div>
          System Online
        </div>
      </div>
    </div>
  </div>

  <!-- ─── SECTION 2: ANALYTICS CARDS ─── -->
  <div class="section-label scroll-reveal">Overview Metrics</div>

  <div class="cards-grid">
    <div class="acard c-blue" data-delay="0" data-bar="72">
      <div class="card-top">
        <div class="card-icon-wrap">👥</div>
        <div class="card-delta delta-up">▲ 8.4%</div>
      </div>
      <div class="card-value">12,847</div>
      <div class="card-label">Total Registered Users</div>
      <div class="card-bar-track"><div class="card-bar-fill"></div></div>
    </div>

    <div class="acard c-purple" data-delay="90" data-bar="54">
      <div class="card-top">
        <div class="card-icon-wrap">⚡</div>
        <div class="card-delta delta-up">▲ 3.1%</div>
      </div>
      <div class="card-value">1,203</div>
      <div class="card-label">Active Sessions Now</div>
      <div class="card-bar-track"><div class="card-bar-fill"></div></div>
    </div>

    <div class="acard c-amber" data-delay="180" data-bar="29">
      <div class="card-top">
        <div class="card-icon-wrap">🚨</div>
        <div class="card-delta delta-down">▼ 2.0%</div>
      </div>
      <div class="card-value">38</div>
      <div class="card-label">Emotional Alerts Today</div>
      <div class="card-bar-track"><div class="card-bar-fill"></div></div>
    </div>

    <div class="acard c-green" data-delay="270" data-bar="97">
      <div class="card-top">
        <div class="card-icon-wrap">🟢</div>
        <div class="card-delta delta-stable">● Stable</div>
      </div>
      <div class="card-value">99.7%</div>
      <div class="card-label">System Uptime (30d)</div>
      <div class="card-bar-track"><div class="card-bar-fill"></div></div>
    </div>
  </div>

  <!-- ─── SECTION 3: MONITORING ─── -->
  <div class="section-label scroll-reveal">Live Monitoring</div>

  <div class="monitor-grid">

    <!-- Activity Log -->
    <div class="glass-panel" data-delay="0">
      <div class="panel-header">
        <div>
          <div class="panel-title">System Activity Feed</div>
          <div class="panel-sub">Real-time events across all services</div>
        </div>
        <span class="panel-tag tag-live">● LIVE</span>
      </div>
      <div class="log-list">
        <div class="log-item">
          <div class="log-dot ld-green"></div>
          <div class="log-content">
            <div class="log-msg">User completed emotional check-in — mood score recorded as <strong>Positive</strong></div>
            <div class="log-meta">
              <span class="log-uid">USR-4821</span>
              <span>check-in</span>
              <span class="log-time">just now</span>
            </div>
          </div>
        </div>
        <div class="log-item">
          <div class="log-dot ld-amber"></div>
          <div class="log-content">
            <div class="log-msg">AI flagged moderate distress pattern — auto-escalation pending review</div>
            <div class="log-meta">
              <span class="log-uid">USR-3107</span>
              <span>ai-alert</span>
              <span class="log-time">2 min ago</span>
            </div>
          </div>
        </div>
        <div class="log-item">
          <div class="log-dot ld-blue"></div>
          <div class="log-content">
            <div class="log-msg">New user registration — email verified, profile created successfully</div>
            <div class="log-meta">
              <span class="log-uid">USR-9243</span>
              <span>auth</span>
              <span class="log-time">5 min ago</span>
            </div>
          </div>
        </div>
        <div class="log-item">
          <div class="log-dot ld-red"></div>
          <div class="log-content">
            <div class="log-msg">High-severity emotional alert — crisis protocol triggered, admin notified</div>
            <div class="log-meta">
              <span class="log-uid">USR-0582</span>
              <span>crisis</span>
              <span class="log-time">11 min ago</span>
            </div>
          </div>
        </div>
        <div class="log-item">
          <div class="log-dot ld-purple"></div>
          <div class="log-content">
            <div class="log-msg">AI model inference completed — response latency 240ms, within threshold</div>
            <div class="log-meta">
              <span class="log-uid">SYS-AI</span>
              <span>performance</span>
              <span class="log-time">14 min ago</span>
            </div>
          </div>
        </div>
        <div class="log-item">
          <div class="log-dot ld-green"></div>
          <div class="log-content">
            <div class="log-msg">Scheduled data backup completed — 847 MB, integrity check passed</div>
            <div class="log-meta">
              <span class="log-uid">SYS-DB</span>
              <span>backup</span>
              <span class="log-time">28 min ago</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- AI Status Panel -->
    <div class="glass-panel" data-delay="100">
      <div class="panel-header">
        <div>
          <div class="panel-title">AI Subsystem Status</div>
          <div class="panel-sub">Model health & performance</div>
        </div>
        <span class="panel-tag tag-ai">AI CORE</span>
      </div>
      <div class="ai-module">
        <div class="ai-row">
          <div class="ai-row-left">
            <div class="ai-icon">🧠</div>
            <div>
              <div class="ai-label">Emotion Engine</div>
              <div class="ai-sub">NLP · Sentiment analysis</div>
            </div>
          </div>
          <span class="status-badge sb-online">ONLINE</span>
        </div>
        <div class="ai-row">
          <div class="ai-row-left">
            <div class="ai-icon">🔍</div>
            <div>
              <div class="ai-label">Pattern Detector</div>
              <div class="ai-sub">Anomaly · Crisis detection</div>
            </div>
          </div>
          <span class="status-badge sb-online">ONLINE</span>
        </div>
        <div class="ai-row">
          <div class="ai-row-left">
            <div class="ai-icon">💬</div>
            <div>
              <div class="ai-label">Response Model</div>
              <div class="ai-sub">Chat · Empathy scoring</div>
            </div>
          </div>
          <span class="status-badge sb-online">ONLINE</span>
        </div>
        <div class="ai-row">
          <div class="ai-row-left">
            <div class="ai-icon">📊</div>
            <div>
              <div class="ai-label">Analytics Worker</div>
              <div class="ai-sub">Batch · Report generation</div>
            </div>
          </div>
          <span class="status-badge sb-idle">IDLE</span>
        </div>
      </div>

      <div class="ai-perf-section">
        <div class="section-label" style="margin-bottom:.8rem;font-size:.65rem;">Performance</div>
        <div class="perf-row">
          <div class="perf-top"><span class="perf-name">Inference Accuracy</span><span class="perf-val" id="pv1">—</span></div>
          <div class="perf-track"><div class="perf-fill pf-blue" id="pf1"></div></div>
        </div>
        <div class="perf-row">
          <div class="perf-top"><span class="perf-name">Response Throughput</span><span class="perf-val" id="pv2">—</span></div>
          <div class="perf-track"><div class="perf-fill pf-purple" id="pf2"></div></div>
        </div>
        <div class="perf-row">
          <div class="perf-top"><span class="perf-name">Uptime Reliability</span><span class="perf-val" id="pv3">—</span></div>
          <div class="perf-track"><div class="perf-fill pf-green" id="pf3"></div></div>
        </div>
      </div>
    </div>

  </div>

  <!-- ─── SECTION 4: BOTTOM ROW ─── -->
  <div class="section-label scroll-reveal">Users & Alerts</div>

  <div class="bottom-grid">

    <!-- Recent Users -->
    <div class="glass-panel" data-delay="0">
      <div class="panel-header">
        <div>
          <div class="panel-title">Recent User Activity</div>
          <div class="panel-sub">Latest mood submissions</div>
        </div>
        <span class="panel-tag tag-live">LIVE</span>
      </div>
      <table class="user-table">
        <thead>
          <tr>
            <th>User</th>
            <th>Mood</th>
            <th>Sessions</th>
            <th>Last Active</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="u-av uav1">S</span> Sarah K.</td>
            <td><span class="mood-chip mood-stable">Stable</span></td>
            <td>14</td>
            <td>just now</td>
          </tr>
          <tr>
            <td><span class="u-av uav2">J</span> James R.</td>
            <td><span class="mood-chip mood-critical">Critical</span></td>
            <td>7</td>
            <td>4 min ago</td>
          </tr>
          <tr>
            <td><span class="u-av uav3">P</span> Priya M.</td>
            <td><span class="mood-chip mood-moderate">Moderate</span></td>
            <td>22</td>
            <td>9 min ago</td>
          </tr>
          <tr>
            <td><span class="u-av uav4">T</span> Tom W.</td>
            <td><span class="mood-chip mood-low">Low Risk</span></td>
            <td>3</td>
            <td>17 min ago</td>
          </tr>
          <tr>
            <td><span class="u-av uav5">A</span> Aisha O.</td>
            <td><span class="mood-chip mood-stable">Stable</span></td>
            <td>31</td>
            <td>25 min ago</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Alert Feed -->
    <div class="glass-panel" data-delay="100">
      <div class="panel-header">
        <div>
          <div class="panel-title">Emotional Alert Queue</div>
          <div class="panel-sub">Requires admin attention</div>
        </div>
        <span class="panel-tag tag-warn">38 OPEN</span>
      </div>
      <div class="alert-list">
        <div class="alert-item sev-high">
          <div class="alert-icon">🚨</div>
          <div class="alert-content">
            <div class="alert-msg">Repeated crisis language detected — immediate follow-up required</div>
            <div class="alert-time">USR-0582 · 11 min ago</div>
          </div>
          <div class="alert-sev">HIGH</div>
        </div>
        <div class="alert-item sev-high">
          <div class="alert-icon">⚠️</div>
          <div class="alert-content">
            <div class="alert-msg">User reports severe sleep disruption for 5th consecutive session</div>
            <div class="alert-time">USR-2294 · 34 min ago</div>
          </div>
          <div class="alert-sev">HIGH</div>
        </div>
        <div class="alert-item sev-medium">
          <div class="alert-icon">🔶</div>
          <div class="alert-content">
            <div class="alert-msg">Downward mood trend detected over past 7 sessions</div>
            <div class="alert-time">USR-3107 · 1 hr ago</div>
          </div>
          <div class="alert-sev">MED</div>
        </div>
        <div class="alert-item sev-low">
          <div class="alert-icon">💙</div>
          <div class="alert-content">
            <div class="alert-msg">Mild anxiety indicators; recommend proactive check-in</div>
            <div class="alert-time">USR-7751 · 2 hr ago</div>
          </div>
          <div class="alert-sev">LOW</div>
        </div>
      </div>
    </div>

  </div>

</div><!-- /page -->

<script>
/* ── Clock ── */
function updateClock(){
  const now = new Date();
  const h = String(now.getHours()).padStart(2,'0');
  const m = String(now.getMinutes()).padStart(2,'0');
  const s = String(now.getSeconds()).padStart(2,'0');
  const el = document.getElementById('clockVal');
  if(el) el.textContent = h+':'+m+':'+s;
  const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const d = document.getElementById('clockDate');
  if(d) d.textContent = days[now.getDay()]+', '+months[now.getMonth()]+' '+now.getDate();
}
updateClock();
setInterval(updateClock,1000);

/* ── Scroll-based reveal via IntersectionObserver ── */
const ioOptions = {
  root: null,
  rootMargin: '0px 0px -60px 0px',
  threshold: 0.12
};

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, ioOptions);

/* Observe .scroll-reveal elements */
document.querySelectorAll('.scroll-reveal').forEach(el => revealObserver.observe(el));

/* ── Analytics Cards staggered reveal ── */
const cardObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      const delay = parseInt(entry.target.dataset.delay||0);
      const barTarget = parseInt(entry.target.dataset.bar||0);
      setTimeout(()=>{
        entry.target.classList.add('revealed');
        /* Animate bar fill */
        const bar = entry.target.querySelector('.card-bar-fill');
        if(bar) setTimeout(()=>{ bar.style.width = barTarget+'%'; }, 200);
      }, delay);
      cardObserver.unobserve(entry.target);
    }
  });
}, {threshold:0.15});

document.querySelectorAll('.acard').forEach(el => cardObserver.observe(el));

/* ── Glass panels staggered reveal ── */
const panelObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      const delay = parseInt(entry.target.dataset.delay||0);
      setTimeout(()=>{ entry.target.classList.add('revealed'); }, delay);

      /* Trigger perf bars once panels visible */
      if(entry.target.querySelector('#pf1')){
        setTimeout(()=>{
          const bars = [
            {id:'pf1',val:94,label:'pv1',text:'94.2%'},
            {id:'pf2',val:78,label:'pv2',text:'78.5%'},
            {id:'pf3',val:99,label:'pv3',text:'99.7%'}
          ];
          bars.forEach((b,i)=>{
            setTimeout(()=>{
              const fill = document.getElementById(b.id);
              const val  = document.getElementById(b.label);
              if(fill) fill.style.width = b.val+'%';
              if(val)  val.textContent  = b.text;
            }, 300 + i*150);
          });
        }, delay+200);
      }

      panelObserver.unobserve(entry.target);
    }
  });
}, {threshold:0.1});

document.querySelectorAll('.glass-panel').forEach(el => panelObserver.observe(el));

/* ── Logout ── */
function doLogout(){
  const target = 'http://localhost:8501/?logout=1';
  /* window.top breaks out of ALL iframe layers Streamlit creates */
  try {
    window.top.location.href = target;
  } catch(e) {
    /* Cross-origin fallback — post message up the chain */
    try { window.parent.location.href = target; } catch(e2) {
      window.location.href = target;
    }
  }
}
</script>
</body>
</html>"""

    components.html(html, height=1600, scrolling=True)