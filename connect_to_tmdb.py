import requests
import click
from utils import genre_dict
import pandas as pd

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

    if movies:
        return movies
    else:
        click.echo(f"No movies found with the title containing '{title}'.\n")


def search_by_year(year):
    url = f"{BASE_URL}/discover/movie?primary_release_year={year}&api_key={API_KEY}"
    res = requests.get(url)
    res_json = res.json()
    movies = res_json["results"]

    if movies:
        return movies
    else:
        click.echo(f"No movies found within the year '{year}'.\n")


def search_by_genres(genres):

    genre_list = genres.split(",")
    genre_arr = []

    for genre in genre_list:
        for k, v in genre_dict.items():
            if v == genre:
                genre_arr.append(k)

    updated_genres = ",".join(map(str, genre_arr))

    url = f"{BASE_URL}/discover/movie?with_genres={updated_genres}&api_key={API_KEY}"
    res = requests.get(url)
    res_json = res.json()
    movies = res_json["results"]

    if movies:
        return movies
    else:
        click.echo(f"No movies found with the genres: '{genres}'.\n")


def new_wishlist_record(id):

    url = f"{BASE_URL}/movie/{id}?api_key={API_KEY}"
    res = requests.get(url)
    movie = res.json()

    if movie:

        title = movie["title"]
        genres = movie["genres"]
        year = movie["release_date"].split("-")[0]
        runtime = movie["runtime"]

        genres = ", ".join([genre["name"].lower() for genre in movie["genres"]])

        df2 = pd.DataFrame(
            {
                "id": [movie["id"]],
                "title": [title],
                "genres": [genres],
                "year": [year],
                "runtime": [runtime],
            },
            # index=[movie["id"]],
        )

        return df2
