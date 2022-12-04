# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and configure a VM instance

1.	Sign in to the [Azure Portal](https://portal.azure.com/)

1.	In the portal, select Create a resource, and on the Create a resource page, navigate the Categories section and select Compute.

1.	In the Create a resource page select Virtual machine.

1.	In the Create virtual machine page, on the Basics tab, review and populate the following settings listed in the Project details section:
    | Project details | Value |
    | --- | --- |
    | Subscription | < Your subscription > |
    | Resource group | < Select preexisting or create new >	|

1.	On the Basic tab, review and populate the following settings listed in the Instance details section:
    | Instance details | Value |
    | --- | --- |
    | Virtual machine name |	winvm0 |
    | Region| < Select a region near you > |
    | Availability options |	Availability zone |
    | Availability zone | Zones 1, 2 |

1. Select zone 1 and 2.

## Task 2: Describe and configure the VM Image, and size.

1.	In the instance details section, review the image setting, select the context menu, and then select Windows Server 2022 Datacenter: Azure Edition – Gen2.

1.	Review the Size setting, and leave the default selection, but notice the vcpu (virtual CPU) core quantity, the memory allocation, and the estimated monthly cost.

1.	Populate the administrator account section with a strong username and password.

## Task 3: Describe and configure network settings

1.	In the inbound port rules section, review and select Allow selected ports, and then Select inbound ports context menu, select HTTP (80).

1.	Review both HTTP (80), and RDP (3389) inbound ports.

1.	Select the Networking tab, review the Network interface, and the Load balancing sections. Select None for the Load balancing options.

1.	Select the Disks tab.

## Task 4: Describe and configure a VM managed disk

1.	In the Disk tab, in the Disk options section, review the following settings:

1.	OS disk type, which supports different types of disks, such as Premium SSD (solid state disk).

1.	Encryption type is defaulted to encrypt at rest.

1.	In the Data disk for VM, you can add data disks for your virtual machine.

1.	Select Review + create, and then select create.
> Note: Do not forget to delete all resources immediately to stop incurring charges
