"""The module which represents a stop location."""

import json

# Strings for JSON
LOCATION_ID = "extId"
LOCATION_NAME = "name"
LOCATION_LONGITUDE = "lon"
LOCATION_LATITUDE = "lat"


class StopLocation:
    """
    A class used to represent the stop locations.

    ...

    Attributes
    ----------
    id : str
        the id of the stop location
    name : str
        the name of the stop location
    lon : int
        the longitude of the stop location
    lat: int
        the latitude of the stop location
    """

    def __init__(self, id, name, lon, lat):
        self.id = id
        self.name = name
        self.lon = lon
        self.lat = lat


def from_json(data):
    """
    The method to parse a json to a StopLocation.

    Parameters
    ----------
    data : str
        the json representation for the stop location

    Returns
    -------
    StopLocation
        the stop location object
    """

    if data is None:
        return None

    dictionary = json.loads(data)

    result = StopLocation(None, None, None, None)
    result.id = dictionary[LOCATION_ID]
    result.name = dictionary[LOCATION_NAME]
    result.lon = dictionary[LOCATION_LONGITUDE]
    result.lat = dictionary[LOCATION_LATITUDE]
    return result
