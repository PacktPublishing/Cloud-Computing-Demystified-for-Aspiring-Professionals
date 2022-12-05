# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Implementing an AWS Lambda Function
1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

3.	In the search field, enter lambda, then select Lambda.

5.	In the Lambda dashboard, select Create function.

7.	Under Basic information, select the following:
    | Basic information | Value |
    | --- | --- |
    |	Function name | pharmafunction |
    |	Runtime | Python |

5.	Select Create function.

7.	Select Upload from context menu, then select .zip file.

9.	Select Upload, then access the directory path ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter8/Serverless/AWS and select lambda_function.zip file.

11.	Select Save.

13.	Select Test, then enter test, in the Event name field.

15.	Review the Event JSON input data.

17.	Select Save.

19.	Select Test, and then review the Execution results response, the status code displays 200, and returns a body of output, Welcome to cloud computing!
