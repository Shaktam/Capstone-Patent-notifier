from dynamodb_patentdata import save_patent_datas
from get_data import get_patent_datas, store_only_ids
from get_account import get_patent_ids

def handler(event, context):
    patent_id= get_patent_ids()
    stored_patent_id=store_only_ids(patent_id)
    patent_data=get_patent_datas(store_patent_id)
    save_patent_datas(patent_data)
    print(patent_data)

if __name__ == "__main__":
    handler({},{})
