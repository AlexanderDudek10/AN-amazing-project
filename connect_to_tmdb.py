import requests
import pandas as pd
from utils import get_genre_ids, get_genre_filtered, genre_dict

# TMDB API key
API_KEY = "2689ee59db9c014d31fd30f77f57e447"

# alex's api key: c19b037e22194f3f3fdec719b1521f62
# nat's api key: 2689ee59db9c014d31fd30f77f57e447

# --------------------------------------------------------
# functions


def search_movies(title, year, genres):

    updated_genres = None

    if genres:
        updated_genres = get_genre_ids(genres)
        print(updated_genres)

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": API_KEY,
        "query": title,
        "primary_release_year": year,
    }

    genre_url = f"https://api.themoviedb.org/3/discover/movie?with_genres={updated_genres}&api_key={API_KEY}"

    # get just genres
    if title == None and year == None:
        genre_movies = requests.get(genre_url).json()
        movies = genre_movies["results"]

        return movies

    # get title/year + genres
    else:
        response = requests.get(url, params=params).json()
        res_movies = response["results"]

        print(res_movies)

        # filter results by genres
        if genres:
            # genre_movies = requests.get(genre_url).json()
            # res_genre_movies = genre_movies["results"]

            filtered_movies = get_genre_filtered(res_movies, updated_genres)

            return filtered_movies

        return res_movies


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
