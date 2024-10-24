import pandas as pd
import click


@click.command()
@click.option("-v", "view", is_flag=True, help="View wishlist")
@click.option("-a", "id", required=False, help="Add a movie to wishlist by id.")
def wishlist(view, id):
    """
    Create a wishlist, add or delete movie records, check off movies you've seen and play roulette to choose which movie to watch next.
    """

    if view and not id:
        print("view")

    elif id and not view:
        print(f"id: {id}")
