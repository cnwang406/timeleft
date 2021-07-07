
from PTXauth import Auth as PTXAuth
from common import AUTH_USERNAME, AUTH_KEY, PTX_URL, MY_LOCATION, ROUTE_NAME, TRA_URL, TRA_StationID
from sendrequest import send_request
from ptx import ptx_response_from_dict, statusString, dutyString
from tra import tra_response_from_dict
from geodistance import geoDistance


def showBus(bus):
    print(
        f'bus {bus.route_name.zh_tw} ({bus.plate_numb}) at [{bus.bus_position.position_lat:9.6},{bus.bus_position.position_lon:9.6}] with speed {bus.speed} km/h')
    print(
        f' distance {geoDistance(MY_LOCATION, [bus.bus_position.position_lat,bus.bus_position.position_lon] ):5.3} km, azimuth {bus.azimuth}')
    print(
        f' direction is {"香山往經國路" if bus.direction == 1 else "經國路往香山" }, transtime {bus.src_trans_time} status:{dutyString(bus.duty_status)}/{statusString(bus.bus_status)}')


def getService():

    ptxAuth = PTXAuth(AUTH_USERNAME, AUTH_KEY)

    resultCode, buses = send_request(
        ptxAuth.get_auth_header(), PTX_URL, ROUTE_NAME)
    if resultCode == 200:
        for bus in ptx_response_from_dict(buses):
            showBus(bus)
    resultCode, trains = send_request(
        ptxAuth.get_auth_header(), TRA_URL, TRA_StationID)
    if resultCode == 200:
        # for train in tra_response_from_dict(trains):
        print(trains)
