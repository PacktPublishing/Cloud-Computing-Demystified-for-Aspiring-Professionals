# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure virtual machine built-in compute security using incremental snapshots

1.	Sign in to the [Azure Portal](https://portal.azure.com/)
> Note: Select the Azure Virtual Machine you created in chapter 8. If required, recreate the Virtual Machine using the instructions located in Chapter 8.

2.	In the portal, search for and activate the Cloud Shell.

4.	In the Cloud Shell command line interface enter the following commands and replace all place holders with unique values:
```
# Create variables
diskName="<placeholder>"
resourceGroupName="<placeholder>"
snapshotName="<placeholder>"
```
```
# Select the disk to backup
yourDiskID=$(az disk show -n $diskName -g $resourceGroupName --query "id" --outputtsv)
```
```
# Create the snapshot
az snapshot create -g $resourceGroupName -n $snapshotName --source $yourDiskID --incremental true
```
5. In the Azure portal, search for your Azure VM, and review the VM disk settings.

> Note: Do not forget to delete all resources immediately to stop incurring charges
