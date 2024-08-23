import streamlit as st

# Apply style css
with open("./styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if st.button("Back"):
    st.switch_page("main.py")

type = st.session_state["search_type"]
display_object = st.session_state["display_object"]

st.write(display_object.name)