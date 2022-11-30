resource "aws_lambda_function" "patent_lambda_crawler" {
  filename     = "dbbuild/apis.zip"
  function_name = "patent-lambda-crawler"
  role          = local.iam_role  
  handler       = "patent.handler"
  timeout       = 300
  runtime       = "python3.9"
  source_code_hash = filebase64sha256("dbbuild/apis.zip")

  environment {
    variables = {
      PATENT_TABLE_NAME = aws_dynamodb_table.patent_dynamodb_table.name
    }
  }
}

resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "dbbuild/requests-layer.zip"
  layer_name = "lambda_layer_name"

  compatible_runtimes = ["python3.9"]
}
