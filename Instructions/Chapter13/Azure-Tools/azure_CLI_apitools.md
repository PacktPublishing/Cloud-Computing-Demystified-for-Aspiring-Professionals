# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 12 Utilizing Management API Tools for Agility
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Learn the Azure CLI essentials

1.	Sign in to the [Azure Portal](https://portal.azure.com/)

3.	In the portal, navigate to and select the Cloud Shell icon, follow the prompts, and create the Cloud Shell storage resources.

![image](https://user-images.githubusercontent.com/61672321/213033926-f8195555-8af0-4cc8-9486-3bcfc0478170.png)

3.	Upon selecting Azure Cloud Shell, you’ll be prompted to create a file share using an Azure storage account. You are required to create the storage resource. Select Create storage.

> **Note**: Helpful tips and tricks are in the book in chapter 12 Utilizing Management API Tools for Agility.

4.	Switch to PowerShell for the remainder of this task.

5.	You must learn the Azure CLI syntax: it’s essential for creating and managing resources. Let’s start by typing the following command:
```
az help
```
6.	Observe the output and review the Group and Subgroups areas.

> Note: The group syntax is az or az vm. The subgroups correspond to Azure services.

7.	Type the ` az vm –help ` command and review the output. ((- -help is an argument in this context.)

9.	Observe the output, and review the Group, Subgroup, and Commands areas.

11.	In the Commands area, review the operations listed.

13.	Type the ` az vm list –help ` groups command with argument and review the output.

15.	Review the Arguments and Examples sections.

> Note: Now, let’s try the PowerShell CLI via Cloud Shell.

12.	Type the ` get-command get-azvm -Syntax ` command and review the output.

13.	The syntax displays the structure of the get-azvm PowerShell commandlet or command.

> Note: Like AWS, Azure, and Google CLIs, the PowerShell commands supported in Azure Cloud Shell can be mastered by learning the syntax.

> Review the following syntax:
```
Get-AzVM [[-ResourceGroupName] <string>] [[-Name] <string>] [-Status] [-UserData] [-DefaultProfile <IazureContextContainer>] [<CommonParameters>]
```
> **Note**: Each command has specific parameters and arguments that are either required or optional during a command’s execution.


