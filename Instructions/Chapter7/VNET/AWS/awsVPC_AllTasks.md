# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 7 Implementing Virtual Network Resources for Security

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and configure a VPC

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/).

1. In the console, navigate and select **Services**, and on the **Services** section, navigate and select **Networking & Content Delivery**.

1.  In the Networking & Content Delivery section select VPC.

1.	In the VPC Dashboard navigate and select Launch VPC Wizard.

1.	Review the VPC dashboard, Create VPC wizard sections labeled VPC settings, VPC, Subnets, and Route tables.

## Task 2: Describe and configure a CIDR

1.	In the IPv4 CIDR block field review the default settings. Analyze the IPs available, 65,536 IPs are listed.

1.	The calculation was performed automatically.

1.	Update the IPv4 CIDR block field to 10.0.0.0/18. Analyze the IPs available, how many are listed?

1.	Review the Availability Zones (AZs) options. Analyze the recommendation denoted, at least two AZs for high availability.

## Task 3: Review subnets

1.	In the Create a VPC page, the Number of public subnets default settings display 2 public subnets.

1.	Review the Customize subnets CIDR blocks section, notice that you can customize the subnets, and the calculated IPs available are listed automatically.

## Task 4: Review routing

1.	Review the Route tables section located in the Create VPC page. 

1.	Lastly, select Create VPC, and review the details upon successfully creating an AWS VPC.

In these tasks, you have implemented an AWS VPC with public and private subnets distributed across multiple availability zones.
