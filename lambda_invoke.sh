PATENT_FUNCTION="Patent Lambda Crawler Function"
NOTIFIER_FUNCTION="Patent Notifier"

echo "Adding Permission for $PATENT_FUNCTION URL"
aws lambda add-permission --function-name patent-lambda-crawler --action lambda:InvokeFunctionUrl --principal "*" --function-url-auth-type "AWS_IAM" --statement-id url

echo "Creating $PATENT_FUNCTION  URL"
aws lambda create-function-url-config --function-name patent-lambda-crawler --auth-type AWS_IAM

echo "Configuring test-event for $PATENT_FUNCTION and running the code"
aws lambda invoke --function-name patent-lambda-crawler --region us-west-2 --cli-binary-format raw-in-base64-out --cli-read-timeout 900 --payload file://dynamodb_payload.json response.json

echo"Adding Permission for $NOTIFIER_FUNCTION URL"
aws lambda add-permission --function-name notifer --action lambda:InvokeFunctionUrl --principal "*" --function-url-auth-type "AWS_IAM" --statement-id url

echo "Creating $NOTIFIER_FUNCTION URL"
aws lambda create-function-url-config --function-name notifer --auth-type AWS_IAM

echo "Configuring test-event for $NOTIFIER_FUNCTION and running the code"
aws lambda invoke --function-name notifer --region us-west-2 --cli-binary-format raw-in-base64-out --cli-read-timeout 600 --payload file://sns_payload.json response.json
