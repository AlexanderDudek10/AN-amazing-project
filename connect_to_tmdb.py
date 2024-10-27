import requests
import pandas as pd
from utils import get_genre_ids, get_title_filtered

# TMDB API key
API_KEY = "2689ee59db9c014d31fd30f77f57e447"

# alex's api key: c19b037e22194f3f3fdec719b1521f62
# nat's api key: 2689ee59db9c014d31fd30f77f57e447

# --------------------------------------------------------
# functions


def search_movies(title, year, genres):
    print(title, year, genres)

    genres = "" if genres is None else get_genre_ids(genres)
    print(title, year, genres)
    
    if genres == "" and year == None and title == None:
        print("Please specify at least one of the following:\n-t for title\n-y for year\n-g for genre")
        exit
    # get just title
    elif genres == "" and year == None:
        title_response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}").json()
        title_movies = title_response["results"]
        
        return title_movies
    
    # get genres/year + title
    elif genres == "":
        response = requests.get(f"https://api.themoviedb.org/3/discover/movie?with_genres={",".join(genres)}&primary_release_year={year}&api_key={API_KEY}").json()
        general_movies = response["results"]
        
        # filter results by title
        if title:

            filtered_movies = get_title_filtered(general_movies, title)

            return filtered_movies

        return general_movies


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
