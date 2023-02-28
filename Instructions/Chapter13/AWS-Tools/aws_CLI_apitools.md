# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 12 Utilizing Management API Tools for Agility
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Learn the AWS CLI fundamentals

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

3.	Start by selecting the Cloud Shell icon.

![image](https://user-images.githubusercontent.com/61672321/212725629-e8dca0a5-ffff-4693-8271-6b5c338a98b7.png)

> **Note**: Helpful tips and tricks are in the book in chapter 12 Utilizing Management API Tools for Agility.

3.	Once the AWS CloudShell is active, you’ll notice the output displays syntax such as Preparing your terminal, as well as other useful information to get you started, such as using the AWS help commands.

5.	Notice that you are at the CLI prompt.

5.	If you did switch to PowerShell, please switch back to the bash shell for the remainder of this task.

7.	Understanding the syntax is essential for any CLI. Let’s start by typing the following command: ` aws help `

9.	Observe the output and review the NAME, DESCRIPTION, and SYNOPSIS fields.

> Note: Right below the SYNOPSIS area, identify the syntax output that resembles the following:
```
aws [options] <command> <subcommand> [parameters]
```
>> Note: AWS CLI commands are comprised of a call to AWS and one of its services, such as EC2. This is known as a top-level command. The subcommand corresponds to an operation. Each operation has specific options and parameters that are either required or optional during an operation’s execution.

11. Type the following command and review its output:
```
aws iam get-account-summary
```
12. Review a summary of your AWS account information.

> **Note**: If you did not have an opportunity to learn how to use the AWS CLI by creating a resource, then I recommend revisiting Chapter 8
