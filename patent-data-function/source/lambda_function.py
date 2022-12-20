from dynamodb_data import save_patent_datas
from main import get_base_data, store_first_element,ids_for_url,get_ids
from api_data import get_patent_datas

def lambda_handler(event,context):
    store_first_element()
    patent_ids=get_base_data(ids_for_url)
    stored_patent_id=get_ids(patent_ids)
    patent_data=get_patent_datas(stored_patent_id)
    return save_patent_datas(patent_data)

if __name__ == "__main__":
    lambda_handler({},{})
