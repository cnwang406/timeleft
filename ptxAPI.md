ptxAPI.md
```
BusA1Data {
PlateNumb (String): 車牌號碼 ,
OperatorID (String, optional): 營運業者代碼 ,
RouteUID (String, optional): 路線唯一識別代碼，規則為 {業管機關簡碼} + {RouteID}，其中 {業管機關簡碼} 可於Authority API中的AuthorityCode欄位查詢 ,
RouteID (String, optional): 地區既用中之路線代碼(為原資料內碼) ,
RouteName (NameType, optional): 路線名稱 ,
SubRouteUID (String, optional): 子路線唯一識別代碼，規則為 {業管機關簡碼} + {SubRouteID}，其中 {業管機關簡碼} 可於Authority API中的AuthorityCode欄位查詢 ,
SubRouteID (String, optional): 地區既用中之子路線代碼(為原資料內碼) ,
SubRouteName (NameType, optional): 子路線名稱 ,
Direction (Int32, optional): 去返程 : [0:'去程',1:'返程',2:'迴圈',255:'未知'] ,
BusPosition (PointType, optional): 車輛位置經度 ,
Speed (number, optional): 行駛速度(kph) ,
Azimuth (number, optional): 方位角 ,
DutyStatus (Int32, optional): 勤務狀態 : [0:'正常',1:'開始',2:'結束'] ,
BusStatus (Int32, optional): 行車狀況 : [0:'正常',1:'車禍',2:'故障',3:'塞車',4:'緊急求援',5:'加油',90:'不明',91:'去回不明',98:'偏移路線',99:'非營運狀態',100:'客滿',101:'包車出租',255:'未知'] ,
MessageType (Int32, optional): 資料型態種類 : [0:'未知',1:'定期',2:'非定期'] ,
GPSTime (DateTime): 車機時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz) ,
TransTime (string, optional): 車機資料傳輸時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz)[多數單位沒有提供此欄位資訊] ,
SrcRecTime (string, optional): 來源端平台接收時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz) ,
SrcTransTime (string, optional): 來源端平台資料傳出時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz)[公總使用動態即時推播故有提供此欄位, 而非公總系統因使用整包資料更新, 故沒有提供此欄位] ,
SrcUpdateTime (string, optional): 來源端平台資料更新時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz)[公總使用動態即時推播故沒有提供此欄位, 而非公總系統因提供整包資料更新, 故有提供此欄] ,
UpdateTime (DateTime): 本平台資料更新時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz)
}
```◊