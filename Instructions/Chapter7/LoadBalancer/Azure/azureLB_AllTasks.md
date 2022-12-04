# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 7 Implementing Virtual Network Resources for Security

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

# Task: Describe and configure an Azure Load Balancer.

1.	Sign in to the [Azure Portal](https://portal.azure.com/)

2.	In the portal, navigate and select **Create a resource**, and on the **Create a resource page**, enter template in the search services and marketplace field. And then select Template deployment.

3.	On the Template deployment (deploy using custom templates) page, select Create.

4.	On the Custom deployment page, select Build your own template in the editor.

5.	In the Edit template page, select Load file.

> Note: If you followed the previous recommendations to FORK, and clone or download the GitHub repository directory and files to your local machine. You can upload the required files to help complete this task.

7.	Select the file named azureloadbalancer.json located in the directory ~ /Cloud-Computing-Essentials-Beg\Allfiles\Chapter7\VNET\Azure. And then select Save on the Edit template page.

8.	In the Custom deployment page, enter the following parameter values:
    | Setting | Value |
    | --- | --- |
    | Resource group | azurelbrg |
    | Region| East US (Select a region in close proximity with available capacity) |
    | Admin Username | Enter a unique name |
    | Admin Password | Pa55w0rd12345 |

> Note: Replace the weak password value with unique characters.

9.	On the Custom deployment page, select Review + create.

10.	After validation has passed, select Create.

> Note: Azure template creation can take some time.

11.	Review the Azure resources created by using the search feature in the Azure portal.

12.	Delete the resources to prevent incurring further charges.

-	Launch the cloud shell in the Azure portal.

-	At the cloud shell command line prompt enter the following to delete the resources:
```
Az group delete –n <Enter your resource group name here>
```
14.	And then enter ` y ` at the next prompt.

> Note: Do not forget to delete all resources immediately to stop incurring charges
