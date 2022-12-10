# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Configure and create a Google Cloud Filestore instance

1.	Sign into the [Google Cloud Console](https://console.cloud.google.com/)

1.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

1.	Launch CloudShell

1.	Create the project container to manage our resources by entering the following commands:
```
gcloud projects create <enter-project-name>
```
1.	Next, create a virtual machine instance to be used as the client by entering the next commands:
```
gcloud compute instances create nfs-client --zone=us-central1-c --image-project=debian-cloud --image-family=debian-10 --tags=http-server
```
1.	Create a Filestore instance by entering the following commands:
```
gcloud beta filestore instances create nfs-server --zone=us-central1-c --tier=BASIC_HDD --file-share=name="vol1",capacity=1TB --network=name="default"
```
1.	Retrieve the Filestore instance IP address by entering the following commands:
```
gcloud filestore instances describe nfs-server --zone=us-central1-c
```
1.	Connect to the compute engine instance, install NFS, and create the mount directory by entering the following commands:
```
gcloud compute ssh nfs-client
sudo apt-get -y update &&
sudo apt-get -y install nfs-common
sudo mkdir /mnt/cceb
```
1.	Enter the next command to mount the file share:
```
sudo mount <enter-IP>:/vol1 /mnt/cceb
```
1.	After you have successfully created and configured Google Cloud Filestore review the resource.

> Note: Do not forget to delete all resources immediately to stop incurring charges
