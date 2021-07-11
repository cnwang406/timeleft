ptxAPIService.md
Implementation Notes
取得營運通阻資料
Response Class (Status 200)
Success
ModelExample Value
TRAAlertList {
UpdateTime (string): 本平台資料更新時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz) ,
UpdateInterval (Int32): 本平台資料更新週期(秒) ,
SrcUpdateTime (DateTime): 來源端平台資料更新時間(ISO8601格式:yyyy-MM-ddTHH:mm:sszzz) ,
SrcUpdateInterval (Int32): 來源端平台資料更新週期(秒)['-1: 不定期更新'] ,
AuthorityCode (String): 業管機關簡碼 ,
Alerts (Array[Alert]): 資料(陣列) ,
Count (integer, optional): 資料總筆數
}
Alert {
AlertID (String): 通阻訊息代碼 ,
Title (String): 通阻訊息標題 ,
Description (String): 通阻訊息說明 ,
Status (Int32): 營運狀況 : [0:'全線營運停止',1:'全線營運正常',2:'有異常狀況'] ,
Scope (AlertScope): 影響範圍 ,
Direction (Int32, optional): 影響方向 : [0:'南下',1:'北上',2:'雙向'] ,
Level (Int32, optional): 影響等級程度 : [1:'重度',2:'中度',3:'輕度'] ,
Effect (String, optional): 影響說明 ,
Reason (String, optional): 影響原因 ,
AlertURL (String, optional): 通阻訊息網址連結 ,
StartTime (string, optional): 訊息起始日期時間 ,
EndTime (string, optional): 訊息結束日期時間 ,
PublishTime (string, optional): 消息發佈日期時間 ,
UpdateTime (DateTime): 消息更新日期時間
}
AlertScope {
NetworkList (AlertScopeNetwork, optional): 受影響的路網 ,
Stations (Array[AlertScopeStation]): 受影響的車站 ,
Lines (Array[AlertScopeLine]): 受影響的實體路線 ,
Routes (Array[AlertScopeRoute]): 受影響的營運路線 ,
Trains (Array[AlertScopeTrain]): 受影響的車次 ,
LineSections (Array[AlertScopeLineSection]): 受影響的路線區間
}
AlertScopeNetwork {
NetworkID (String, optional): 路網代碼 ,
NetworkName (String, optional): 路網名稱
}
AlertScopeStation {
StationID (String, optional): 車站代碼 ,
StationName (String, optional): 車站名稱
}
AlertScopeLine {
LineID (String, optional): 實體路線代碼 ,
LineName (String, optional): 實體路線名稱
}
AlertScopeRoute {
RouteID (String, optional): 營運路線代碼 ,
RouteName (String, optional): 營運路線名稱
}
AlertScopeTrain {
TrainNo (String, optional): 受影響的車次
}
AlertScopeLineSection {
LineID (String, optional): 路線區間所在路線代碼 ,
StartingStationID (String, optional): 區間起站車站代碼 ,
StartingStationName (String, optional): 區間起站車站名稱 ,
EndingStationID (String, optional): 區間迄站車站代碼 ,
EndingStationName (String, optional): 區間迄站車站名稱 ,
Description (String, optional): 影響區間輔助描述
}