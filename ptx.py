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
#     result = welcome_from_dict(json.loads(json_string))


# generated from https://app.quicktype.io/#l=python
# and modify speed, azimuth from int to float

from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
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


@dataclass
class BusPosition:
    position_lon: float
    position_lat: float
    geo_hash: str

    @staticmethod
    def from_dict(obj: Any) -> 'BusPosition':
        assert isinstance(obj, dict)
        position_lon = from_float(obj.get("PositionLon"))
        position_lat = from_float(obj.get("PositionLat"))
        geo_hash = from_str(obj.get("GeoHash"))
        return BusPosition(position_lon, position_lat, geo_hash)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PositionLon"] = to_float(self.position_lon)
        result["PositionLat"] = to_float(self.position_lat)
        result["GeoHash"] = from_str(self.geo_hash)
        return result


@dataclass
class RouteName:
    zh_tw: str
    en: str

    @staticmethod
    def from_dict(obj: Any) -> 'RouteName':
        assert isinstance(obj, dict)
        zh_tw = from_str(obj.get("Zh_tw"))
        en = from_str(obj.get("En"))
        return RouteName(zh_tw, en)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Zh_tw"] = from_str(self.zh_tw)
        result["En"] = from_str(self.en)
        return result


@dataclass
class WelcomeElement:
    plate_numb: str
    operator_id: int
    route_uid: str
    route_id: str
    route_name: RouteName
    sub_route_uid: str
    sub_route_id: str
    sub_route_name: RouteName
    direction: int
    bus_position: BusPosition
    speed: float
    azimuth: float
    duty_status: int
    bus_status: int
    message_type: int
    gps_time: datetime
    src_rec_time: datetime
    src_trans_time: datetime
    update_time: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        plate_numb = from_str(obj.get("PlateNumb"))
        operator_id = int(from_str(obj.get("OperatorID")))
        route_uid = from_str(obj.get("RouteUID"))
        route_id = from_str(obj.get("RouteID"))
        route_name = RouteName.from_dict(obj.get("RouteName"))
        sub_route_uid = from_str(obj.get("SubRouteUID"))
        sub_route_id = from_str(obj.get("SubRouteID"))
        sub_route_name = RouteName.from_dict(obj.get("SubRouteName"))
        direction = from_int(obj.get("Direction"))
        bus_position = BusPosition.from_dict(obj.get("BusPosition"))
        speed = from_float(obj.get("Speed"))
        azimuth = from_float(obj.get("Azimuth"))
        duty_status = from_int(obj.get("DutyStatus"))
        bus_status = from_int(obj.get("BusStatus"))
        message_type = from_int(obj.get("MessageType"))
        gps_time = from_datetime(obj.get("GPSTime"))
        src_rec_time = from_datetime(obj.get("SrcRecTime"))
        src_trans_time = from_datetime(obj.get("SrcTransTime"))
        update_time = from_datetime(obj.get("UpdateTime"))
        return WelcomeElement(plate_numb, operator_id, route_uid, route_id, route_name, sub_route_uid, sub_route_id, sub_route_name, direction, bus_position, speed, azimuth, duty_status, bus_status, message_type, gps_time, src_rec_time, src_trans_time, update_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlateNumb"] = from_str(self.plate_numb)
        result["OperatorID"] = from_str(str(self.operator_id))
        result["RouteUID"] = from_str(self.route_uid)
        result["RouteID"] = from_str(self.route_id)
        result["RouteName"] = to_class(RouteName, self.route_name)
        result["SubRouteUID"] = from_str(self.sub_route_uid)
        result["SubRouteID"] = from_str(self.sub_route_id)
        result["SubRouteName"] = to_class(RouteName, self.sub_route_name)
        result["Direction"] = from_int(self.direction)
        result["BusPosition"] = to_class(BusPosition, self.bus_position)
        result["Speed"] = from_int(self.speed)
        result["Azimuth"] = from_int(self.azimuth)
        result["DutyStatus"] = from_int(self.duty_status)
        result["BusStatus"] = from_int(self.bus_status)
        result["MessageType"] = from_int(self.message_type)
        result["GPSTime"] = self.gps_time.isoformat()
        result["SrcRecTime"] = self.src_rec_time.isoformat()
        result["SrcTransTime"] = self.src_trans_time.isoformat()
        result["UpdateTime"] = self.update_time.isoformat()
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)
