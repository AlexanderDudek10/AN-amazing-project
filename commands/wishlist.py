import pandas as pd
import click
from connect_to_tmdb import new_wishlist_record
import os


@click.command()
@click.option("-v", "view", is_flag=True, help="View wishlist")
@click.option("-a", "id", required=False, help="Add a movie to wishlist by id.")
def wishlist(view, id):
    """
    Create a wishlist, add or delete movie records, check off movies you've seen and play roulette to choose which movie to watch next.
    """

    df = None

    if os.path.exists("wishlist.csv"):
        df = pd.read_csv("wishlist.csv")

    else:
        data = {
            "title": [],
            "genres": [],
            "year": [],
            "runtime": [],
        }

        df = pd.DataFrame(data)
        df.to_csv("wishlist.csv", index=True)

    if view and not id:
        print(df)

    elif id and not view:
        print(f"id: {id}")

        df2 = new_wishlist_record(id)

        if isinstance(df2, pd.DataFrame):
            updated_df = pd.concat([df, df2], ignore_index=True)

            updated_df["runtime"] = updated_df["runtime"].astype(int)
            updated_df["id"] = updated_df["id"].astype(int)
            updated_df = updated_df[["id", "title", "genres", "year", "runtime"]]
            updated_df.to_csv("wishlist.csv", index=False)
        else:
            print("no")
