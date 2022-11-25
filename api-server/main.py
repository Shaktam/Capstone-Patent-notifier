import requests
import json
api_url_base = 'https://search.patentsview.org/api/v1/patent/?q={"_and":[{"_gte":{"patent_date":"2006-01-01"}}]}'
headers = {'content-type' : 'application/json'}
auth_response = requests.get(api_url_base, headers=headers)
response=json.loads(auth_response.content.decode('utf-8'))
print(response)
