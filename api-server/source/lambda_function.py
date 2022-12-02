from dynamodb_data import save_patent_datas
from api_data import get_patent_datas,get_id
from main import get_patent_ids

def lambda_handler(event,context):
    patent_id_list=get_patent_ids()
    stored_patent_id=get_id(patent_id_list)
    patent_data=get_patent_datas(stored_patent_id)
    return save_patent_datas(patent_data)

if __name__ == "__main__":
    lambda_handler({},{})
