"""
Authentication Handler for MindWatch
Manages user login state and session
"""

import streamlit as st
import json
from urllib.parse import unquote


class AuthHandler:
    """
    Handles authentication logic for MindWatch
    Reads user data from URL parameters set by Firebase login
    """
    
    def __init__(self):
        """Initialize the authentication handler"""
        self._init_session_state()
        self._check_url_params()
    
    def _init_session_state(self):
        """Initialize session state variables"""
        if "user" not in st.session_state:
            st.session_state.user = None
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
    
    def _check_url_params(self):
        """Check URL for user data from Firebase redirect"""
        try:
            # Get query parameters
            query_params = st.query_params
            
            # Check if user data exists in URL
            if "user" in query_params:
                user_encoded = query_params["user"]
                
                # Decode user data
                user_json = unquote(user_encoded)
                user_data = json.loads(user_json)
                
                # Store in session state
                st.session_state.user = user_data
                st.session_state.logged_in = True
                
                # Clear the URL parameter (optional, for cleaner URLs)
                # Note: This requires a rerun
                st.query_params.clear()
                
        except Exception as e:
            # If there's an error parsing user data, keep logged out
            st.session_state.logged_in = False
            st.session_state.user = None
    
    def is_logged_in(self):
        """
        Check if user is currently logged in
        
        Returns:
            bool: True if user is logged in, False otherwise
        """
        return st.session_state.logged_in
    
    def get_user(self):
        """
        Get current user data
        
        Returns:
            dict: User data including name, email, picture
            None: If no user is logged in
        """
        return st.session_state.user if self.is_logged_in() else None
    
    def logout(self):
        """
        Logout the current user
        Clears session state and forces a rerun
        """
        st.session_state.user = None
        st.session_state.logged_in = False
        st.rerun()
    
    def get_user_name(self):
        """
        Get the current user's display name
        
        Returns:
            str: User's name or "Guest" if not logged in
        """
        user = self.get_user()
        return user["name"] if user else "Guest"
    
    def get_user_email(self):
        """
        Get the current user's email
        
        Returns:
            str: User's email or None if not logged in
        """
        user = self.get_user()
        return user["email"] if user else None
    
    def get_user_picture(self):
        """
        Get the current user's profile picture URL
        
        Returns:
            str: URL to user's profile picture or None if not logged in
        """
        user = self.get_user()
        return user["picture"] if user else None