# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure Compute Engine instance built-in compute security using snapshots

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project
> Note: You will need to create a Compute Engine instance. To create a Compute Engine instance, use the instructions in Chapter 8.

2.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
3.	
4.	Select, Activate Cloudshell.
5.	
6.	In the Cloudshell command line interface enter the following command and replace any placeholders with unique values:
```
gcloud compute snapshots create <placeholder> \
    --source-disk <placeholder> \
    --source-disk-zone <placeholder>
```
7. placeholder
