import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
patent_Table = dynamodb.Table('patent_dynamodb_table')

def save_patent_to_db(data):
    patent_Table.put_item(Item = data)

def save_patent_datas(patent_data):
    for data in patent_data:
        save_patent_to_db(data)
