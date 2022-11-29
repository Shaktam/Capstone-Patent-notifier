resource "aws_dynamodb_table" "patent_dynamodb_table" {
  name             = "Patent-dynamodb-table"
  hash_key         = "patent_id"
  range_key        = "assignee_organization"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
  billing_mode     = "PROVISIONED"
  read_capacity    = 100
  write_capacity   = 100

  attribute {
    name = "patent_id"
    type = "N"
  }

  attribute {
    name = "assignee_organization"
    type = "S"
  }
    tags = {
    Name        = "Patent-dynamodb-table"
  }
}
