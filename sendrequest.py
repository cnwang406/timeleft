import requests

# Install the Python Requests library:
# `pip install requests`


def send_request(headers, url):
    # Request
    # GET https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/Streaming/City/Hsinchu

    try:
        response = requests.get(
            url=url,
            params={
                "$top": "30",
                "$format": "JSON",
                "$filter": "RouteID eq '0739'",
            },
            headers=headers,
        )
        #print('Response HTTP Status Code: {status_code}'.format(    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(content=response.content))
        return response.status_code, response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return 404, ''
