import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
Patent_data_name = "patent_dynamodb_table"
Patent_Table = dynamodb.Table(Patent_data_name)

def save_patent_to_db(data):
    Patent_Table.put_item(Item = data)

def save_patent_datas(patent_data):
    for data in patent_data:
        save_patent_to_db(data)
