# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Create and configure an Event Grid Topic in Azure

1.	Sign into the Azure Portal (https://portal.azure.com/).

1.	In the Azure portal, select and launch Cloud Shell.

1.	In the Cloud Shell command line, enter the following command:
```
Code .
```
1.	In the Cloud Shell editor, select Upload, and upload the files named CreateQueue.sh, CreateEventGrid.sh, and PostEventData.sh from the directory ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter9/EventStorage/Azure

1.	Review each file and replace the placeholders.
> Note: For example, the following is a place holder with a string value: <EnterUniqueName>
  
1.	Save each file after you’ve replaced all the place holders.
  
1.	In the cloud shell editor, enter the following commands:
```
bash CreateQueue.sh
bash CreateEventGrid.sh
bash PostEventData.sh
```
1.	After you have executed the shell scripts successfully, review the Azure Storage Queue event data routed by the Event Grid Topic.

  > Note: Do not forget to delete all resources immediately to stop incurring charges
