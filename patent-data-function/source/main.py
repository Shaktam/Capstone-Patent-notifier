import requests
import logging
import json
import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
import time
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_url='https://search.patentsview.org/api/v1/patent/?q={"_gte":{"patent_year":2023}}&f=["patent_id"]&o={"size":1000,"after":' 
PATENT_CSRF_TOKEN= os.getenv("PATENT_CSRF_TOKEN")
PATENT_API_KEY =  os.getenv("PATENT_API_KEY")
headers = {'content-type' : 'application/json',
            'X-CSRFToken': PATENT_CSRF_TOKEN,
            'X-Api-Key': PATENT_API_KEY}

ids_for_url= []  
def store_first_element():
    ids_for_url.append(0)

def get_last_ids(patent_id_list):
    if len(patent_id_list) > 0 and patent_id_list[-1].get('patent_id') is not None:
        last_patent_id = patent_id_list[-1]['patent_id']  
        last_id_string=json.dumps(last_patent_id)
        return ids_for_url.append(last_id_string)   
    
def get_base_data(ids_for_url): 
    patent_ids=[] 
    for ids in ids_for_url: 
        api_url_base =api_url + str(ids)+'}'
        auth_response = requests.get(api_url_base, headers=headers)
        patent_id_list=json.loads(auth_response.content.decode('utf-8'))#["patents"]  
        if "patents" in patent_id_list:
            patent_ids.extend(patent_id_list["patents"])      
            ids_for_url=get_last_ids(patent_id_list["patents"]) 
        else:
            print("patent not found")  
# time.sleep is only used because of limitation of requests per minute.
# In real time when we have full access, use the file without timesleep              
        time.sleep(1)
    return patent_ids                   

def get_ids(patent_ids):
    store_patent_ids=[]
    for patent_id in patent_ids:
        store_patent_ids.append(patent_id['patent_id'])      
    return store_patent_ids
    