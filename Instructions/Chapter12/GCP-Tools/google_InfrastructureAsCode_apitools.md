# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 12 Utilizing Management API Tools for Agility
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Learn the Google Cloud Deployment Manager essentials

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

5.	Make sure that billing is enabled for your Google Cloud project.

3.	Next, enable access to the APIs. Enable the Cloud Deployment Manager V2 API.

> **Note**: Helpful tips and tricks are in the book in chapter 12 Utilizing Management API Tools for Agility.

4.	Activate Cloud Shell and select the upload option or create a new file to edit.

6.	Copy the sample configuration str.yaml file located in GitHub and paste it into the Google Cloud editor.

6.	To deploy use the Cloud Shell CLI to create a deployment using the configuration file. Type the following command: 
```
gcloud deployment-manager deployments create ccdapxxxx-cloudstrg –config strg.yaml
```

> Note: Replace the placeholder syntax, ` xxxx `, with a unique string of characters.

7.	After successfully creating a Google Cloud Storage account, review the Google Cloud Deployment Manager dashboard.

> **Note**: If you missed the opportunity to learn how to use the Google Cloud Deployment Manager to create a resource, then I recommend revisiting Chapter 8.
