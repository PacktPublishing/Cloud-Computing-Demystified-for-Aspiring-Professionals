# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Create and configure EventBridge with a target event handler

1.	Sign into the [AWS Management Console](https://console.aws.amazon.com/console/)

1.	In the search field enter lambda, and then select Lambda to access the lambda dashboard.

1.	Select Create function.

1.	Select Author from scratch.

1.	Enter a unique name for the Lambda function.

1.	Select Create function

1.	In the function page, select index.js.

1.	Select Upload from .zip file, then select Upload, and select the file named index.zip from the directory path ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter9/EventStorage/AWS

1.	Select Deploy.

## Task 2: Create and configure the event archive, and rule.
1.	Sign in to the EventBridge management console using the following link:
```
https://console.aws.amazon.com/events/
```
1.	Select Archives.

1.	Select Create archive.

1.	Enter a unique archive name.

1.	Select Create archive.

1.	Select Rules

1.	Select Create rule.

1.	Enter a unique rule name.

1.	Select the default Event bus. If it’s preselected, then disregard.

1.	Select Rule with an event pattern for Rule type.

1.	Select Next.

1.	Select Other, for the Event source.

1.	Enter the following for the Event pattern:
```
{
  "detail-type": [
    "customerCreated"
  ]
}
```
1.	Select Next.

1.	Select AWS service for Target types.

1.	Select Lambda function for Select a target.

1.	Select the lambda function you created previously.

1.	Select Next, and then Next again.

1.	Select Create a rule and then review your EventBridge resources

> Note: Do not forget to delete all resources immediately to stop incurring charges
