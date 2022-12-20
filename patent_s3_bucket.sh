S3_BUCKET_NAME=$1
REGION=us-west-2
if aws s3 ls "s3://$S3_BUCKET_NAME" 2>&1 | grep -q 'An error occurred'
then
    aws s3api create-bucket --bucket $S3_BUCKET_NAME --region $REGION --create-bucket-configuration LocationConstraint=$REGION
else
    echo "bucket $S3_BUCKET_NAME already exists"
fi
