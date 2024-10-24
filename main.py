# Load welcome message
# after 5 s, clear screen
# Load home/main screen
# ^ List + roulette ^

# import welcome
import click
from connect_to_tmdb import search_by_title

# welcome.my_function()

# commands


@click.command()
@click.argument("cmd")
@click.option("-t", "--title", required=False, help="Title of the movie to search for.")
def cli(cmd, title):
    if cmd == "\search":
        if title:
            search_by_title(title)
        else:
            click.echo("Please provide a title to search for using -t or --title.")
    else:
        click.echo("Unknown command. Use \search to find movies by title.")


def main():

    # welcome message goes here
    print("\nWelcome to the Movie Picker CLI!")
    print("Type '\search -t {title}' to search for a movie or 'exit' to quit.\n")

    while True:
        user_input = input("Enter a command: ")

        if user_input.lower() == "exit":
            print("buh-bye!\n")
            break

        try:
            args = user_input.split()

            # print(args)

            cli(args, standalone_mode=False)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
