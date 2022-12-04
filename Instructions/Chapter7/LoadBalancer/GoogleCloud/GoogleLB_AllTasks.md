# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 7 Implementing Virtual Network Resources for Security

> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

# Task 1: Describe and configure a Google Cloud Load Balancer.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

2.	In the console, enter Cloud Run API in the search field, and then select Cloud Run API.

3.	In the Cloud Run API page, select ENABLE.

4.	In the console, select Activate Cloud Shell.

6.	In cloud shell, at the prompt, enter git clone <GitHub repo URL>

7.	Next, enter cd ~/Instructions/Chapter7/ to change to the directory containing the terraform files.

8.	Set the project by entering ` PROJECT=YOUR_PROJECT `
  

9.	Next, enter ` gcloud config set project ${PROJECT} `

10.	Configure the Terraform environment by entering:
```
[[ $CLOUD_SHELL ]] || gcloud auth application-default login

export GOOGLE_PROJECT=$(gcloud config get-value project)
```
11.	Initialize Terraform by entering ` terraform init `

12.	And then implement the resources defined in the Terraform files like the load balancer by entering ` terraform apply -var=project_id=$PROJECT \
-var=ssl=false -var=domain=null `

13.	Resource creation may take several minutes.

14.	If you encounter any prompts, enter ` yes ` to continue.

15.	After successful resource creation, review the resources governed by your Google Cloud project.

16.	After reviewing the load balancer resources. I recommend you delete all resources to control incurring additional charges.

17.	At the cloud shell prompt change the directory back to the folder containing the terraform files, and then run ` terraform init ` again, and then, at the prompt enter ` terraform destroy `

