"""The module with the main functions."""

import requests

from PyInterrail.stop_location import from_json
from PyInterrail.config import URL_GET_LOCATIONS


class Client:
    """ The main class for the client """

    def get_locations(name: str):
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
        response = requests.get(URL_GET_LOCATIONS, params)
        return from_json(response.json())
