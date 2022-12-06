from typing import Union
from fastapi import FastAPI, HTTPException
import uvicorn
from dynamodb_repository import  get_patent_data, get_list_of_patent

app = FastAPI()


@app.get("/")
def health():
    return {"health": "OK"}


@app.get("/patent")
def patent_list(query: str= "", exclusivestartkey:Union[str, None]= None,limit: int = 20):
    return get_list_of_patent(query,exclusivestartkey,limit)
 
@app.get("/patent/{patent_id}")
def get_patent(patent_id):
    try:
        return get_patent_data(patent_id)
    except Exception as exception:
        print(exception)
        raise HTTPException(status_code=404, detail="Patent with id " + patent_id + " not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
