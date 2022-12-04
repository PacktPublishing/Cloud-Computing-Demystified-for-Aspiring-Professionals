# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and configure instances and AMI

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

1.	In the console, navigate and select **Services**, and on the **Services** section, navigate and select **Compute**.

1.	In the Compute section select EC2.

1.	In the EC2 Dashboard select instances, and then select Launch instances.

1.	Review the Launch an instance page, enter a value <Example: WebApp > in the Name field.

1.	In the Application and OS Images (Amazon Machine Image) section, select Windows from the Quick Start options of AMIs listed. And then select Confirm Changes once prompted.

1.	Review your Amazon Machine Image, description, architecture, and the unique AMI ID associated with your image within the current region.

## Task 2: Describe and configure an instance type

1.	In the Instance type section, select compare instance types, and then review the Compare instance types page. Once you are done, select, Select instance type.
	
1.	In the Key pair (login) section, either select a preexisting key pair or select Create new key pair.

## Task 3: Describe and configure network settings

1.	In the Network settings section, review the following settings:

1.	The default VPC has already been selected and the CIDR IP address auto populated.

1.	The subnet setting displays No preference—meaning, the system will automatically configure a subnet from the CIDR IP address.

1.	Auto-assign public IP setting is set to Enable—meaning, the system will automatically assign a public IP.

1.	In the Firewall (security groups) section, review the firewall rules that control traffic for you EC2 instance.

1.	Create security group is pre-selected.

1.	The Security group name field displays launch-wizard-1.

1.	The inbound security group rules list the following:
    | Setting | Value |
    | --- | --- |
    | Type | rdp |
    | Protocol | TCP |
    | Port range | 3389 |
    | Source type | Anywhere |
    | Source | Add CIDR, prefix list or security – 0.0.0.0/0 |
    | Description | optional: e.g., SSH for admin desktop |

## Task 4: Describe and configure an EBS storage volume

1.	Review the Configure storage section settings:
    | Setting | Value |
    | --- | --- |
    | Root volume | gp2—General purpose SSD (solid state disk) |
    | GiB (Gigabyte) | 30 |
1.	Review the summary section, and then select Launch instance.
> Note: This may take several minutes.
1.	After the successful creation of your EC2 instance, I recommend you review your instance utilizing the EC2 dashboard.

