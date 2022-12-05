# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Describe and deploy Google Cloud Storage

1.	Sign into the [Google Cloud Console](https://console.cloud.google.com/)

1.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

1.	Use the Google Cloud Shell and open a terminal window.

1.	Enter the following commands to create a Google Cloud Storage bucket:
```
gsutil mb -b on -l us-east1 gs://<enter-unique-name>/
```
5. Enter the next command to create a file also known as blob (object), and then upload to destination Cloud Storage bucket:
```
touch cloudrocks.txt

gsutil cp cloudrocks.txt gs://<enter-unique-name>
```
6. After successfully creating and uploading data, review the Google Cloud Storage
> Note: Do not forget to delete all resources immediately to stop incurring charges
