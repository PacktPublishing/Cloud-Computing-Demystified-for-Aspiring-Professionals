# Chapter 7 : Implementing an Azure VNet


## Why?

Technical and non-technical controls can be analyzed. In this case, we started our tutorial by understanding the importance of examining the cloud networking service resources before further development and testing. If approved, implement in production to securely host our organization's line of business application or service.

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

#### Task 1: Describe and configure a VNet

In this task, you will implement a VNet by using the Azure portal.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/).

1.	In the portal, navigate and select **Create a resource**, and on the **Create a resource page**, navigate the Categories section and select **Networking**.

1. In the Create a resource page select Virtual network.

1. In the Create virtual network page, on the Basics tab, review and populate the following empty fields, use the table entries from the value column listed below:
    - Resource Group: ccebnetworkRG
    - Name: Vnet0
    - Region: East US
1.	Select Next: IP Addresses.

#### Task 2: Describe and configure an address space.
In this task, you will define and configure an IP address space.

1.	In the IP Addresses tab, review the default IPv4 address space field value automatically generated displaying 10.0.0.0/16.

2.	This IPv4 address space can be modified, and the empty field below supports additional address spaces. Remember, IP address spaces cannot overlap.

#### Task 3: Describe and configure subnets.
In this task, you will define and configure an IP address space subnet.

1.	In the IP address tab, select the Subnet name labeled default, and then replace the Subnet name field value named default, by entering public_1, and then selecting Save.

2.	In the IP address tab, select Add subnet, and in the Add subnet page, enter private_1 in the Subnet name field.

3.	In the Add subnet page, enter 10.0.1.0/24 in the Subnet address range field, and then select Add.

4.	In the IP address tab, select Add subnet, and in the Add subnet page, enter public_2 in the Subnet name field.

5.	In the Add subnet page, enter 10.0.2.0/24 in the Subnet address range field, and then select Add.

6.	In the IP address tab, select Add subnet, and in the Add subnet page, enter private_2 in the Subnet name field.

7.	In the Add subnet page, enter 10.0.3.0/24 in the Subnet address range field, and then select Add.

8.	In the IP address tab, navigate and select Review + create. And then in the Review + create tab, select Create.

#### Task 4: Describe and configure routing and an internet gateway.
In this task, you will understand Azure routing and its built-in internet gateway.





