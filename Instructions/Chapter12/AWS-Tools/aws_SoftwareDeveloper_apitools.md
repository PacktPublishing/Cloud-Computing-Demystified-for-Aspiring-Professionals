# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 12 Utilizing Management API Tools for Agility
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Code - Learn about the AWS software development kit fundamentals

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

> **Note**: Helpful tips and tricks are in the book in chapter 12 Utilizing Management API Tools for Agility.

1.	Go to https://aws.amazon.com/developer/tools/ and read the user-friendly SDK content and community support forum.

3.	You will need to know what programming language you’re building the application with.

> Note: Organizations use frameworks based on several factors, such as familiarity and internal talent. Sometimes, they may transition due to security and compliance concerns.

> Note: I use Python or .NET C# in my examples.

3.	Navigate the website and select Python.

5.	Upon selecting Python, review the intuitive installation instructions.

7.	Notice that you can install this Python SDK using familiar Python package management tools such as pip

> **Note**: Review the following figure, which displays the AWS SDK installation options via Visual Studio Code.

![image](https://user-images.githubusercontent.com/61672321/212747764-4efd3b7f-5f23-4064-932a-d86d7aecd101.png)

6.	After installing the SDK package using your preferred IDE, you can start writing code.

7. The following example shows how to list AWS S3 bucket objects using the Python SDK:
```
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('cloudcomputingrocksbucket')
for obj in bucket.objects.all():
    print(obj.key)
```
9. The command imports the installed SDK and uses programming classes and members to interact with the AWS S3 APIs.


