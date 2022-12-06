# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Describe and implement a container application with Kubernetes Engine

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the Project selector page, select or create a Google Cloud project.

5.  Make sure that billing is enabled for your Cloud project

7.	In the console, select Activate Cloud Shell

4.	In the cloud shell, enter the following commands:
```
gcloud config set project EnterYourProjectName
gcloud config set compute/zone us-east1-a
gcloud config set compute/region us-east1
```
5.	Create the GKE cluster by entering the following commands:
```
gcloud container clusters create-auto hello-cluster
```
6.	To connect and manage the cluster you’ll need credentials, enter the following commands:
```
gcloud container clusters get-credentials hello-cluster
```
7.	And, to deploy an application, enter the following commands:
```
kubectl create deployment hello-server --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
```

