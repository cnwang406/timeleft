
from PTXauth import Auth as PTXAuth
from common import AUTH_USERNAME, AUTH_KEY, PTX_URL, MY_LOCATION, ROUTE_NAME, TRA_TB_URL, TRA_StationID, TRA_LIVE_URL
from sendrequest import send_request
from ptxbus import ptxbus_response_from_dict, ptxbus_statusString, ptxbus_dutyString
from ptxtratb import ptxtra_response_from_dict
from ptxtralive import tra_liveboard_response_from_dict, tra_liveboard_TrainTypeCode as trainTypeCode, tra_liveboard_running_status as runningStatus
from geodistance import geoDistance


def showBus(bus):
    print(
        f'bus {bus.route_name.zh_tw} ({bus.plate_numb}) at [{bus.bus_position.position_lat:9.6},{bus.bus_position.position_lon:9.6}] 時速 {bus.speed} km/h')
    print(
        f' 距離 {geoDistance(MY_LOCATION, [bus.bus_position.position_lat,bus.bus_position.position_lon] ):5.3} km, 開向 {bus.azimuth}度')
    print(
        f' direction is {"香山往經國路" if bus.direction == 1 else "經國路往香山" }, transtime {bus.src_trans_time} status:{ptxbus_dutyString(bus.duty_status)}/{ptxbus_statusString(bus.bus_status)}')


def showLiveboard(train):
    if train.station_name.zh_tw != train.ending_station_name.zh_tw:
        print(f'車號 {train.train_no:5}({trainTypeCode(train.train_type_code):3}) 往 {train.ending_station_name.zh_tw}({"順" if train.direction else "逆"}), 預計離站 {train.schedule_departure_time}, 延誤 {train.delay_time:3} min, status = {runningStatus(train.running_status)}')


def getService():

    ptxAuth = PTXAuth(AUTH_USERNAME, AUTH_KEY)
    print("=====  BUS  =====")
    resultCode, buses = send_request(
        ptxAuth.get_auth_header(), PTX_URL, ROUTE_NAME)
    if resultCode == 200:
        for bus in ptxbus_response_from_dict(buses):
            showBus(bus)
    print()
    print("===== TRAIN =====")
    resultCode, trains = send_request(
        ptxAuth.get_auth_header(), TRA_LIVE_URL, TRA_StationID)
    if resultCode == 200:
        for train in tra_liveboard_response_from_dict(trains).station_live_boards:
            showLiveboard(train)
