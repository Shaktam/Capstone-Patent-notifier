resource "aws_lambda_function" "patent_lambda_crawler" {
  filename     = "dbbuild/api-server.zip"
  function_name = "patent-lambda-crawler"
  role          = local.iam_role  
  handler       = "patent.handler"
  timeout       = 300
  runtime       = "python3.9"
  source_code_hash = filebase64sha256("dbbuild/apis.zip")

  environment {
    variables   = {
      TOPIC_ARN = aws_sns_topic.patent_email.arn
    }
  }
}

resource "aws_lambda_event_source_mapping" "patent_table_update" {
  event_source_arn  = aws_dynamodb_table.patent_dynamodb_table.stream_arn
  function_name     = aws_lambda_function.patent_lambda_crawler.arn
  starting_position = "LATEST"
}
