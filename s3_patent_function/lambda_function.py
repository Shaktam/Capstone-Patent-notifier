import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
patent_Table = dynamodb.Table('Patent-dynamodb-table')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file_name = event['Records'][0]['s3']['object']['key']
    csv_object = s3_client.get_object(Bucket=bucket,Key=csv_file_name)
    csv_file_reader = csv_object['Body'].read().decode("utf-8")
    datas = csv_file_reader.split("\n")
    datas = list(filter(None, datas))
    for patent_records in datas:
        patent_data = patent_records.split(",")
        patent_Table.put_item(Item = {
            "patent_id":patent_data[0],
            "title":patent_data[1],
            "abstract":patent_data[2],
            "patent_date":patent_data[3],
            "organization":patent_data[4]
        })
    return 'success'

if __name__ == "__main__":
    lambda_handler({},{})   