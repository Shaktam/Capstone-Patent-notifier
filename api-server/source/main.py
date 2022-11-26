import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_url_base = 'https://search.patentsview.org/api/v1/patent/?q={"patent_year":"2020"}&f=["patent_id"]'
PATENT_CSRF_TOKEN= os.getenv("PATENT_CSRF_TOKEN")
PATENT_API_KEY =  os.getenv("PATENT_API_KEY")

def get_patent_ids():

    headers = {'content-type' : 'application/json',
               'X-CSRFToken': PATENT_CSRF_TOKEN,
               'X-Api-Key': PATENT_API_KEY}
    auth_response = requests.get(api_url_base, headers=headers)
    response=json.loads(auth_response.content.decode('utf-8'))["patents"]
    return response
    
patent_id= get_patent_ids()

def write_json_file(patent_id):
    with open("get_patent_id.json", "w") as file:
        file.write(json.dumps(patent_id))
write_json_file(patent_id)  