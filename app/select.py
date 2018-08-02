import requests
import json

# defining the api-endpoint, App 목록 조회
URL = 'http://112.216.38.190:9180/openapi/app/select'

# your API key here
API_KEY = 'acroCbs'

# defining the http header
HEADER = {'Content-Type': 'application/json', 'token': API_KEY}

# data to be sent to api
send_body = {'appName': ''}

# sending post request and saving response as response object
res = requests.post(url=URL, data=json.dumps(send_body), headers=HEADER)

# status_code - 200: 성공, '400': 요청오류, '401': 권한오류, '500': 내부오류
if res.status_code == 200:
    recv_body = dict(res.json())
    # extracting response data
    print(recv_body.get('resultCode'))
    print(recv_body.get('message'))
    print(recv_body.get('txDate'))
    print(recv_body.get('totalPage'))
    print(recv_body.get('totalCount'))
    print(recv_body.get('rowPerPage'))
    print(recv_body.get('currentPage'))
    if recv_body.get('resultCode') == 'SUCCESS':
        print(recv_body.get('data'))
