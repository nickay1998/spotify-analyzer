import streamlit as st
from streamlit_card import card

def display_card(item):
    if len(item.images) > 0:
        image_link = item.images[0]["url"]
    else:
        image_link = ""

    card(
        title="",
        text=item.name,
        image=image_link,
        styles={
            "card": { "width": "100%", "height": "width", "border-radius": "10px", "aspect-ratio": "1","box-shadow": "0 0 0px rgba(0,0,0,0.5)", "margin": "1px" },
            "filter": { "background-color": "rgba(0, 0, 0, 0.5)" },
            "div": { "padding": "1px" }
        },
        key=item.id,
    )

def display_cards(items):
    window_width = st.session_state["window_width"]

    columns = round(window_width / 330)
    columns = 2 if columns < 2 else columns

    grouped_list = [items[i:i+columns] for i in range(0, len(items), columns)]

    for group in grouped_list:
        cols = st.columns(columns)
        for i, result in enumerate(group):
            with cols[i]:
                display_card(result)