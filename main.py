import streamlit as st
from spotify import check_spotify_access, search
from streamlit_js_eval import streamlit_js_eval

if __name__ == '__main__':

    # Set title in tab
    st.set_page_config(page_title="Spotify Analysis", layout="wide", initial_sidebar_state="collapsed")
    
    # Fetch initial window width
    streamlit_js_eval(js_expressions='window.innerWidth', key="window_width")

    # Apply style css
    with open("./styles/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    check_spotify_access()

    if "details" not in st.session_state:
        st.session_state["details"] = False

    with st.form(key="Search"):
        if st.session_state["details"]:
            st.session_state["details"] = False
            st.session_state["search_box"] = st.session_state["search_term"]
        
        search_text = st.session_state["search_term"] = st.text_input("Search Spotify", key="search_box")

        submitted = st.form_submit_button(label="Submit")

    if "search_container" not in st.session_state:
        st.session_state["search_container"] = st.empty()

    if submitted:
        search_results = search(search_text)
    elif "search_results" in st.session_state and search_text in st.session_state["search_results"].keys():
        search_results = st.session_state["search_results"][search_text]
    else:
        search_results = None

    if search_results != None:
        search_results.display_results("artists")