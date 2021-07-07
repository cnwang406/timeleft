# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = tra_response_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


class Name:
    zh_tw: str
    en: str

    def __init__(self, zh_tw: str, en: str) -> None:
        self.zh_tw = zh_tw
        self.en = en

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        assert isinstance(obj, dict)
        zh_tw = from_str(obj.get("Zh_tw"))
        en = from_str(obj.get("En"))
        return Name(zh_tw, en)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Zh_tw"] = from_str(self.zh_tw)
        result["En"] = from_str(self.en)
        return result


class TimeTable:
    sequence: int
    train_no: int
    destination_station_id: str
    destination_station_name: Name
    train_type_id: str
    train_type_code: int
    train_type_name: Name
    arrival_time: str
    departure_time: str

    def __init__(self, sequence: int, train_no: int, destination_station_id: str, destination_station_name: Name, train_type_id: str, train_type_code: int, train_type_name: Name, arrival_time: str, departure_time: str) -> None:
        self.sequence = sequence
        self.train_no = train_no
        self.destination_station_id = destination_station_id
        self.destination_station_name = destination_station_name
        self.train_type_id = train_type_id
        self.train_type_code = train_type_code
        self.train_type_name = train_type_name
        self.arrival_time = arrival_time
        self.departure_time = departure_time

    @staticmethod
    def from_dict(obj: Any) -> 'TimeTable':
        assert isinstance(obj, dict)
        sequence = from_int(obj.get("Sequence"))
        train_no = int(from_str(obj.get("TrainNo")))
        destination_station_id = from_str(obj.get("DestinationStationID"))
        destination_station_name = Name.from_dict(
            obj.get("DestinationStationName"))
        train_type_id = from_str(obj.get("TrainTypeID"))
        train_type_code = int(from_str(obj.get("TrainTypeCode")))
        train_type_name = Name.from_dict(obj.get("TrainTypeName"))
        arrival_time = from_str(obj.get("ArrivalTime"))
        departure_time = from_str(obj.get("DepartureTime"))
        return TimeTable(sequence, train_no, destination_station_id, destination_station_name, train_type_id, train_type_code, train_type_name, arrival_time, departure_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Sequence"] = from_int(self.sequence)
        result["TrainNo"] = from_str(str(self.train_no))
        result["DestinationStationID"] = from_str(self.destination_station_id)
        result["DestinationStationName"] = to_class(
            Name, self.destination_station_name)
        result["TrainTypeID"] = from_str(self.train_type_id)
        result["TrainTypeCode"] = from_str(str(self.train_type_code))
        result["TrainTypeName"] = to_class(Name, self.train_type_name)
        result["ArrivalTime"] = from_str(self.arrival_time)
        result["DepartureTime"] = from_str(self.departure_time)
        return result


class StationTimetable:
    route_id: str
    station_id: int
    station_name: Name
    direction: int
    time_tables: List[TimeTable]

    def __init__(self, route_id: str, station_id: int, station_name: Name, direction: int, time_tables: List[TimeTable]) -> None:
        self.route_id = route_id
        self.station_id = station_id
        self.station_name = station_name
        self.direction = direction
        self.time_tables = time_tables

    @staticmethod
    def from_dict(obj: Any) -> 'StationTimetable':
        assert isinstance(obj, dict)
        route_id = from_str(obj.get("RouteID"))
        station_id = int(from_str(obj.get("StationID")))
        station_name = Name.from_dict(obj.get("StationName"))
        direction = from_int(obj.get("Direction"))
        time_tables = from_list(TimeTable.from_dict, obj.get("TimeTables"))
        return StationTimetable(route_id, station_id, station_name, direction, time_tables)

    def to_dict(self) -> dict:
        result: dict = {}
        result["RouteID"] = from_str(self.route_id)
        result["StationID"] = from_str(str(self.station_id))
        result["StationName"] = to_class(Name, self.station_name)
        result["Direction"] = from_int(self.direction)
        result["TimeTables"] = from_list(
            lambda x: to_class(TimeTable, x), self.time_tables)
        return result


class TRAResponse:
    update_time: datetime
    update_interval: int
    src_update_time: datetime
    src_update_interval: int
    train_date: datetime
    station_timetables: List[StationTimetable]

    def __init__(self, update_time: datetime, update_interval: int, src_update_time: datetime, src_update_interval: int, train_date: datetime, station_timetables: List[StationTimetable]) -> None:
        self.update_time = update_time
        self.update_interval = update_interval
        self.src_update_time = src_update_time
        self.src_update_interval = src_update_interval
        self.train_date = train_date
        self.station_timetables = station_timetables

    @staticmethod
    def from_dict(obj: Any) -> 'TRAResponse':
        assert isinstance(obj, dict)
        update_time = from_datetime(obj.get("UpdateTime"))
        update_interval = from_int(obj.get("UpdateInterval"))
        src_update_time = from_datetime(obj.get("SrcUpdateTime"))
        src_update_interval = from_int(obj.get("SrcUpdateInterval"))
        train_date = from_datetime(obj.get("TrainDate"))
        station_timetables = from_list(
            StationTimetable.from_dict, obj.get("StationTimetables"))
        return TRAResponse(update_time, update_interval, src_update_time, src_update_interval, train_date, station_timetables)

    def to_dict(self) -> dict:
        result: dict = {}
        result["UpdateTime"] = self.update_time.isoformat()
        result["UpdateInterval"] = from_int(self.update_interval)
        result["SrcUpdateTime"] = self.src_update_time.isoformat()
        result["SrcUpdateInterval"] = from_int(self.src_update_interval)
        result["TrainDate"] = self.train_date.isoformat()
        result["StationTimetables"] = from_list(
            lambda x: to_class(StationTimetable, x), self.station_timetables)
        return result


def tra_response_from_dict(s: Any) -> TRAResponse:
    return TRAResponse.from_dict(s)


def tra_response_to_dict(x: TRAResponse) -> Any:
    return to_class(TRAResponse, x)
