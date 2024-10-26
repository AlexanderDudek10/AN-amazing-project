# Load welcome message
# after 5 s, clear screen
# Load home/main screen
# ^ List + roulette ^

# import welcome
import click
from commands.search import search
from commands.wishlist import wishlist


@click.group()
def cli():
    """Main CLI group"""
    pass


cli.add_command(search)
cli.add_command(wishlist)


def main():
    # welcome message goes here
    # welcome.my_function()

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
            print(args)

            if args[0] == "\search":
                args[0] = "search"
                cli.main(args=args, standalone_mode=False)
            elif args[0] == "\wishlist":
                args[0] = "wishlist"
                cli.main(args=args, standalone_mode=False)
            else:
                print("Command not known.")

        except Exception as e:
            print(f"\nError: {e}")


main()
