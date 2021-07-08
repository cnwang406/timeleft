import dateutil.parser
from datetime import datetime
from typing import Any, List, TypeVar, Type, cast, Callable
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
#     result = tra_liveboard_response_from_dict(json.loads(json_string))


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


class StationLiveBoard:
    station_id: int
    station_name: Name
    train_no: int
    direction: int
    train_type_id: str
    train_type_code: int
    train_type_name: Name
    ending_station_id: str
    ending_station_name: Name
    trip_line: int
    platform: str
    schedule_arrival_time: datetime
    schedule_departure_time: datetime
    delay_time: int
    running_status: int
    update_time: datetime

    def __init__(self, station_id: int, station_name: Name, train_no: int, direction: int, train_type_id: str, train_type_code: int, train_type_name: Name, ending_station_id: str, ending_station_name: Name, trip_line: int, platform: str, schedule_arrival_time: datetime, schedule_departure_time: datetime, delay_time: int, running_status: int, update_time: datetime) -> None:
        self.station_id = station_id
        self.station_name = station_name
        self.train_no = train_no
        self.direction = direction
        self.train_type_id = train_type_id
        self.train_type_code = train_type_code
        self.train_type_name = train_type_name
        self.ending_station_id = ending_station_id
        self.ending_station_name = ending_station_name
        self.trip_line = trip_line
        self.platform = platform
        self.schedule_arrival_time = schedule_arrival_time
        self.schedule_departure_time = schedule_departure_time
        self.delay_time = delay_time
        self.running_status = running_status
        self.update_time = update_time

    @staticmethod
    def from_dict(obj: Any) -> 'StationLiveBoard':
        assert isinstance(obj, dict)
        station_id = int(from_str(obj.get("StationID")))
        station_name = Name.from_dict(obj.get("StationName"))
        train_no = int(from_str(obj.get("TrainNo")))
        direction = from_int(obj.get("Direction"))
        train_type_id = from_str(obj.get("TrainTypeID"))
        train_type_code = int(from_str(obj.get("TrainTypeCode")))
        train_type_name = Name.from_dict(obj.get("TrainTypeName"))
        ending_station_id = from_str(obj.get("EndingStationID"))
        ending_station_name = Name.from_dict(obj.get("EndingStationName"))
        trip_line = from_int(obj.get("TripLine"))
        platform = from_str(obj.get("Platform"))
        schedule_arrival_time = from_datetime(obj.get("ScheduleArrivalTime"))
        schedule_departure_time = from_datetime(
            obj.get("ScheduleDepartureTime"))
        delay_time = from_int(obj.get("DelayTime"))
        running_status = from_int(obj.get("RunningStatus"))
        update_time = from_datetime(obj.get("UpdateTime"))
        return StationLiveBoard(station_id, station_name, train_no, direction, train_type_id, train_type_code, train_type_name, ending_station_id, ending_station_name, trip_line, platform, schedule_arrival_time, schedule_departure_time, delay_time, running_status, update_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["StationID"] = from_str(str(self.station_id))
        result["StationName"] = to_class(Name, self.station_name)
        result["TrainNo"] = from_str(str(self.train_no))
        result["Direction"] = from_int(self.direction)
        result["TrainTypeID"] = from_str(self.train_type_id)
        result["TrainTypeCode"] = from_str(str(self.train_type_code))
        result["TrainTypeName"] = to_class(Name, self.train_type_name)
        result["EndingStationID"] = from_str(self.ending_station_id)
        result["EndingStationName"] = to_class(Name, self.ending_station_name)
        result["TripLine"] = from_int(self.trip_line)
        result["Platform"] = from_str(self.platform)
        result["ScheduleArrivalTime"] = self.schedule_arrival_time.isoformat()
        result["ScheduleDepartureTime"] = self.schedule_departure_time.isoformat()
        result["DelayTime"] = from_int(self.delay_time)
        result["RunningStatus"] = from_int(self.running_status)
        result["UpdateTime"] = self.update_time.isoformat()
        return result


class TRALiveboardResponse:
    update_time: datetime
    update_interval: int
    src_update_time: datetime
    src_update_interval: int
    authority_code: str
    station_live_boards: List[StationLiveBoard]

    def __init__(self, update_time: datetime, update_interval: int, src_update_time: datetime, src_update_interval: int, authority_code: str, station_live_boards: List[StationLiveBoard]) -> None:
        self.update_time = update_time
        self.update_interval = update_interval
        self.src_update_time = src_update_time
        self.src_update_interval = src_update_interval
        self.authority_code = authority_code
        self.station_live_boards = station_live_boards

    @staticmethod
    def from_dict(obj: Any) -> 'TRALiveboardResponse':
        assert isinstance(obj, dict)
        update_time = from_datetime(obj.get("UpdateTime"))
        update_interval = from_int(obj.get("UpdateInterval"))
        src_update_time = from_datetime(obj.get("SrcUpdateTime"))
        src_update_interval = from_int(obj.get("SrcUpdateInterval"))
        authority_code = from_str(obj.get("AuthorityCode"))
        station_live_boards = from_list(
            StationLiveBoard.from_dict, obj.get("StationLiveBoards"))
        return TRALiveboardResponse(update_time, update_interval, src_update_time, src_update_interval, authority_code, station_live_boards)

    def to_dict(self) -> dict:
        result: dict = {}
        result["UpdateTime"] = self.update_time.isoformat()
        result["UpdateInterval"] = from_int(self.update_interval)
        result["SrcUpdateTime"] = self.src_update_time.isoformat()
        result["SrcUpdateInterval"] = from_int(self.src_update_interval)
        result["AuthorityCode"] = from_str(self.authority_code)
        result["StationLiveBoards"] = from_list(lambda x: to_class(
            StationLiveBoard, x), self.station_live_boards)
        return result


def tra_liveboard_response_from_dict(s: Any) -> TRALiveboardResponse:
    return TRALiveboardResponse.from_dict(s)


def tra_liveboard_response_to_dict(x: TRALiveboardResponse) -> Any:
    return to_class(TRALiveboardResponse, x)


def tra_liveboard_running_status(status):
    statusDict = {0: '準點', 1: '誤點', 2: '取消'}
    return statusDict[status]


def tra_liveboard_TrainTypeCode(code):
    typeCodeDict = {1: '太魯閣', 2: '普悠瑪', 3: '自強',
                    4: '莒光', 5: '復興', 6: '區間', 7: '普快', 10: '區間快'}
    return typeCodeDict[code]
