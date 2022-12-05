import json
import re
import requests

def get_id(patent_id_list):
    store_patent_id=[]
    for patent_id in patent_id_list:
        store_patent_id.append(patent_id['patent_id'])  
    return store_patent_id

def get_patent(id):
    baseurl='https://api.patentsview.org/patents/query?q={"patent_id":'
    field = '}&f=["patent_id","patent_title","patent_abstract","assignee_organization","patent_date"]'
    url= baseurl +str(id) + field
    response = requests.get(url)
    return json.loads(response.content.decode('utf-8'))

def get_organization(patent):
    get_organisation_data = "" if 'assignee_organization'== None else [assignee['assignee_organization']for assignee in patent['assignees']]
    organisation_string=json.dumps(get_organisation_data)
    remove_bracket_from_string=re.sub(r'[\[\]]', r'', organisation_string)
    return remove_bracket_from_string.replace('"','')

def get_patent_datas(stored_patent_id):
    patent_data=[]  
    for id in stored_patent_id:
        obj_data=get_patent(id)
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
        print(patent_data)    
    return patent_data
