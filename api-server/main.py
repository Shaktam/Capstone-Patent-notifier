import requests
import json
api_url_base = 'https://search.patentsview.org/api/v1/patent/10757852/'
api_token = 'n8eiYbx8.oyBat24OZjTDA40SZ09tKrTvTiqgImye'

headers = {'content-type' : 'application/json',
'X-CSRFToken': 'zPZwOFHnynLs69FHTvhPeb868YPutic9hnTCz9WwK2HyIF0MMDAYkIJ9sUVa6juG',
    'X-Api-Key': 'n8eiYbx8.oyBat24OZjTDA40SZ09tKrTvTiqgImye'}
auth_response = requests.get(api_url_base, headers=headers)
response=json.loads(auth_response.content.decode('utf-8'))
print(response)
