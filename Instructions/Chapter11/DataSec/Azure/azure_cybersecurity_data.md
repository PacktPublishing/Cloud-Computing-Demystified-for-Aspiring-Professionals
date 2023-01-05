# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Implement built-in data security for managed disks

1.	Sign in to the [Azure Portal](https://portal.azure.com/)

3.	In the portal, use the search field and enter virtual machine, and then select virtual machine to navigate to the dashboard

5.	Select Disks from the settings.

7.	Select Encryption settings, then select Disks to encrypt, and then select OS and data disks from the menu.

9.	Select a key vault and key for encryption.

11.	Select Create New to create a Key Vault, which is Azure key management service.

13.	Select a key, and then select Create new under the Key Vault field area.

15.	Enter a unique name for your Key Vault.

17.	Select Access Policies, and then select Azure Disk Encryption for volume encryption.

19.	Select Review + create. And then select Create.

21.	Select the select option.

23.	Select Save, and when prompted, select Yes.

> Note: For further information on Windows or Linux encryption features review chapter 11.

## Task 2: Implement built-in data security for Azure SQL Database

1.	Select the search field and enter Azure SQL Database.

> Note: You will need to create an Azure SQL Database. To create an Azure SQL Database, use the instructions detailed in Chapter 10.

3.	Select your Azure SQL Database resource.

5.	Review your Azure SQL Database resource security settings.

> Note: Azure SQL DB tables are encrypted by default.

> Note: Do not forget to delete all resources immediately to stop incurring charges

