# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Create and configure an Azure file share

1.	Sign into the [Azure Portal](https://portal.azure.com/)

1.	In the portal, launch Cloud Shell.

1.	In the Cloud Shell command line enter the following commands to create a resource group to manage this project:
```
az group create --name fileshareRG --location <region location>
resourceGroupName="fileshareRG"
storageAccountName="<enter-unique-name>$RANDOM"
region="eastus"
```
1.	Enter the following commands to create an Azure Storage account that supports a file share:
```
az storage account create \
--resource-group $resourceGroupName \
--name $storageAccountName \
--kind StorageV2 \
--sku Standard_ZRS \
--enable-large-file-share \
--output none
```
1.	Enter the next commands to create the Azure file share:
```
shareName="cloudfileshare"

az storage share-rm create \
--resource-group $resourceGroupName \
--storage-account $storageAccountName \
--name $shareName \
--access-tier "TransactionOptimized" \
--quota 1024 \
--output none
```
1.	Mounting an Azure file share on Windows or Linux is as simple as navigating to the Azure portal and managing your Azure Storage Accounts file share.

1.	Simply select the file share, and then select Connect.

1.	Review all the important information detailed in the connect page for mounting Windows, Linux, including macOS

