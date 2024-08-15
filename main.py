import streamlit as st
from spotify import check_spotify_access

if __name__ == '__main__':
    check_spotify_access()
    st.write(st.session_state["token"])