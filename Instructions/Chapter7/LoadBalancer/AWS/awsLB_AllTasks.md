# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 7 Implementing Virtual Network Resources for Security

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task : Describe and configure an Elastic Load Balancer
1. Sign into the [AWS Management Console](https://console.aws.amazon.com/console/)

1.  In the console, select Services, and in the Services section, navigate and select Management & Governance.
	
1.	In the Management & Governance section, select CloudFormation.

1. 	In the CloudFormation dashboard, navigate and select Designer.

1. On the CloudFormation Designer page, navigate and select the file icon, and then select Open.

1. On the Open a template dialogue box or prompt, select Local file.

1.	After selecting the Local file option, you’ll have access to your local machine directory and files. Using your local machine file system. For example, File    Explorer opens, and displays my directories.

1.	Using file explorer, I navigate to the directory ~ Cloud-Computing-Essentials-Beg\Allfiles\Chapter7\VNET\AWS. And then I select awsloadbalancer.json.

1.	On the CloudFormation Designer page, navigate and select the validate template icon. The output should display template is valid.

1.	On the CloudFormation Designer page, navigate and select the create stack icon.

1.	Select Next.

1.	In the Specify stack details page, enter a stack name. For example, stack01.

1.	In the Specify stack details page, review the instance type, KeyName, and SSHLocation parameters. And then select a KeyName preexisting value. For Example, KeyPairCh7. And then select Next.
	
1. Select Next.

1.  In the Review <place holder for your stack name> page. For example, In the Review stack01. Navigate and select, I acknowledge that AWS CloudFormation might create    IAM resources, and then select Create stack. 
> Note: Stack creation can take some time.
  
1.  Review the AWS resources created by using the search feature in the AWS management console.

1.  Delete the stack of resources to prevent incurring further charges.
  - Launch the cloud shell in the AWS management console.
  - At the cloud shell command line prompt enter the following to delete the stack of resources:
  ```
    aws cloudformation delete-stack --stack-name <enter your stack name here>
  ```
> Note: Do not forget to delete all resources immediately to stop incurring charges



