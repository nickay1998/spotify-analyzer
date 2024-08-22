import streamlit as st
from utils import get_data, display_cards
from .artist import process_artist_data

def search(search_text):
    if "search_results" not in st.session_state:
        st.session_state["search_results"] = {}
    elif search_text in st.session_state["search_results"].keys():
        return st.session_state["search_results"][search_text]

    search_text = search_text.replace(" ", "+")
    url = f"https://api.spotify.com/v1/search?q={search_text}&type=album%2Cartist%2Ctrack"
    search_json = get_data(url)

    if search_text not in st.session_state["search_results"].keys():
        st.session_state["search_results"][search_text] = SearchResults(search_json)

    return st.session_state["search_results"][search_text]

class SearchResults:
    def __init__(self, data):
        self.artist_json = {data["artists"]["offset"]: data["artists"]}
        self.artist_next = data["artists"]["next"]
        self.artists = process_artist_data(data["artists"])

    def add_artists(self):
        data = get_data(self.artist_next)
        self.artist_json[data["artists"]["offset"]] = data["artists"]
        self.artist_next = data["artists"]["next"]
        self.artists = self.artists + process_artist_data(data["artists"])
        self.display_results("artists", data["artists"]["next"] != None)

    def display_results(self, type, button = True):
        with st.session_state["search_container"].container():
            self.display_cards(type)
            
            if button:
                self.load_more_button(type)

    def display_cards(self, type):
        if type == "artists":
            st.write(f"Showing {len(self.artists)} of {self.artist_json[0]['total']} {type}")
            display_cards(self.artists)
    
    def load_more_button(self, type):
        if type == "artists":
            st.button(f"Load more {type}...", on_click=self.add_artists)