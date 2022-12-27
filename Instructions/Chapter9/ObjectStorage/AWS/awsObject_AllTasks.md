# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Describe and create an S3 bucket

1.	Sign into the [AWS Management Console](https://console.aws.amazon.com/console/)

3.	Launch the AWS CloudShell, select a region, and then select Shell.

5.	(Optionally) Upload a file to the CloudShell.

7.	In the CloudShell command line create a S3 bucket (container) by entering the following command:
```
aws s3api create-bucket --bucket <enter-unique-bucket-name> --region us-east-1
```
5.	(Optionally) If you uploaded a file to CloudShell, you could upload that file to the S3 bucket you created by entering the following command:
```
aws s3api put-object --bucket <enter-unique-bucket-name> --key <EnterfileName> --body < EnterfileName >
```
> Note: Do not forget to delete all resources immediately to stop incurring charges
