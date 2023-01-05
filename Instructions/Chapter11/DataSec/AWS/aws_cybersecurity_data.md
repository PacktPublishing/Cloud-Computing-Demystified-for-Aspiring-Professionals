# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Implement built-in data security for EBS

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

3.	Using the search field, enter EC2, and then select EC2 to navigate to the EC2 dashboard.

5.	Select Account Attributes, and then EBS encryption.

7.	Select Manage.

9.	Select Enable

11.	Select Update EBS encryption

> Note: You will need to create an EC2 instance backed by an EBS managed disk. To create a compute instance backed by an EBS use the instructions detailed in Chapter 8.
>>      Review instructions located in chapter 11 for further information.

## Task 2: Implement built-in data security for DynamoDB

1.	Using the search field, enter DynamoDB, and then select DynamoDB to navigate to the DynamoDB dashboard.

3.	You will need to create an DynamoDB table. To create a table, use the instructions detailed in Chapter 10.

5.	If you used the default settings upon table creation, tables are encrypted at rest using AWS owned keys.

> Note: DynamoDB tables are encrypted by default.

