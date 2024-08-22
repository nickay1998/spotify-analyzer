import streamlit as st

def process_artist_data(data):
    return [Artist(item) for item in data["items"]]

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