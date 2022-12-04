# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Implementing Virtual Network Resources for Security

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

Objectives
After completing these tasks, you will be able to achieve the following:
•	Describe and configure a VM instance.
•	Describe and configure the VM Image, and size.
•	Describe and configure network settings.
•	Describe and configure a VM managed disk.
Prerequisites
Recommended requirements for completing all tasks:
•	An updated version of Windows 8.1 or later, MAC 10.15 or later, or Linux Ubuntu 18.04 or later, computer operating system.
•	An up to date and secure internet browser (Chrome or Edge are recommended)
•	Instructions are located either:
o	In chapter 8, titled, Launching Compute Service Resources for Scalability, in the section labeled Virtual Machines.
o	Navigate online to https://github.com/PacktPublishing/Cloud-Computing-for-Beginners/tree/main/Instructions/Chapter8/VM
•	Access to an Azure subscription with the required privileges to create and manage all VPC resources and dependencies.
o	How to create an Azure trial subscription for training purposes only?
	https://azure.microsoft.com/en-us/free/.
Note: The author is using a Windows 10 OS (operating system), and Chrome or Edge browser.
Important: You should FORK, Clone or Download and follow along with the step-by-step tasks in GitHub or described herein. I recommend using GitHub in conjunction with the book because any parts written in code are more clearly defined in GitHub. However, that’s my preference, you may prefer the book format.
“READY?”
Start the tasks to launch an Azure VM.
TO DO 0: Subscribing to Microsoft Azure.
Task 1: Sign into Azure
1.	Select the Edge or Chrome browser on your computer and search for https://azure.microsoft.com/en-us/free/.
2.	After the website loads, select Start free.
3.	In the login.microsoftonline.com website select Create one! Here are several email account name examples:
a.	 Example.lastname@outlook.com
b.	Example98765@outlook.com
4.	Follow the remaining prompts and populate all required fields to complete the new account creation process.
5.	Note: I have elected to exclude any guidance pertaining to billing details which include personal identifiable information.
6.	Insight: Here are several resources to help you create and manage your Azure Free tier to ensure you don’t incur substantial costs.
a.	https://azure.microsoft.com/en-us/free/free-account-faq/

Tasks
TO DO 2: Launch an Azure VM.
Task 1: Describe and configure a VM instance
In this task, you will create a VM using the Azure portal.

1.	Sign in to the [Azure Portal] (https://portal.azure.com/).
2.	In the portal, select **Create a resource**, and on the **Create a resource page**, navigate the Categories section and select **Compute**.
3.	In the Create a resource page select Virtual machine.
4.	In the Create virtual machine page, on the Basics tab, review and populate the following settings listed in the Project details section:

Subscription	<Your subscription>	none
Resource group	computerg	Create new
5.	On the Basic tab, review and populate the following settings listed in the Instance details section:
Instance details	Value	Additional Instructions
Virtual machine name	winvm0	none
Region	<Select a region near you>	none
Availability options	Availability zone	none
Availability zone	Zones 1, 2	Select Zone 1, and 2

Task 2: Describe and configure the VM Image, and size.
In this task, you will configure a VM image and size.

1.	In the instance details section, review the image setting, select the context menu, and then select Windows Server 2022 Datacenter: Azure Edition – Gen2.
2.	Review the Size setting, and leave the default selection, but notice the vcpu (virtual CPU) core quantity, the memory allocation, and the estimated monthly cost.
Insight: Optionally, you can select See all sizes and review additional size offerings in more granularity.
3.	Populate the administrator account section with a strong username and password.
Task 3: Describe and configure network settings
In this task, you will review and configure VNet settings.

1.	In the inbound port rules section, review and select Allow selected ports, and then Select inbound ports context menu, select HTTP (80).
2.	Review both HTTP (80), and RDP (3389) inbound ports.
Insight: Notice that Microsoft recommends this configuration only be used for testing.
3.	Select the Networking tab, review the Network interface, and the Load balancing sections. Select None for the Load balancing options.

4.	Select the Disks tab.
Task 4: Describe and configure a VM managed disk
In this task, you will configure managed disks.

1.	In the Disk tab, on the Disk options section, review the following settings:
1.	OS disk type, which supports different types of disks, such as Premium SSD (solid state disk), and the disk is locally redundant by default improving availability.
2.	You can alternatively delete the disk when the VM instance is deleted, or elect to support an unattached disk, that persists independently of the VM.
3.	You can also encrypt the host.
4.	Encryption type is defaulted to encrypt at rest, and Microsoft Azure manages the key for you.
2.	In the Data disk for VM, you can add data disks for your virtual machine or attach existing disks.
3.	Select Review + create, and then select create.
In these tasks, you have implemented an Azure virtual machine resource and its dependencies
