"""The module which represents a service."""


class Service:
    """
    A class used to represent a service in a trip.

    ...

    Attributes
    ----------
    origin_id : str
        the id of the origin
    departure_time : str
        the departure time
    departure_date : str
        the departure date
    destination_id: str
        the id of the destination
    arrival_time: str
        the arrival time
    arrival_date: str
        the arrival date
    train_name: str
        the train name
    train_operator: str
        the operator name of the train
    sleeper_train: bool
        the boolean to indicate that the train has beds
    """

    def __init__(self, origin_id: str, departure_time: str, departure_date: str, destination_id: str,
                 arrival_time: str, arrival_date: str, train_name: str, train_operator: str, sleeper_train: bool):
        self.origin_id = origin_id
        self.departure_time = departure_time
        self.departure_date = departure_date
        self.destination_id = destination_id
        self.arrival_time = arrival_time
        self.arrival_date = arrival_date
        self.train_name = train_name
        self.train_operator = train_operator
        self.sleeper_train = sleeper_train

    def __str__(self):
        return f"origin id: {self.origin_id}, departure time: {self.departure_time}, " \
               f"departure date: {self.departure_date}, destination id: {self.destination_id}, " \
               f"arrival time: {self.arrival_time}, arrival date: {self.arrival_date}, " \
               f"train name: {self.train_name}, train operator: {self.train_operator}, " \
               f"sleeper train: {self.sleeper_train}"


def service_from_json(data):
    """
    The method to parse a json to a Service.

    Parameters
    ----------
    data : str
        the json-encoded representation for the service

    Returns
    -------
    Service
        a Service object
    """

    if data is None:
        raise ValueError("Error")

    service = data

    result = Service(origin_id=service.get("Origin", {}).get("extId"), departure_time=service.get("Origin", {}).get("time"),
                     departure_date=service.get("Origin", {}).get("date"),
                     destination_id=service.get("Destination", {}).get("extId"),
                     arrival_time=service.get("Destination", {}).get("time"),
                     arrival_date=service.get("Destination", {}).get("date"),
                     train_name=service.get("Product", {}).get("name"),
                     train_operator=service.get("Product", {}).get("operator"), sleeper_train=False)

    for note in [x for x in service.get("Notes", {}).get("Note")]:
        if "sleeper" in note.get("value"):
            result.sleeper_train = True

    return result
