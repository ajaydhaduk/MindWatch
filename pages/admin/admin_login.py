import streamlit as st

def show():

    st.title("Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.admin = True
            st.rerun()

        else:
            st.error("Invalid credentials")
