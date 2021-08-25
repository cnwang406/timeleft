import requests

# Install the Python Requests library:
# `pip install requests`


def send_request(headers, url, routeName=''):
    try:
        response = requests.get(
            url=url + '/' + routeName,
            params={
                "$top": "30",
                "$format": "JSON"
            },
            headers=headers,
        )
        return response.status_code, response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return 404, ''
