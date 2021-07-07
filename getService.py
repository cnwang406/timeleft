
from auth import Auth
from common import AUTH_USERNAME, AUTH_KEY, PTX_URL, MY_LOCATION
from sendrequest import send_request
from ptx import welcome_from_dict
from geodistance import geoDistance


def getService():

    auth = Auth(AUTH_USERNAME, AUTH_KEY)

    resultCode, resultData = send_request(auth.get_auth_header(), PTX_URL)
    if resultCode == 200:
        for data in welcome_from_dict(resultData):
            print(
                f'bus {data.route_name.zh_tw} ({data.plate_numb}) at [{data.bus_position.position_lat:9.6},{data.bus_position.position_lon:9.6}] with speed {data.speed} km/h')
            print(
                f' distance {geoDistance(MY_LOCATION, [data.bus_position.position_lat,data.bus_position.position_lon] ):5.3} km, azimuth {data.azimuth}')
            print(
                f' direction is {data.direction}, transtime {data.src_trans_time}')
