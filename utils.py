from variables import genre_dict
import click


def display_movies(movies):
    """Helper function to display movies."""
    for movie in movies:
        year = movie["release_date"].split("-")[0]
        genre_ids = movie["genre_ids"]
        genres = ", ".join(
            [genre_dict.get(genre_id, "Unknown") for genre_id in genre_ids]
        )
        click.echo(f"- {movie['title']} ({year}) - {genres}\n")


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
            genre_ids.append(genre_id)
        else:
            click.echo(f"Genre '{genre_name}' not found.")

    return genre_ids
