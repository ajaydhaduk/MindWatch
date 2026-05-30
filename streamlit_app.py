import streamlit as st
from auth.auth_handler import AuthHandler

from pages.user import user_public
from pages.user import user_dashboard
from pages.admin import admin_dashboard

st.set_page_config(
    page_title="MindWatch – AI Mental Health Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

auth = AuthHandler()


def main():

    params = st.query_params

    # ── 1. ADMIN LOGIN  (?admin=true sent by login.html) ──────────────────────
    if params.get("admin") == "true":
        st.session_state["is_admin"] = True
        st.query_params.clear()

    # ── 2. ADMIN LOGOUT  (?logout=1 sent by admin dashboard) ──────────────────
    # Clears the admin session and renders user_public directly
    if params.get("logout") == "1":
        st.session_state.clear()        # wipes is_admin and all other session keys
        st.query_params.clear()         # removes ?logout=1 from the URL
        user_public.show()              # render the public/landing page immediately
        return                          # stop — don't fall through to other checks

    # ── 3. ADMIN SESSION ACTIVE  → show admin dashboard ───────────────────────
    if st.session_state.get("is_admin"):
        admin_dashboard.show()
        return

    # ── 4. REGULAR USER FLOW  (existing logic, untouched) ─────────────────────
    if auth.is_logged_in():
        user_dashboard.show()
    else:
        user_public.show()


main()