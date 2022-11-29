import boto3

AWS_REGION = "us-west-2"
s3 = boto3.resource('s3')
client = boto3.client('s3',region_name=AWS_REGION)
location = {'LocationConstraint': AWS_REGION}
statefiles3='terraform-state-dynodb-patent'
dynamodb_bucket='patent-notifier-dynodb'
patent_id_bucket='patent-json-id-bucket'


def backend_tfbucket():
    if s3.Bucket(f'{statefiles3}') in s3.buckets.all():
        print(f" Bucket {statefiles3} Exists!")
        return True
    else:
        client.create_bucket(Bucket=statefiles3,CreateBucketConfiguration=location)
        print(f"Created a new bucket while bucket {statefiles3} does not exist!")
        return False
        
backend_tfbucket()
