from typing import Union
from fastapi import FastAPI, HTTPException
import uvicorn
from dynamodb_repository import  get_patent_data, get_list_of_patent,get_patentdata_of_organization
app = FastAPI()

@app.get("/")
def health():
    return {"health": "OK"}

@app.get("/patent")
def patent_list(search:str= "", exclusivestartkey:Union[str, None]= None,limit: int = 20):
    id= get_list_of_patent(search,exclusivestartkey,limit)
    org= get_patentdata_of_organization(search,limit)
    if id==org:
        return id
    else:
        return (id,org)    

@app.get("/patent/{patent_id}")
def get_patent(patent_id):
    try:
        return get_patent_data(patent_id)
    except Exception as exception:
        print(exception)
        raise HTTPException(status_code=404, detail="Patent with id " + patent_id + " not found")

@app.get("/patent/{organization}")
def get_patent(organization):
    try:
        return get_patent_data(organization)
    except Exception as exception:
        print(exception)
        raise HTTPException(status_code=404, detail="Patent with " + organization + " not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
