# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure Network Security Groups for built-in network security

1.	Sign in to the [Azure Portal](https://portal.azure.com/)
> Note: Select the VNet you created in chapter 7. If required, recreate the VNet using the instructions located in Chapter 7.

2.	Select Create a resource.

4.	Select Networking, then select Network security groups.

6.	In the Basics tab, set values for the following settings, subscription, resource group, name, region.

8.	Select Review + create, and then select Create.

10.	Select the Network security group you created.

12.	Select Inbound security rules.

14.	Select Add, and then populate the following settings – source, source IP, Source service tag, source application security group, source port ranges, destination, destination IP, Destination service tag, destination application security group, destination port ranges, protocol, allow or deny, priority, name and description.

16.	In the network security group dashboard, select subnets.

18.	Select + Associate

20.	Select your VNET, and then select OK
