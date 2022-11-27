import boto3

AWS_REGION = "us-west-2"
s3 = boto3.resource('s3')
client = boto3.client('s3',region_name=AWS_REGION)
location = {'LocationConstraint': AWS_REGION}
statefiles3='terraform-state-dynodb-patent'

def backend_tfbucket():
    if s3.Bucket(f'{statefiles3}') in s3.buckets.all():
        print(f" {statefiles3} Exists!")
        return True
    else:
        client.create_bucket(Bucket=statefiles3,CreateBucketConfiguration=location)
        print(f"Created a new bucket while bucket {statefiles3} does not exist!")
        return False

backend_tfbucket()