from utils import get_data

def search(search_term):
    search_term = search_term.replace(" ", "+")
    url = f"https://api.spotify.com/v1/search?q={search_term}&type=album%2Cartist%2Ctrack"
    search_json = get_data(url)

    return search_json