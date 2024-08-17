from streamlit_card import card

def display_card(data):
    if len(data.images) > 0:
        image_link = data.images[0]["url"]
    else:
        image_link = ""

    card(
        title="",
        text=data.name,
        image=image_link,
        styles={
            "card": { "width": "100%", "height": "width", "border-radius": "10px", "aspect-ratio": "1","box-shadow": "0 0 0px rgba(0,0,0,0.5)", "margin": "1px" },
            "filter": { "background-color": "rgba(0, 0, 0, 0.5)" },
            "div": { "padding": "1px" }
        },
        key=data.id,
    )
