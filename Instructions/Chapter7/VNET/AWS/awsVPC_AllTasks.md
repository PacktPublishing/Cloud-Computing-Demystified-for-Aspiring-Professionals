# Chapter 7 : Implementing an AWS VPC


## Why?

Traditional and modern development projects still recommend technical and non-technical controls to be properly assessed. In this case, we started our tutorial by understanding the importance of analyzing the cloud networking service resources before further development. After a thorough but insightful analysis of our network resources, organizations can consider implementing thier line of business application or service in a VPC.

## Objectives

In this lab, you will:

+ Task 1: Describe and configure a VPC
+ Task 2: Describe and configure a CIDR
+ Task 3: Describe and configure subnets
+ Task 4: Describe and configure an internet gateway
+ Task 5: Describe and configure routing


## Instructions

## Exercise 0

### Task 0: Setup and configure prerequisites

In this task, you will review and setup all required prerequisites

1. Review and follow suggested instructions located in a file named README.md located in the directory ~/Cloud-Computing-for-Beginners/tree/main/Instructions/Chapter7/VNET/AWS

> Note: After reviewing and complying with all required prerequisites denoted in the file mentioned above return to this file and continue to the next exercise task.

### Exercise 1
#### Task 1: Describe and configure a VPC
In this task, you will implement a VPC by using the AWS management console.

> Amazon provides a preconfigured VPC in every AWS geographical region. The VPC is labeled default VPC... For further information and examples read the book titled Cloud Computing Essentials for Beginners.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/).

1. In the console, navigate and select **Services**, and on the **Services** section, navigate and select **Networking & Content Delivery**.

1.  In the Networking & Content Delivery section select VPC.

1.	In the VPC Dashboard navigate and select Launch VPC Wizard.

1.	Insight: Do not modify any fields or sections unless explicitly instructed. For example, If the author circumvents an option which appears  as a button or box or name field or metadata it’s intentional. These options or settings are already configured by the system, and I will refer to as the default settings.

1.	Review the VPC dashboard, Create VPC wizard sections labeled VPC settings, VPC, Subnets, and Route tables.

1.  Insight: The VPC dashboard configuration section labeled Create a VPC streamlines the manual configuration... For further information please read the book titled Cloud Computing Essentials for Beginners.

#### Task 2: Describe and configure a CIDR
In this task, you will define a CIDR by using the Launch VPC Wizard.

In cloud computing, virtual networks require network administrators to define the starting IP and the size of the VPC using... For further information read the book titled Cloud Computing Essentials for Beginners.

1.	In the IPv4 CIDR block field review the default settings. Analyze the IPs available, 65,536 IPs are listed.

1.	The calculation was performed automatically.

1.	Update the IPv4 CIDR block field to 10.0.0.0/18. Analyze the IPs available, how many are listed?

1.	Review the Availability Zones (AZs) options. Analyze the recommendation denoted, at least two AZs for high availability.

1.	Remember, in chapter 3 titled Understanding the Benefits of Public Clouds (AWS, Azure, and GCP) we described the Fault Tolerant Infrastructure which explained Availability Zones (AZ).

#### Task 3: Describe and configure subnets
In this task, you will define and configure VPC subnets.

1.	In the Create a VPC page, the Number of public subnets default settings display 2 public subnets and denote, for web applications that need to be publicly accessible over the internet. If you interpreted accurately, you understand, publicly accessible resources such as web applications need a subnet that allows for public access.

1.	If we follow best practices in terms of resiliency, recall that we elected at minimum two Availability Zones. Theoretically, we should distribute a web application or service across two different availability zones to improve resiliency. Therefore, we will leave the default settings unmodified.

1.	And because we are adhering to best practices, we should also have at minimum two private subnets for resiliency and to secure backend resources that should not be accessible over the public internet. Hence, private IP addresses are sufficient and internal VPC routing for the private subnet should only allow inbound traffic from VPC isolated services and service ports explicitly defined after one or more rigorous risk analysis tests are concluded and approved by all stakeholders.

1.	Review the Customize subnets CIDR blocks section, notice that you can customize the subnets, and the calculated IPs available are listed automatically.

#### Task 4: Describe and configure routing
In this task, you will define routing.

1.	Review the Route tables section located in the Create VPC page. Identify the route table suffix labeled <place holder>-rtb-public. This route table was automatically generated and assigned to your public subnets. Like the other route tables, this table has a destination and a target. This route table enables the public subnets to access the public internet, which is the destination, via an internet gateway, which is the target.

1.	Lastly, select Create VPC, and review the details upon successfully creating an AWS VPC.

In these tasks, you have implemented an AWS VPC with public and private subnets distributed across multiple availability zones.
