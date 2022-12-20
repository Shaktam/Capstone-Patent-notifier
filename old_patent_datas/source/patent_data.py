import re
import time
import pandas as pd
import requests
import json
from api_ids import get_base_data, get_id, store_first_element,ids_for_url

def get_patent_content(id):
    baseurl='https://api.patentsview.org/patents/query?q={"patent_id":'
    field = '}&f=["patent_id","patent_title","patent_abstract","assignee_organization","patent_date"]'
    url =baseurl+'"'+ str(id).strip()+'"'+field
    print(url)
    response = requests.get(url)
    return json.loads(response.content.decode('utf-8')) 

def get_organization(patent):
    get_organisation_data = "" if 'assignee_organization'== None else [assignee['assignee_organization']for assignee in patent['assignees']]
    organisation_string=json.dumps(get_organisation_data)
    remove_bracket_from_string=re.sub(r'[\[\]]', r'', organisation_string)
    return remove_bracket_from_string.replace('"','')

def get_patent_datas(file):
    file = open("patent.csv", "r")
    patent_data=[]  
    for id in file:
        obj_data=get_patent_content(id)
        for patent in obj_data['patents']:
            organization=get_organization(patent)
            list_data ={
                "patent_id":patent['patent_id'],
                "title":patent['patent_title'],
                "abstract":patent['patent_abstract'],
                "patent_date":patent['patent_date'],
                "organization":organization
                }
        patent_data.append(list_data)
        time.sleep(1) 
    return patent_data  

def create_csv_file(patent_data):
    df = pd.DataFrame(patent_data)
    df.to_csv('patent_datas.csv', index=False)
    df_csv = pd.read_csv('patent_datas.csv')
    return df_csv

      
