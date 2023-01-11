# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure AWS Network access control lists for built-in network security

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)
> Note: Select the VPC you created in chapter 7. If required, recreate the VPC using the instructions located in Chapter 7.

2.	Search for VPC, and then access the VPC dashboard.

4.	Select Network ACLs.

6.	Select Create Network ACL.

8.	When prompted by the Create Network ACL dialog box, enter a unique name for your network ACL, and select the ID of your VPC from the VPC list. Select Yes | Create.

10.	Select your Network ACL.

12.	Select Details, then select Inbound Rules, and then select Edit.

14.	Add the rule number, type, protocol, port, source, or destination, and either allow or deny based on your security control requirements.

> Note: Do not forget to delete all resources immediately to stop incurring charges
