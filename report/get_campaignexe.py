import requests
import json

# defining the api-endpoint, 전체 캠페인 발송 상세
URL = 'http://112.216.38.190:9180/openapi/report/get/campaignExe'

# your API key here
API_KEY = 'acroCbs'

# defining the http header
HEADER = {'Content-Type': 'application/json', 'token': API_KEY}

# data to be sent to api
send_body = {'campExeKey': ''}

# sending post request and saving response as response object
res = requests.post(url=URL, data=json.dumps(send_body), headers=HEADER)

# status_code - 200: 성공, '400': 요청오류, '401': 권한오류, '500': 내부오류
if res.status_code == 200:
    # extracting response data
    recv_body = dict(res.json())
    print(recv_body.get('resultCode'))
    print(recv_body.get('message'))
    print(recv_body.get('txDate'))
    if recv_body.get('resultCode') == 'SUCCESS':
        print(recv_body.get('data'))
