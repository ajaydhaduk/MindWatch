"""
chat_api.py
───────────
Streamlit query-params bridge between the JS frontend (user_public.py)
and the RAGChatbot backend.

How it works:
  1. user_public.py's JS calls:
       fetch("?chat_msg=<encoded message>")   (same page, GET request)
  2. Streamlit re-runs with st.query_params["chat_msg"] set.
  3. This module detects that param, runs RAGChatbot.get_response(),
     writes the answer into st.session_state, and returns it as JSON
     via st.write() in a hidden div that JS reads back.

NOTE: Because Streamlit does not natively support REST endpoints,
      we use the cleaner approach of st.session_state + st.rerun()
      triggered via a hidden Streamlit text_input acting as a message bus.
      See user_public.py for the full wiring.
"""

import streamlit as st
from chatbot.rag_chatbot import RAGChatbot


@st.cache_resource          # load model only once across all sessions
def get_bot() -> RAGChatbot:
    return RAGChatbot()


def handle_chat_request() -> str | None:
    """
    Call this at the top of user_public.show().
    Returns the bot reply string if a new message is pending, else None.
    """
    bot = get_bot()

    pending = st.session_state.get("_pending_msg", "").strip()
    if not pending:
        return None

    # Clear immediately so we don't double-process
    st.session_state["_pending_msg"] = ""

    response = bot.get_response(pending)
    return response