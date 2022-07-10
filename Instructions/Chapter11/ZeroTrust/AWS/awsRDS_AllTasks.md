# Chapter 8 : Launching Compute Service Resources for Scalability

## Why?

Traditional and modern development projects still recommend technical and non-technical controls to be properly assessed. In this case, we started our tutorial by understanding the importance of analyzing the EC2 before further development. After a thorough but insightful analysis of our resources, we can consider implementing our line of business application or service in a EC2.

## Objectives

In this lab, you will:

+ Task 1: Describe and configure instances and AMI
+ Task 2: <>
+ Task 3: <>
+ Task 4: <>
+ Task 5: <>


## Instructions

## Exercise 0

### Task 0: Setup and configure prerequisites

Start the tasks to create an AWS EC2.

TO DO 0: Subscribing to AWS.

Task 1: Sign into AWS

1.	Select the Edge or Chrome browser on your computer and search for https://aws.amazon.com/free.

2.	After the website loads, select Create a Free Account.

3.	In the portal.aws.amazon.com website populate the fields labeled Root user email address and AWS account name, enter a valid, and readily
accessible email account name and AWS account name for training purposes. Here are several email accounts and AWS account name examples:

a.	 Example.lastname@gmail.com

b.	Example.lastname@outlook.com

c.	Cloud Practitioner

4.	Follow the remaining prompts and populate all required fields to complete the new account creation process.

5.	Note: I have elected to exclude any guidance pertaining to billing details which include personal identifiable information.

6.	Insight: Here are several resources to help you create and manage your AWS Free tier to ensure you don’t incur substantial costs.

a.	https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/

b.	https://aws.amazon.com/premiumsupport/knowledge-center/what-is-free-tier/

Tasks

TO DO 1: Launch an AWS EC2 instance.

Important: The instructions listed match the AWS management portal version available in May of 2022. AWS is always updating the interface to improve the user experience.

Task 1: Describe and configure instances and AMI

In this task, you will launch a EC2 instance using the AWS management console.

1.	Sign in to the [AWS Management Console] (https://console.aws.amazon.com/console/).

2.	In the console, navigate and select **Services**, and on the **Services** section, navigate and select **Compute**.

3.	In the Compute section select EC2.

4.	In the EC2 Dashboard select instances, and then select Launch instances.

5.	Insight: Do not modify any fields or sections unless explicitly instructed. For example, If the author circumvents an option which appears as a button or box or name field or metadata it’s intentional. These options or settings are already configured by the system, and I will refer to them as the default settings.

6.	Review the Launch an instance page, enter a value <Example: WebApp > in the Name field.

7.	Insight: The EC2 dashboard configuration section labeled Launch an instance improves the manual configuration process by centralizing overall virtual machine settings which include application and operating system configuration, and virtual machine sizing, disk storage, and network settings.

8.	In the Application and OS Images (Amazon Machine Image) section, select Windows from the Quick Start options of AMIs listed. And then select Confirm Changes once prompted.

9.	Insight: Amazon provides Amazon Machine Images which describes the data required to launch an instance. The AMI contains many things like, the source AMI, also referred to as image, which is an image of an operating system. The AMI helps you launch multiple instances with a similar configuration. And denotes a template for the root volume containing your OS, privileges required to allow your AWS account or others to use the AMI and the information required to attach a block storage device to your EC2 instance when created.

10.	Review your Amazon Machine Image, description, architecture, and the unique AMI ID associated with your image within the current region.

Task 2: Describe and configure an instance type

In this task, you will define a CIDR by using the Launch VPC Wizard.

1.	In the Instance type section, select compare instance types, and then review the Compare instance types page. Once you are done, select, Select instance type.
2.	In the Key pair (login) section, either select a preexisting key pair or select Create new key pair.
Task 3: Describe and configure network settings
In this task, you will define and configure your VPC network settings.

1.	In the Network settings section, review the following settings:
1.	The default VPC has already been selected and the CIDR IP address auto populated.
Insight: Recall what we mentioned regarding the default VPC in chapter 7.
2.	The subnet setting displays No preference—meaning, the system will automatically configure a subnet from the CIDR IP address.
3.	Auto-assign public IP setting is set to Enable—meaning, the system will automatically assign a public IP.
2.	In the Firewall (security groups) section, review the firewall rules that control traffic for you EC2 instance.
1.	Create security group is pre-selected.
2.	The Security group name field displays launch-wizard-1.
3.	The inbound security group rules list the following:
a.	Type: rdp
b.	Protocol: TCP
c.	Port range: 3389
d.	Source type: Anywhere
e.	Source: Add CIDR, prefix list or security – 0.0.0.0/0
f.	Description – optional: e.g., SSH for admin desktop
3.	And you will see a AWS best practice suggestion like, we recommend setting security group rules to allow access from known IP addresses only.

Task 4: Describe and configure an EBS storage volume
In this task, you will configure EC2 disk storage.

1.	Review the Configure storage section settings:
1.	Root volume: gp2—General purpose SSD (solid state disk)
a.	Solid State Disks are known for their performance.
b.	General purpose disk types are practical for a range of workloads, development, testing, and for base operating system volumes.
2.	GiB (Gigabyte): 30
2.	Review the summary section, and then select Launch instance.
3.	This may take several minutes.
4.	After the successful creation of your EC2 instance, I recommend you review your instance utilizing the EC2 dashboard.
In these tasks, you have launched an AWS EC2 instance with EBS and VPC
