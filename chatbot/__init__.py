# chatbot/__init__.py
# This file marks 'chatbot' as a Python package.
# It exposes the main classes and functions so they can be imported cleanly.

from chatbot.rag_chatbot import RAGChatbot
from chatbot.chat_api import get_bot, handle_chat_request

__all__ = [
    "RAGChatbot",
    "get_bot",
    "handle_chat_request",
]