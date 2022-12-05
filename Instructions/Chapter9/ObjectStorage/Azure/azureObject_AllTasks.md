# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Describe and create an Azure Storage Blob

1.	Sign into the [Azure Portal](https://portal.azure.com/)

1.	In the portal, select and launch Cloud Shell

1.	In the Cloud Shell command line, enter the following command to create a project container known as a resource group:
```
az group create --name <enter-resource-group> --location <region location>
```
1.	Create a storage account service that can be used to support object-level storage, known as blob (binary large object) by entering the following command:
```
az storage account create \
--name <storage-account> \
--resource-group <resource-group> \
--location <location> \
--sku Standard_ZRS \
--encryption-services blob
```
1.	Now let’s create a container to store our blobs, also known as objects by entering the following commands:
```
az storage container create \
--account-name <storage-account> \
--name <container>
```
1.	Create a file and then upload the file using the following commands:
```
touch cloudrocks.txt
```
1.	And then enter this next command to upload blobs:
```
az storage blob upload \
--account-name <enter-storage-account> \
--container-name <enter-container> \
--name cloudrocks \
--file cloudrocks.txt
```
1.	After successfully creating and uploading data, review the storage account.

