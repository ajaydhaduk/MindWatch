"""
Navigation Bar Component for MindWatch
Modern glassmorphism design for authenticated users
"""

import streamlit as st
from auth.auth_handler import AuthHandler


def show_navbar():
    """
    Display the navigation bar with user information
    Shows user profile and logout button when logged in
    """
    
    auth = AuthHandler()
    
    # Add custom CSS for navbar
    st.markdown("""
    <style>
    /* Dashboard Navbar */
    .dashboard-navbar {
        background: rgba(10, 1, 24, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1rem 1.5rem;
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .navbar-logo-section {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .navbar-logo-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #8b5cf6, #3b82f6);
        border-radius: 12px;
        font-size: 1.5rem;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
    }
    
    .navbar-logo-text {
        font-family: 'Syne', 'Outfit', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff, #8b5cf6, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .navbar-user-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .navbar-user-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.5rem 1rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .navbar-user-name {
        color: rgba(255, 255, 255, 0.9);
        font-weight: 600;
        font-size: 0.95rem;
        font-family: 'DM Sans', sans-serif;
    }
    
    .user-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: 2px solid rgba(139, 92, 246, 0.5);
        box-shadow: 0 0 12px rgba(139, 92, 246, 0.3);
        object-fit: cover;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .dashboard-navbar {
            padding: 1rem;
            flex-direction: column;
            text-align: center;
        }
        
        .navbar-logo-section {
            width: 100%;
            justify-content: center;
        }
        
        .navbar-user-section {
            width: 100%;
            justify-content: center;
        }
        
        .navbar-logo-text {
            font-size: 1.4rem;
        }
        
        .navbar-logo-icon {
            width: 36px;
            height: 36px;
            font-size: 1.3rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create navbar layout
    if auth.is_logged_in():
        user = auth.get_user()
        
        # Create navbar HTML
        avatar_html = f'<img src="{user.get("picture")}" class="user-avatar" alt="User Avatar" />' if user.get("picture") else '<div class="user-avatar" style="background: linear-gradient(135deg, #8b5cf6, #3b82f6);"></div>'
        
        st.markdown(f"""
        <div class="dashboard-navbar">
            <div class="navbar-logo-section">
                <div class="navbar-logo-icon">🧠</div>
                <span class="navbar-logo-text">MindWatch</span>
            </div>
            <div class="navbar-user-section">
                <div class="navbar-user-info">
                    {avatar_html}
                    <span class="navbar-user-name">{user.get("name", "User")}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Logout button (using Streamlit button)
        col1, col2, col3 = st.columns([6, 2, 2])
        with col3:
            if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
                auth.logout()
    else:
        # Simple navbar for non-logged-in users
        st.markdown("""
        <div class="dashboard-navbar">
            <div class="navbar-logo-section" style="margin: 0 auto;">
                <div class="navbar-logo-icon">🧠</div>
                <span class="navbar-logo-text">MindWatch</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def show_navbar_simple():
    """
    Display a simple navbar without authentication info
    Useful for public pages or when you want minimal navbar
    """
    
    st.markdown("""
    <style>
    .simple-navbar {
        background: rgba(10, 1, 24, 0.9);
        backdrop-filter: blur(20px);
        padding: 1.25rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .simple-navbar-content {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
    }
    
    .simple-navbar-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #8b5cf6, #3b82f6);
        border-radius: 12px;
        font-size: 1.5rem;
    }
    
    .simple-navbar-title {
        font-family: 'Syne', 'Outfit', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff, #8b5cf6, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="simple-navbar">
        <div class="simple-navbar-content">
            <div class="simple-navbar-icon">🧠</div>
            <div class="simple-navbar-title">MindWatch</div>
        </div>
    </div>
    """, unsafe_allow_html=True)