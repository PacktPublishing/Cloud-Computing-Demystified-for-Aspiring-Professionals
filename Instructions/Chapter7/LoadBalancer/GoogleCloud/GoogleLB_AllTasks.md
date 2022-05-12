# Tasks
## TO DO 1: Implement a Google Cloud Load Balancer.
To help you the reader successfully implement a service. I’ve elected to utilize IaC tools and patterns to streamline creation.
This book is not intended to replace an instructor-led course. Instructor led courses allocate the time recommended to learn all the components of a service. I do provide recommendations on how to improve your learning experience with instructor led courses in chapter 13 titled Enhancing the Continuous Learning Journey.

# Task 1: Describe and configure a Google Cloud Load Balancer.

In this task, you will implement a Google Cloud load balancer using Terraform.

1.	Sign in to the [Google Cloud Console] (https://console.cloud.google.com/).

2.	In the console, enter Cloud Run API in the search field, and then select Cloud Run API.

3.	In the Cloud Run API page, select ENABLE.

4.	In the console, select Activate Cloud Shell.

5.	Note: If you followed the previous recommendations to FORK, and clone or download the GitHub repository directory and files to your local machine. You can upload any files to help complete tasks. For example, you can clone your GitHub forked copy in step 6 listed below. In step 7, you can change directory (cd) to the folder/directory where the Terraform files are located.

6.	In cloud shell, at the prompt, enter git clone <GitHub repo URL>

7.	Next, enter cd ~/Instructions/Chapter7/VNET/GoogleCloud to change to the directory containing the terraform files.

8.	Set the project by entering PROJECT=YOUR_PROJECT

9.	Next, enter gcloud config set project ${PROJECT}

10.	Configure the Terraform environment by entering:
[[ $CLOUD_SHELL ]] || gcloud auth application-default login
export GOOGLE_PROJECT=$(gcloud config get-value project)

11.	Initialize Terraform by entering terraform init

12.	And then implement the resources defined in the Terraform files like the load balancer by entering terraform apply -var=project_id=$PROJECT \
-var=ssl=false -var=domain=null

13.	Resource creation may take several minutes.

14.	If you encounter any prompts, enter yes to continue.

15.	After successful resource creation, review the resources/ assets governed by your Google Cloud project.

16.	After reviewing the load balancer resources. I recommend you delete all resources to control incurring additional charges.

17.	At the cloud shell prompt, if active, if not, activate, and then change directory back to the folder containing the terraform files, and then run terraform init again, and then, at the prompt enter terraform destroy

