resource "aws_lambda_function" "patent_s3_dynamodb" {
  filename     =  "dbbuild/s3_patent_function.zip"
  function_name = "patent-s3-dynamodb"
  role          = local.iam_role  
  handler       = "lambda_function.lambda_handler"
  timeout       = 900
  runtime       = "python3.9"
  layers        = [aws_lambda_layer_version.lambda_layer.arn]
  source_code_hash = filebase64sha256("dbbuild/s3_patent_function.zip")


  environment {
    variables = {
      PATENTS_TABLE_NAME = aws_dynamodb_table.patent_dynamodb_table.name
    }
  }
}