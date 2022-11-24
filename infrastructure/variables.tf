variable "region_number" {
  # Arbitrary mapping of region name to number to use in
  # a VPC's CIDR prefix.
  default = {
    us-west-2      = 1
  }
}

variable "az_number" {
  # Assign a number to each AZ letter used in our configuration
  default = {
    a = 1
    b = 2
    c = 3
    d = 4
  }
}
# Retrieve the AZ where we want to create network resources
# This must be in the region selected on the AWS provider.
data "aws_availability_zone" "az_a" {
   name = "us-west-2a"
}

data "aws_availability_zone" "az_b" {
  name = "us-west-2b"
}

data "aws_availability_zone" "az_c" {
  name = "us-west-2c"
}

data "aws_availability_zone" "az_d" {
  name = "us-west-2d"
}