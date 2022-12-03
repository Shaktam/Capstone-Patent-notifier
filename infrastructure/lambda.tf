resource "aws_lambda_function" "patent_lambda_crawler" {
  filename     = "dbbuild/api-server.zip"
  function_name = "patent-lambda-crawler"
  role          = local.iam_role  
  handler       = "lambda_function.lambda_handler"
  timeout       = 300
  runtime       = "python3.9"
  layers        = [aws_lambda_layer_version.lambda_layer.arn]
  source_code_hash = filebase64sha256("dbbuild/api-server.zip")

  environment {
    variables = {
      PATENTS_TABLE_NAME = aws_dynamodb_table.patent_dynamodb_table.name
    }
  }
}

resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "dbbuild/requests_layer.zip"
  layer_name = "lambda_layer"
  compatible_runtimes = ["python3.9"]
}

resource "aws_cloudwatch_event_rule" "every_five_minutes" {
    name = "every-five-minutes"
    description = "Fires every five minutes"
    schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "job_crawler_every_five_minutes" {
    rule = aws_cloudwatch_event_rule.every_five_minutes.name
    target_id = "crawl-jobs"
    arn = aws_lambda_function.job_crawler.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_job_crawler" {
    statement_id = "AllowExecutionFromCloudWatch"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.job_crawler.function_name
    principal = "events.amazonaws.com"
    source_arn = aws_cloudwatch_event_rule.every_five_minutes.arn
}