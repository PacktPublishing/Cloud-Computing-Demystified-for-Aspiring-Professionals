# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure Google Cloud Tasks queue

1.	Sign in tointo the Google [Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

5.	In the Google Cloud console, select Activate Cloud Shell.

7.	In the Cloud Shell command line, enter the following commands to create a Cloud Tasks queue:
``` gcloud tasks queues create <EnterUniqueName> --location=<EnterLocation> ```
5.	Review queues in your current project by entering the following commands:
``` gcloud tasks queues list --location=<EnterLocation> ```
