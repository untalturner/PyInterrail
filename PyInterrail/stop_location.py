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
    lon : float
        the longitude of the stop location
    lat: float
        the latitude of the stop location
    """

    def __init__(self, id, name, lon, lat):
        self.id = id
        self.name = name
        self.lon = lon
        self.lat = lat


def from_json(data):
    """
    The method to parse a json to a list of StopLocation.

    Parameters
    ----------
    data : str
        the json-encoded representation for the stop locations

    Returns
    -------
    list
        a list of StopLocations
    """

    if data is None:
        return None

    locations = data.get("stopLocationOrCoordLocation")

    if locations is None:
        return None

    results = []
    for location in [x.get("StopLocation") for x in locations]:
        result = StopLocation(None, None, None, None)
        result.id = location.get(LOCATION_ID)
        result.name = location.get(LOCATION_NAME)
        result.lon = location.get(LOCATION_LONGITUDE)
        result.lat = location.get(LOCATION_LATITUDE)
        results.append(result)
    return results
