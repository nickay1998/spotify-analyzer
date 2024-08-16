import streamlit as st

def process_artist_data(data):
    items = data["items"]

    with st.expander("Artist results", True):
        st.write(items)

    artists = []

    with st.expander("Artist images", True):
        for item in items:
            artist = Artist(item)
            artists.append(artist)

            if len(artist.images) == 0:
                image_url = "assets/blank.PNG"
            else:
                image_url = artist.images[0]["url"]

            st.image(image_url, artist.name)


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