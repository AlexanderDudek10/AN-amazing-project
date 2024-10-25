import click
from connect_to_tmdb import search_by_title
from utils import display_movies, get_genre_ids


@click.command()
@click.option("-t", "title", required=False, help="Title of the movie to search for.")
@click.option("-y", "year", required=False, help="Year of movies to search for.")
@click.option("-g", "genres", required=False, help="Genre(s) of movies to search for.")
def search(title, year, genres):
    """
    Search for movies by title, year, and genres.
    """

    # only look for title and genres
    if title and genres and not year:
        movies = search_by_title(title, year, genres)
        genre_ids = get_genre_ids(genres)

        filtered_movies = [
            movie
            for movie in movies
            if all(genre_id in movie["genre_ids"] for genre_id in genre_ids)
        ]

        if filtered_movies:
            display_movies(filtered_movies)
        else:
            click.echo("No results found.\n")

    # only look for title and year
    elif title and year and not genres:
        movies = search_by_title(title, year, genres)
        movies = [movie for movie in movies if movie["release_date"].startswith(year)]

        if movies:
            display_movies(movies)
        else:
            click.echo("No results found.\n")

    # look for title, year and genres
    elif title and year and genres:
        movies = search_by_title(title, year, genres)
        genre_ids = get_genre_ids(genres)

        filtered_movies = [
            movie
            for movie in movies
            if all(genre_id in movie["genre_ids"] for genre_id in genre_ids)
        ]

        if filtered_movies:
            final_movies = [
                movie
                for movie in filtered_movies
                if movie["release_date"].startswith(year)
            ]

            if final_movies:
                display_movies(final_movies)
            else:
                click.echo("No results found.\n")
        else:
            click.echo("No results found.\n")

    else:
        movies = search_by_title(title, year, genres)
        display_movies(movies)

    # else:
    #     click.echo(
    #         "\n-t to search for titles. '\search -t title'.\n-y for years. '\search -t title -y year'.\n-g for genres. '\search -t title -g genre,genre,genre' (no space between multiple genres).\n\nOr you can quit the program with 'exit'\n"
    #     )
