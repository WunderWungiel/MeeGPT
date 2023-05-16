import json
import urllib.request
from urllib.error import HTTPError, URLError


def api(query, model="gpt-3.5-turbo"):
    link = "<api_instance>"
    api = "<api_key>"

    headers = {
        'Authorization': 'Bearer {}'.format(api),
        'Content-Type': 'application/json',
        'Referer': 'https://www.google.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows'
    }
    data = {
        "model": model,
        "max_tokens": 2048,
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
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
