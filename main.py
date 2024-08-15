import streamlit as st
from spotify import check_spotify_access, search

if __name__ == '__main__':
    check_spotify_access()

    with st.form(key="Search"):
        search_text = st.text_input("Search Spotify")
        submitted = st.form_submit_button(label="Submit")

    if submitted:
        with st.expander("Search results", True):
            st.write(search(search_text))