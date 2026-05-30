"""
UI Elements Component for MindWatch
Reusable UI components with glassmorphism design
"""

import streamlit as st


def glass_card(title, content):
    """
    Create a glass-morphic card with title and content
    
    Args:
        title (str): Card title/heading
        content (str): Card body content
    """
    st.markdown(
        f"""
        <div style="
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.75rem;
            margin-bottom: 1.25rem;
            transition: all 0.3s ease;
        ">
            <h3 style="
                font-family: 'Syne', 'Outfit', sans-serif;
                font-size: 1.3rem;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 0.75rem;
                margin-top: 0;
            ">{title}</h3>
            <p style="
                font-family: 'DM Sans', sans-serif;
                font-size: 1rem;
                color: rgba(255, 255, 255, 0.8);
                line-height: 1.7;
                margin: 0;
            ">{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_badge(text, color="#8b5cf6"):
    """
    Create a small info badge with glassmorphism
    
    Args:
        text (str): Badge text
        color (str): Badge color (hex code)
    """
    st.markdown(
        f"""
        <span style="
            display: inline-block;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 0.4rem 0.9rem;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.85rem;
            font-weight: 600;
            color: {color};
            margin: 0.25rem;
        ">{text}</span>
        """,
        unsafe_allow_html=True
    )


def section_header(title, subtitle=None):
    """
    Create a section header with optional subtitle
    
    Args:
        title (str): Section title
        subtitle (str, optional): Section subtitle
    """
    st.markdown(
        f"""
        <div style="text-align: center; margin: 2rem 0 1.5rem 0;">
            <h2 style="
                font-family: 'Syne', 'Outfit', sans-serif;
                font-size: clamp(1.75rem, 4vw, 2.25rem);
                font-weight: 700;
                color: #ffffff;
                margin-bottom: {0.75 if subtitle else 0}rem;
                background: linear-gradient(135deg, #ffffff, #8b5cf6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">{title}</h2>
            {f'<p style="font-family: \'DM Sans\', sans-serif; font-size: 1.05rem; color: rgba(255, 255, 255, 0.7); margin: 0;">{subtitle}</p>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True
    )