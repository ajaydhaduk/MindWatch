"""
Firebase Configuration
Replace values with your Firebase Web App config
"""

FIREBASE_CONFIG = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT.firebaseapp.com",
    "projectId": "YOUR_PROJECT_ID",
    "storageBucket": "YOUR_PROJECT.appspot.com",
    "messagingSenderId": "YOUR_SENDER_ID",
    "appId": "YOUR_APP_ID"
}

# Firebase REST endpoints
GOOGLE_AUTH_URL = (
    "https://accounts.google.com/o/oauth2/v2/auth"
)

TOKEN_URL = "https://oauth2.googleapis.com/token"

USER_INFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"
