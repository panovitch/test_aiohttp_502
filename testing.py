code = 0

import requests

while code != 502:
    response = requests.get('http://127.0.0.1/test/')
    code = response.status_code
    print(response)
