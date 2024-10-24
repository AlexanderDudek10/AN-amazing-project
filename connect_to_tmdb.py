import requests
import click
from variables import genre_dict

# TMDB API key
API_KEY = "2689ee59db9c014d31fd30f77f57e447"

# alex's api key: c19b037e22194f3f3fdec719b1521f62
# nat's api key: 2689ee59db9c014d31fd30f77f57e447

# Base URL for TMDB API
BASE_URL = "https://api.themoviedb.org/3"

# --------------------------------------------------------
# functions


def search_by_title(title):
    url = f"{BASE_URL}/search/movie?query={title}&api_key={API_KEY}"
    res = requests.get(url)
    res_json = res.json()
    movies = res_json["results"]

    # results = [movie for movie in movies if title.lower() in movie["title"].lower()]

    if movies:
        click.echo(f"Movies matching '{title}':")

        for movie in movies:
            year = movie["release_date"].split("-")[0]
            genre_ids = movie["genre_ids"]

            genres = ""

            for index, (genre) in enumerate(genre_ids):
                genres += (
                    f", {genre_dict.get(genre)}" if index > 0 else genre_dict.get(genre)
                )

            click.echo(f"- {movie['title']} ({year}) - {genres} \n")

    else:
        click.echo(f"No movies found with the title containing '{title}'.\n")
