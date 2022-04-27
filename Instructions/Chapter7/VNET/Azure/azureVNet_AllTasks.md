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


