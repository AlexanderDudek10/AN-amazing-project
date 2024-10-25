import requests
import click
from utils import genre_dict
import pandas as pd

# TMDB API key
API_KEY = "2689ee59db9c014d31fd30f77f57e447"

# alex's api key: c19b037e22194f3f3fdec719b1521f62
# nat's api key: 2689ee59db9c014d31fd30f77f57e447

# --------------------------------------------------------
# functions


def search_movies(title, year, genres):

    updated_genres = None

    if genres:
        genre_list = genres.split(",")
        genre_arr = []

        for genre in genre_list:
            for k, v in genre_dict.items():
                if v == genre:
                    genre_arr.append(k)

        updated_genres = ",".join(map(str, genre_arr))

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": "2689ee59db9c014d31fd30f77f57e447",
        "query": title,
        "primary_release_year": year,
    }

    genre_url = f"https://api.themoviedb.org/3/discover/movie?with_genres={updated_genres}&api_key={API_KEY}"

    if title and year == "Null":
        response_genres = requests.get(genre_url).json()
        res = response_genres["results"]

    else:
        response = requests.get(url, params=params).json()
        res = response["results"]

        if genres:
            response_genres = requests.get(genre_url)

            # filter results by genres


def new_wishlist_record(id):

    url = f"https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}"
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
        )

        return df2
