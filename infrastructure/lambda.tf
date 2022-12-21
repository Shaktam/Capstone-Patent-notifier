resource "aws_lambda_function" "patent_lambda_crawler" {
  filename     = "dbbuild/patent-data-function.zip"
  function_name = "patent-lambda-crawler"
  role          = local.iam_role  
  handler       = "lambda_function.lambda_handler"
  timeout       = 900
  runtime       = "python3.9"
  layers        = [aws_lambda_layer_version.lambda_layer.arn]
  source_code_hash = filebase64sha256("dbbuild/patent-data-function.zip")

  environment {
    variables = {
      PATENTS_TABLE_NAME = aws_dynamodb_table.patent_dynamodb_table.name
      PATENT_CSRF_TOKEN =var.PATENT_CSRF_TOKEN
      PATENT_API_KEY=var.PATENT_API_KEY
    }
  }
}

resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "dbbuild/requests_layer.zip"
  layer_name = "lambda_layer"
  compatible_runtimes = ["python3.9"]
}

resource "aws_cloudwatch_event_rule" "every_hour" {
    name = "every_hour"
    description = "Fires every hour"
    schedule_expression = "rate(60 minutes)"
}

resource "aws_cloudwatch_event_target" "patent_crawler_every_hour" {
    rule = aws_cloudwatch_event_rule.every_hour.name
    target_id = "patent-informer"
    arn = aws_lambda_function.patent_lambda_crawler.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_patent_crawler" {
    statement_id = "AllowExecutionFromCloudWatch"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.patent_lambda_crawler.function_name
    principal = "events.amazonaws.com"
    source_arn = aws_cloudwatch_event_rule.every_hour.arn
}
