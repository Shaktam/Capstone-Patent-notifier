import requests
from main import get_patent_ids

patent_id= get_patent_ids()

store_patent_id=[]
def store_only_ids(patent_id):
    for patent_ids in patent_id:
        store_patent_id.append((patent_ids['patent_id']))
    return store_patent_id

store_patent_id=store_only_ids(patent_id)

def get_patent_datas(store_patent_id):

    baseurl='https://api.patentsview.org/patents/query?q={"patent_id":'
    field = '}&f=["patent_id","patent_title","patent_abstract","assignee_organization","patent_date"]'

    patent_data=[]

    for id in store_patent_id:
        url= baseurl+ id +field
        r = requests.get(url)
        json_patent_data = r.json()
        patent_data.append(json_patent_data)
    return patent_data

get_patent_datas(store_patent_id)
