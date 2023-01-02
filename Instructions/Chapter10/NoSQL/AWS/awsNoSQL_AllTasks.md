# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 10 Developing Database Service Resources at Scale
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and develop Amazon DynamoDB table

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

3.	Select the cloudshell icon, and in the cloudshell command-line interface, enter the following commands to create a DynamoDB table, and then put items into the table:
```
aws dynamodb create-table \
    --table-name cceb \
    --attribute-definitions \
        AttributeName=CloudComputing,AttributeType=S \
        AttributeName=IaaS,AttributeType=S \
    --key-schema \
        AttributeName=CloudComputing,KeyType=HASH \
        AttributeName=IaaS,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --table-class STANDARD
```
3.	Review the status of your table by entering the following command:
` aws dynamodb describe-table --table-name cceb | grep TableStatus `
4.	Put an item into the table by entering the following command:
```
aws dynamodb put-item \
    --table-name cceb  \
    --item \
        '{"CloudComputing": {"S": "AWS"}, "IaaS": {"S": "VM"}, "Compute": {"S": "EC2"}, "Managed": {"N": "0"}}'
```
5.	After successfully creating your DynamoDB table, review the DynamoDB properties by navigating to the dashboard on the AWS management console.

> Note: Do not forget to delete all resources immediately to stop incurring charges
