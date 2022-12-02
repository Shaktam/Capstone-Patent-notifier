from main import get_patent_ids
from api_data import store_only_ids,get_patent_datas
from dynamodb_data import save_patent_datas

def lambda_handler(event,context):
    patent_id= get_patent_ids()
    store_patent_id=store_only_ids(patent_id)
    patent_data=get_patent_datas(store_patent_id)
    return save_patent_datas(patent_data)

if __name__ == "__main__":
    lambda_handler({},{})
    