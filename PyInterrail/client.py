"""The module with the main functions."""

import requests

from PyInterrail.stop_location import from_json


def get_locations(name):
    """
    The method to call Interrail server for list of locations.

    Parameters
    ----------
    name : str
        the name of the location

    Returns
    -------
    list
        a list of StopLocations
    """

    url = "https://api.eurail.com/timetable/location.name?input=" + str(name)
    response = requests.get(url)
    return from_json(response.json())
