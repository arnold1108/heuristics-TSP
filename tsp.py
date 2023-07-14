# ! /usr/bin/env python

import click
import pandas as pd
import geopy
from geopy import distance
from geopy.geocoders import Nominatim

# Create a function that takes a variable arguments and creates a list of towns


def my_towns(*args):
    """Create a list of towns from arguments"""
    return list(args)

# Creating a function that creates a pandas dataframe of cities and their lattitudes and longitudes


def create_towns_dataframe(towns=None):
    """A dataframe of towns and their latitudes and longitudes"""
    if towns is None:
        towns = ["Nairobi", "Kisumu", "Mombasa", "Eldoret", "Nakuru", "Thika"]
    # Creating an empty list that will hold the latitudes and longitudes
    latitudes = []
    longitudes = []
    # Looping through the towns list to get the latitudes and longitudes
    for town in towns:
        geolocator = Nominatim(user_agent="tsp_pandas")
        location = geolocator.geocode(town)
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
    # Create a dataframe for the towns, their latitudes and their longitudes
    df = pd.DataFrame(
        {
            "Town": towns,
            "Lat": latitudes,
            "Long": longitudes
        }
    )
    return df

# A function that gets the total distance travelled across all the towns
def tsp(towns_df):
    # Create a list of cities  
    towns_df = towns_df["Town"].to_list()
    # Shuffle the list of towns
    # Create a distance list to append to 
    # Get the distance between the towns and append to the list 


# Creating a click group


@click.group()
def cli():
    """This is a commandline tool that figurs out the shortest distance to visit all towns in a list"""

# This command takes a varaible number of arguments of cities passed in


@cli.command("towns")
@click.argument("towns", nargs=-1)  # Takes any number of arguments
@click.option("--count", default=5, help="The number of simulations to run")
def cities_cli(cities, count):
    """This commmand-line tool figurs out the shortest distance to visit all the towns in a list

    Example: ./tsp.py towns "Nairobi" "Eldoret" --count 3
    """
    # Create a list of towns
    towns_list = my_towns(*towns)
    # Create a dataframe of cities and their lattitudes and longitudes
    towns_df = create_towns_dataframe(towns_list)
    # Running the TSP function
    main(count, towns_df)
