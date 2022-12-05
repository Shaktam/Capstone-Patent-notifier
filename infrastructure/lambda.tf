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

resource "aws_lambda_event_source_mapping" "patent_table_update" {
  event_source_arn  = aws_dynamodb_table.patent_dynamodb_table.stream_arn
  function_name     = aws_lambda_function.patent_lambda_crawler.arn
  starting_position = "LATEST"
}
