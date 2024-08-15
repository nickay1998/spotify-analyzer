import streamlit as st
from spotify import *

if __name__ == '__main__':
    check_spotify_access()
    st.write(get_token())