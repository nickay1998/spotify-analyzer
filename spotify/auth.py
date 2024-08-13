import streamlit as st
from .utils import post_data

token = None

def retrieve_access_token():
    
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": st.secrets["API_KEY"],
        "client_secret": st.secrets["API_SECRET"]
    }

    access_token_response = post_data(url, headers, data)

    return access_token_response["access_token"]

def check_spotify_access():    
    global token
    token = retrieve_access_token()
    st.toast(f"Successfully acquired access token: " + token, icon="✅")

def get_token():
    global token
    return token