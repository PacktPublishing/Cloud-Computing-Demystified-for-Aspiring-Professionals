# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and configure a VM instance.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

1.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

1.	Make sure that billing is enabled for your Cloud project

1.	In the search field, enter the search parameter VM. And then select VM instances.

1.	In the Compute Engine page select CREATE INSTANCE.

1.	Update the following settings:
    | Create an instance | Value |
    | --- | --- |
    | Name | instance-1 |
    | Region | < Select a region > |
    | Zone | < Select a zone > |
  
## Task 2: Describe and configure Machine type.

1.	In the Machine configuration section, review the series, which correlates with the machine family, and the machine type which denotes the compute capacity size.

## Task 3: Describe and configure a boot disk.

1.	In the Boot disk section, review the boot disk properties:
    | Project details | Value |
    | --- | --- |
    | Name | instance-1 |
    |Type | New balanced persistent disk |
    | Size | 10 GB |
    | License type | Free |
    |Image | Debian GNU/Linux 11 |

## Task 4: Describe and configure Networking

1.	Review the Firewall section, select Allow HTTPS traffic, which in-turn configures an inbound rule. Deselect Allow HTTPS traffic.
  
2.	Access the context menu in the Networking section under the Advanced options, and then review the settings that support custom hostnames, and Network interfaces.
  
3.	Select, Create, and wait for the instance status.
  
> Note: Do not forget to delete all resources immediately to stop incurring charges
