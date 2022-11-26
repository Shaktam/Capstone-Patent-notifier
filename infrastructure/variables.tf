variable "aws_region" {
    type = string
    default = "us-west-2"
}

locals {
  account_id = data.aws_caller_identity.current.account_id
  iam_role   = join(":", ["arn:aws:iam:", local.account_id, "role/LabRole"])
}
