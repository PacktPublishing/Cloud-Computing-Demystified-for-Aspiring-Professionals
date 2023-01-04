# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 10 Developing Database Service Resources at Scale
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Describe and develop Google Cloud SQL.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

5.	Use the Google Cloud Shell and open a terminal window.

7.	Enter the following command:
` mkdir cceb && cd cceb `
` nano main.tf `
5.	Copy the contents of the file named googleCloudSql.tf located in the directory path ~/Cloud-Computing-for-Aspiring-Professionals/blob/main/Allfiles/Chapter10/RDS/GoogleCloud/.

7.	Paste the content you copied from the previous task, into the CloudShell command-line while using Nano.

9.	Enter the following commands from the CloudShell command-line:
` terraform init `
` terraform plan `
` terraform apply `

8.	Enter yes to confirm the terraform apply command.

10.	Using the search field, enter sql, and then select Cloud SQL.

12.	Review your Cloud SQL instance properties

> Note: Do not forget to delete all resources immediately to stop incurring charges
