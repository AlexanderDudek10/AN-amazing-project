import click


def display_movies(movies):
    """Helper function to display movies."""
    for movie in movies:
        year = movie["release_date"].split("-")[0]
        genre_ids = movie["genre_ids"]
        genres = ", ".join(
            [genre_dict.get(genre_id, "Unknown") for genre_id in genre_ids]
        )

        click.echo(f"» {movie['id']} - {movie['title']} ({year}) - {genres}\n")


def get_genre_ids(genres):
    """Convert genre names into their corresponding genre IDs."""
    genre_list = genres.split(",")
    genre_ids = []

    for genre_name in genre_list:
        genre_name = genre_name.strip().lower()

        genre_id = next(
            (k for k, v in genre_dict.items() if v.lower() == genre_name), None
        )

        if genre_id is not None:
            genre_ids.append(str(genre_id))
        else:
            click.echo(f"Genre '{genre_name}' not found.")

    return ",".join(genre_ids)


def get_genre_filtered(movies, genre_ids):
    filtered_movies = [
        movie
        for movie in movies
        if all(genre_id in movie["genre_ids"] for genre_id in genre_ids)
    ]

    return filtered_movies


def get_yearly_filtered(movies, year):
    filtered_movies = [
        movie for movie in movies if movie["release_date"].startswith(year)
    ]

    return filtered_movies


genre_dict = {
    28: "action",
    12: "adventure",
    16: "animation",
    35: "comedy",
    80: "crime",
    99: "documentary",
    18: "drama",
    10751: "family",
    14: "fantasy",
    36: "history",
    27: "horror",
    10402: "music",
    9648: "mystery",
    10749: "romance",
    878: "science fiction",
    10770: "tv movie",
    53: "thriller",
    10752: "war",
    37: "western",
}
