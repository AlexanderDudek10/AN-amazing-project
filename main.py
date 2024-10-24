# Load welcome message
# after 5 s, clear screen
# Load home/main screen
# ^ List + roulette ^

# import welcome
import click
from connect_to_tmdb import search_by_title, search_by_year, search_by_genres
from variables import genre_dict
from utils import display_movies, get_genre_ids

# welcome.my_function()

# commands


@click.command()
@click.argument("cmd")
@click.option("-t", "title", required=False, help="Title of the movie to search for.")
@click.option("-y", "year", required=False, help="Year of movies to search for.")
@click.option("-g", "genres", required=False, help="Genre(s) of movies to search for.")
def cli(cmd, title, year, genres):
    if cmd == "\search":

        # only look for year
        if year and not title and not genres:
            movies = search_by_year(year)
            display_movies(movies)

        # only look for genres
        elif genres and not title and not year:
            movies = search_by_genres(genres)
            display_movies(movies)

        # only look for title
        elif title and not year and not genres:
            movies = search_by_title(title)
            display_movies(movies)

        # only look for title and genres
        elif title and not year:
            movies = search_by_title(title)
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
        elif title and not genres:
            movies = search_by_title(title)
            movies = [
                movie for movie in movies if movie["release_date"].startswith(year)
            ]

            if movies:
                display_movies(movies)
            else:
                click.echo("No results found.\n")

        # look for title, year and genres
        elif title and year and genres:
            movies = search_by_title(title)
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
            click.echo(
                "\n-t to search for titles. '\search -t title'.\n-y for years. '\search -t title -y year'.\n-g for genres. '\search -t title -g genre,genre,genre' (no space between multiple genres).\n\nOr you can quit the program with 'exit'\n"
            )
    else:
        click.echo(
            "Unknown command. Use \search to find movies by title, year, genre or combination of any.\n"
        )


def main():
    # welcome message goes here
    print("\nWelcome to the Movie Picker CLI!\n")
    print(
        "-t to search for titles. '\search -t title'.\n-y for years. '\search -t title -y year'.\n-g for genres. '\search -t title -g genre,genre,genre' (no space between multiple genres).\n\nOr you can quit the program with 'exit'\n"
    )

    while True:
        user_input = input("Enter a command: ")

        if user_input.lower() == "exit":
            print("buh-bye!\n")
            break

        try:
            args = user_input.split()
            # print(args)

            cli.main(args=args, standalone_mode=False)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
