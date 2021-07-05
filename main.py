import sys

import urllib3
import json
from ptx import welcome_from_dict

jsonStr = u'''
[{"PlateNumb":"809-U7","OperatorID":"14","RouteUID":"HSZ0739","RouteID":"0739","RouteName":{"Zh_tw":u"綠線","En":u"綠線"},"SubRouteUID":"HSZ073902","SubRouteID":"073902","SubRouteName":{"Zh_tw":u"綠線","En":u"綠線"},"Direction":1,"BusPosition":{"PositionLon":120.981188333333,"PositionLat":24.8122933333333,"GeoHash":"wsqj0uzy4"},"Speed":0.0,"Azimuth":53.0,"DutyStatus":1,"BusStatus":0,"MessageType":1,"GPSTime":"2021-07-05T07:39:53+08:00","SrcRecTime":"2021-07-05T07:39:57+08:00","SrcTransTime":"2021-07-05T07:39:57+08:00","UpdateTime":"2021-07-05T07:39:57+08:00"},{"PlateNumb":"819-U7","OperatorID":"14","RouteUID":"HSZ0739","RouteID":"0739","RouteName":{"Zh_tw":"綠線","En":"綠線"},"SubRouteUID":"HSZ073901","SubRouteID":"073901","SubRouteName":{"Zh_tw":"綠線","En":"綠線"},"Direction":0,"BusPosition":{"PositionLon":120.969646666667,"PositionLat":24.806325,"GeoHash":"wsqj0ez7m"},"Speed":35.0,"Azimuth":233.0,"DutyStatus":1,"BusStatus":0,"MessageType":1,"GPSTime":"2021-07-05T07:39:49+08:00","SrcRecTime":"2021-07-05T07:39:51+08:00","SrcTransTime":"2021-07-05T07:39:51+08:00","UpdateTime":"2021-07-05T07:39:52+08:00"}]
'''
jsonA = [{"PlateNumb": "809-U7", "OperatorID": "14", "RouteUID": "HSZ0739", "RouteID": "0739", "RouteName": {"Zh_tw": u"綠線", "En": u"綠線"}, "SubRouteUID": "HSZ073902", "SubRouteID": "073902", "SubRouteName": {"Zh_tw": u"綠線", "En": u"綠線"}, "Direction": 1, "BusPosition": {"PositionLon": 120.981188333333, "PositionLat": 24.8122933333333, "GeoHash": "wsqj0uzy4"}, "Speed": 0.0, "Azimuth": 53.0, "DutyStatus": 1, "BusStatus": 0, "MessageType": 1, "GPSTime": "2021-07-05T07:39:53+08:00", "SrcRecTime": "2021-07-05T07:39:57+08:00", "SrcTransTime": "2021-07-05T07:39:57+08:00", "UpdateTime": "2021-07-05T07:39:57+08:00"},
         {"PlateNumb": "819-U7", "OperatorID": "14", "RouteUID": "HSZ0739", "RouteID": "0739", "RouteName": {"Zh_tw": "綠線", "En": "綠線"}, "SubRouteUID": "HSZ073901", "SubRouteID": "073901", "SubRouteName": {"Zh_tw": "綠線", "En": "綠線"}, "Direction": 0, "BusPosition": {"PositionLon": 120.969646666667, "PositionLat": 24.806325, "GeoHash": "wsqj0ez7m"}, "Speed": 35.0, "Azimuth": 233.0, "DutyStatus": 1, "BusStatus": 0, "MessageType": 1, "GPSTime": "2021-07-05T07:39:49+08:00", "SrcRecTime": "2021-07-05T07:39:51+08:00", "SrcTransTime": "2021-07-05T07:39:51+08:00", "UpdateTime": "2021-07-05T07:39:52+08:00"}]

if (__name__ == "__main__"):
    print("start here")
    print(isinstance(jsonA, list))
    result = welcome_from_dict(jsonA)
    print(f"total {len(result)} buses.")
    for x in result:
        print(f"bus {x.plate_numb} with speed {x.speed}km/h")

    print("finished")
