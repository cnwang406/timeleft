## enviroment : Python 3.9
### packages :
## IDE : VSCODE

## Source

### URL:
PTX https://ptx.transportdata.tw/MOTC#!/CityBus/CityBusApi_RealTimeByFrequency_UDP_1

### format
/v2/Bus/RealTimeByFrequency/Streaming/City/{City}/{RouteName}
取得指定[縣市],[路線名稱]的公車動態定時資料(A1)[逐筆更新]

https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/Streaming/City/Hsinchu/%E7%B6%A0%E7%B7%9A?$top=30&$format=JSON

** 必須將 路線名稱轉換為 url

### return data
[
  {
    "PlateNumb": "809-U7",
    "OperatorID": "14",
    "RouteUID": "HSZ0739",
    "RouteID": "0739",
    "RouteName": {
      "Zh_tw": "綠線",
      "En": "綠線"
    },
    "SubRouteUID": "HSZ073901",
    "SubRouteID": "073901",
    "SubRouteName": {
      "Zh_tw": "綠線",
      "En": "綠線"
    },
    "Direction": 0,
    "BusPosition": {
      "PositionLon": 120.984245,
      "PositionLat": 24.8149733333333,
      "GeoHash": "wsqj1j6j9"
    },
    "Speed": 51,
    "Azimuth": 264,
    "DutyStatus": 1,
    "BusStatus": 0,
    "MessageType": 1,
    "GPSTime": "2021-07-04T15:24:27+08:00",
    "SrcRecTime": "2021-07-04T15:24:29+08:00",
    "SrcTransTime": "2021-07-04T15:24:30+08:00",
    "UpdateTime": "2021-07-04T15:24:34+08:00"
  }
  ]

