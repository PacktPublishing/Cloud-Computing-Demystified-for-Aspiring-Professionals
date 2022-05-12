# Tasks
## TO DO 1: Implement an AWS Elastic Load Balancer.
Important: The instructions listed are accurate if you are using the New VPC Experience, which is optional. Furthermore, to help you the reader successfully implement a service, I have elected to utilize IaC like tools and services to streamline creation. However, this may impact your experience mastering all the components and features of the cloud computing service in this chapter.


# Task 1: Describe and configure an Elastic Load Balancer.

In this task, you will implement an Elastic load balancer by using AWS CloudFormation.


1.	Sign in to the [AWS Management Console] (https://console.aws.amazon.com/console/).

2.	Insight: You will need to create an AWS KeyPair for task step 15 below.

3.	In the console, navigate and select **Services**, and on the **Services** section, navigate and select **Management & Governance**.

4.	In the Management & Governance section, select CloudFormation.

5.	In the CloudFormation dashboard, navigate and select Designer.

6.	On the CloudFormation Designer page, navigate and select the file icon, and then select Open.

7.	On the Open a template dialogue box or prompt, select Local file.

8.	Note: If you followed the previous recommendations to FORK, and clone or download the GitHub repository directory and files to your local machine. You can upload any files to help complete tasks.

9.	After selecting the Local file option, you’ll have access to your local machine directory and files. Using your local machine file system. For example, File Explorer opens, and displays my directories.

10.	Using file explorer, I navigate to the directory ~ Cloud-Computing-Essentials-Beg\Allfiles\Chapter7\VNET\AWS. And then I select awsloadbalancer.json.

11.	On the CloudFormation Designer page, navigate and select the validate template icon. The output should display template is valid.

12.	On the CloudFormation Designer page, navigate and select the create stack icon.

13.	Select Next.

14.	In the Specify stack details page, enter a Stack name. For example, stack01.

15.	In the Specify stack details page, review the instance type, KeyName, and SSHLocation parameters. And then select a KeyName preexisting value. For Example, KeyPairCh7. And then select Next.

16.	Select Next.

17.	In the Review <place holder for your stack name> page. For example, In the Review stack01. Navigate and select, I acknowledge that AWS CloudFormation might create IAM resources, and then select Create stack.

a.	Stack creation can take some time.

18.	Review the AWS resources created by using the search feature in the AWS management console.

19.	Delete the stack of resources to prevent incurring further charges.

a.	Launch the cloud shell in the AWS management console.

b.	At the cloud shell command line prompt enter the following to delete the stack of resources:

i.	aws cloudformation delete-stack \
--stack-name <enter your stack name here>.
