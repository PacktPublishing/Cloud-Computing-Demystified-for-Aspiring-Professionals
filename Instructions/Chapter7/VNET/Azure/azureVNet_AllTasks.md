# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 7 Implementing Virtual Network Resources for Security

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and configure a VNet

1.	Sign in to the [Azure Portal](https://portal.azure.com/).

1.	In the portal, navigate and select **Create a resource**, and on the **Create a resource page**, navigate the Categories section and select **Networking**.

1. In the Create a resource page, select Virtual network.

1. In the Create virtual network page, on the Basics tab, review and populate the empty fields. You can use the example table entries located in chapter 7.

1.	Select Next: IP Addresses.

## Task 2: Describe and configure an address space.

1.	In the IP Addresses tab, review the default IPv4 address space field value automatically generated displaying 10.0.0.0/16.

2.	This IPv4 address space can be modified, and the empty field below supports additional address spaces.

## Task 3: Describe and configure subnets.

1.	In the IP address tab, select the Subnet name labeled default, and then replace the Subnet name field value named default, by entering public_1, and then selecting     Save.

2.	In the IP address tab, select Add subnet, and in the Add subnet page, enter private_1 in the Subnet name field.

3.	In the Add subnet page, enter 10.0.1.0/24 in the Subnet address range field, and then select Add.

4.	In the IP address tab, select Add subnet, and in the Add subnet page, enter public_2 in the Subnet name field.

5.	In the Add subnet page, enter 10.0.2.0/24 in the Subnet address range field, and then select Add.

6.	In the IP address tab, select Add subnet, and in the Add subnet page, enter private_2 in the Subnet name field.

7.	In the Add subnet page, enter 10.0.3.0/24 in the Subnet address range field, and then select Add.

8.	In the IP address tab, navigate and select Review + create. And then in the Review + create tab, select Create.

## Task 4: Describe and configure routing and an internet gateway.

1. Cloud computing providers like Azure include their own route tables and internet gateway. Microsoft Azure has a default system route table.

In these tasks, you have implemented an Azure VNet with public and private subnets.





