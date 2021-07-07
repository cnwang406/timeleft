import requests

# Install the Python Requests library:
# `pip install requests`


def send_request(headers, url, routeName):
    # Request
    # GET https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/Streaming/City/Hsinchu

    try:
        response = requests.get(
            url=url + '/' + routeName,
            params={
                "$top": "30",
                "$format": "JSON",
                # "$filter": "RouteID eq '0739'",
            },
            headers=headers,
        )
        return response.status_code, response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return 404, ''
