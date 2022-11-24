
# Create a VPC for the region associated with the AZ
resource "aws_vpc" "patent_vpc" {
  cidr_block = cidrsubnet("10.0.0.0/16", 4, var.region_number[data.aws_availability_zone.az_a.region])
  tags = {
        Name    = "Patent VPC"
   }
}

# Create a subnet for the AZ within the regional VPC
resource "aws_subnet" "public_subnet_a" {
  vpc_id     = aws_vpc.patent_vpc.id
  cidr_block = cidrsubnet(aws_vpc.patent_vpc.cidr_block, 4, var.az_number[data.aws_availability_zone.az_a.name_suffix])
  tags = {
     Name = "Public Subnet a"
   }
}

resource "aws_subnet" "public_subnet_b" {
  vpc_id     = aws_vpc.patent_vpc.id
  cidr_block = cidrsubnet(aws_vpc.patent_vpc.cidr_block, 4, var.az_number[data.aws_availability_zone.az_b.name_suffix])
  tags = {
     Name = "Public Subnet b"
   }
}

resource "aws_subnet" "private_subnet_a" {
  vpc_id     = aws_vpc.patent_vpc.id
  cidr_block = cidrsubnet(aws_vpc.patent_vpc.cidr_block, 4, var.az_number[data.aws_availability_zone.az_c.name_suffix])
  tags = {
     Name = "Private Subnet a"
   }
}

resource "aws_subnet" "private_subnet_b" {
  vpc_id     = aws_vpc.patent_vpc.id
  cidr_block = cidrsubnet(aws_vpc.patent_vpc.cidr_block, 4, var.az_number[data.aws_availability_zone.az_d.name_suffix])
  tags = {
     Name = "Private Subnet b"
   }
}
resource "aws_internet_gateway" "gw" {
  vpc_id           = aws_vpc.patent_vpc.id
  
  tags = {
    Name = "Public Internet Gateway"
  }
}

resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.patent_vpc.id

  route {
    cidr_block =  "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }


  tags = {
    Name = "Public Route table"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.public_subnet_a.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.public_subnet_b.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_eip" "eip" {
  vpc      = true
}

resource "aws_nat_gateway" "nat_gw" {
  allocation_id = aws_eip.eip.id
  subnet_id     = aws_subnet.private_subnet_a.id

  tags = {
    Name = "gw NAT"
  }

  # To ensure proper ordering, it is recommended to add an explicit dependency
  # on the Internet Gateway for the VPC.
  depends_on = [aws_internet_gateway.gw]
}


resource "aws_default_route_table" "private_route_table" {
  default_route_table_id = aws_vpc.patent_vpc.default_route_table_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.nat_gw.id
  }

  tags = {
    Name = "Private Route Table"
  }
}
