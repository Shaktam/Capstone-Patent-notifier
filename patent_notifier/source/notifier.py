import boto3
import os

client = boto3.client('sns')

topic_arn = os.getenv("TOPIC_ARN")
notification_topic="google"
def inform_about_new_patent(title, abstract,organization):
    client.publish(
        TopicArn=topic_arn,
        Message= "New Patent: "+ title +" \n "+abstract + "\n"+ organization,
        Subject='New Patent: ' + title
    )

def handle_new_image(newImage):
    title = newImage["title"]["S"]
    abstract = newImage["abstract"]["S"]
    if notification_topic in title.lower() or notification_topic in abstract.lower():
        inform_about_new_patent(title, abstract)


def handle_record(record):
    if "NewImage" in record["dynamodb"]:
        handle_new_image(record["dynamodb"]["NewImage"])


def handler(event, context):
    for record in event["Records"]:
        handle_record(record)
