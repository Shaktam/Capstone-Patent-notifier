resource "aws_sns_topic" "patent_email" {
  name = "Patent-email-Notification"
}

resource "aws_sns_topic_subscription" "patent_update_notification" {
  topic_arn = aws_sns_topic.patent_email.arn
  protocol  = "email"
  endpoint  = var.sns_email
}
