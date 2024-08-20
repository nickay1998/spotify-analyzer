import streamlit as st
from utils import display_cards
import math

def process_artist_data(data):
    items = data["items"]
    artists = []

    for item in items:
        artist = Artist(item)
        artists.append(artist)

    display_cards(artists)

class Artist:
    def __init__(self, data):
        self.name = data["name"]
        self.followers = data["followers"]["total"]
        self.genres = data["genres"]
        self.id = data["id"]
        self.images = data["images"]
        self.popularity = data["popularity"]
        self.uri = data["uri"]
        self.url = data["external_urls"]["spotify"]
        self.data = data