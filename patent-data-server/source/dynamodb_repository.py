from re import search
import boto3
from boto3.dynamodb.conditions import Attr, Or

dynamodb = boto3.resource('dynamodb')
patent_Table = dynamodb.Table('Patent-dynamodb-table')

def get_patent_data(patent_id):

    response = patent_Table.get_item(
        Key={
            'patent_id': patent_id
        }
    )
    return response['Item']
  
def get_list_of_patent(search,exclusivestartkey,limit):
    filter_expression=Or(Attr('title').contains(search),Attr('abstract').contains(search))
    response = patent_Table.scan(
        Limit = limit,
        FilterExpression=filter_expression,
        ExclusiveStartKey= {"patent_id":exclusivestartkey}
    ) if exclusivestartkey is not None else patent_Table.scan(Limit = limit,FilterExpression = filter_expression) 
                    
    return {'items' :response['Items'],
           'LastEvaluatedKey': response['LastEvaluatedKey']}  

def get_patentdata_of_organization(search,limit):
    filter_expression=Attr('organization').contains(search)
    response = patent_Table.scan(
        Limit = limit,
        FilterExpression=filter_expression 
    ) 
                    
    return {
        'items' :response['Items']  
           }  
           