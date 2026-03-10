provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "service_repo" {
  name = var.service_name
}

resource "aws_iam_role" "service_role" {
  name = "${var.service_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}