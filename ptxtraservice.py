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
#     result = tra_service_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Alert:
    title: str
    status: int
    update_time: datetime

    def __init__(self, title: str, status: int, update_time: datetime) -> None:
        self.title = title
        self.status = status
        self.update_time = update_time

    @staticmethod
    def from_dict(obj: Any) -> 'Alert':
        assert isinstance(obj, dict)
        title = from_str(obj.get("Title"))
        status = from_int(obj.get("Status"))
        update_time = from_datetime(obj.get("UpdateTime"))
        return Alert(title, status, update_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Title"] = from_str(self.title)
        result["Status"] = from_int(self.status)
        result["UpdateTime"] = self.update_time.isoformat()
        return result


class TRAService:
    update_time: datetime
    update_interval: int
    src_update_time: datetime
    src_update_interval: int
    authority_code: str
    alerts: List[Alert]

    def __init__(self, update_time: datetime, update_interval: int, src_update_time: datetime, src_update_interval: int, authority_code: str, alerts: List[Alert]) -> None:
        self.update_time = update_time
        self.update_interval = update_interval
        self.src_update_time = src_update_time
        self.src_update_interval = src_update_interval
        self.authority_code = authority_code
        self.alerts = alerts

    @staticmethod
    def from_dict(obj: Any) -> 'TRAService':
        assert isinstance(obj, dict)
        update_time = from_datetime(obj.get("UpdateTime"))
        update_interval = from_int(obj.get("UpdateInterval"))
        src_update_time = from_datetime(obj.get("SrcUpdateTime"))
        src_update_interval = from_int(obj.get("SrcUpdateInterval"))
        authority_code = from_str(obj.get("AuthorityCode"))
        alerts = from_list(Alert.from_dict, obj.get("Alerts"))
        return TRAService(update_time, update_interval, src_update_time, src_update_interval, authority_code, alerts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["UpdateTime"] = self.update_time.isoformat()
        result["UpdateInterval"] = from_int(self.update_interval)
        result["SrcUpdateTime"] = self.src_update_time.isoformat()
        result["SrcUpdateInterval"] = from_int(self.src_update_interval)
        result["AuthorityCode"] = from_str(self.authority_code)
        result["Alerts"] = from_list(lambda x: to_class(Alert, x), self.alerts)
        return result


def tra_service_from_dict(s: Any) -> TRAService:
    return TRAService.from_dict(s)


def tra_service_to_dict(x: TRAService) -> Any:
    return to_class(TRAService, x)


def tra_service_status(code):
    serviceDict = {0: '全線營運停止', 1: '全線營運正常', 2: '有異常狀況'}
    return serviceDict(code)


def tra_service_scope(code):
    scopeDict = {0: '南下', 1: '北上', 2: '雙向'}
    return scopeDict(code)


def tra_service_level(code):
    levelDict = {1: '重度', 2: '中度', 3: '輕度'}
    return levelDict(code)
