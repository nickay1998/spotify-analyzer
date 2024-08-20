import streamlit as st
from spotify import check_spotify_access, search, process_artist_data
from streamlit_js_eval import streamlit_js_eval

if __name__ == '__main__':

    # Set title in tab
    st.set_page_config(page_title="Spotify Analysis", layout="wide")

    # Fetch initial window width
    streamlit_js_eval(js_expressions='window.innerWidth', key="window_width")
    
    check_spotify_access()

    with st.form(key="Search"):
        search_text = st.text_input("Search Spotify")
        submitted = st.form_submit_button(label="Submit")

    if submitted:
        search_results = search(search_text)
        
        process_artist_data(search_results["artists"])