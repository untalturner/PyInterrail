"""The module with the main functions."""

import requests

from PyInterrail.stop_location import from_json

# Constants
URL = "https://api.eurail.com/timetable/location.name"


class Client:
    """ The main class for the client """

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

        params = {'input': name}
        response = requests.get(URL, params)
        return from_json(response.json())
