import json
import urllib.request
from urllib.error import HTTPError, URLError


def api(query):

    data = json.dumps(data).encode('utf-8')
    request = urllib.request.Request(link, data=data, headers=headers)
    try:
        response = urllib.request.urlopen(request)
    except (HTTPError, URLError) as e:
        return "Error"

    response_data = response.read().decode('utf-8')
    try:
        response_dict = json.loads(response_data)
    except:
        response_dict = response_data
    return response_dict
