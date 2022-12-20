from api_ids import get_base_data, store_first_element,ids_for_url,create_csv_file,get_ids
from patent_data import file, get_patent_datas

def collection_of_patent_datas():
    store_first_element() 
    patent_ids=get_base_data(ids_for_url)  
    stored_patent_ids=get_ids(patent_ids)
    create_csv_file(stored_patent_ids)
    patent_data= get_patent_datas()
    return create_csv_file(patent_data)
data=collection_of_patent_datas()
