# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Create and configure an Elastic File System

1.	Sign into the [AWS Management Console](https://console.aws.amazon.com/console/)

1.	Launch AWS CloudShell.

1.	In the CloudShell command line enter the following command to create an AWS EFS file system:
```
aws efs create-file-system \
--encrypted \
--creation-token FileSystemToken \
--tags Key=Name,Value=tag1 \
--region us-west-2 \
--profile adminuser
```
1.	Copy the file system Id output.

1.	Create a mount target for your Elastic File System in a subnet on your AWS Availability Zone where you’ve deployed an EC2 instance by entering the following command:
```
aws efs create-mount-target \
--file-system-id <enter-file-system-id> \
--subnet-id  <enter-subnet-id> \
--security-group <enter-securityId-group-created-for-mount-target> \
--region us-west-2 \
--profile adminuser
```
1. You will need to collect some information, namely the Domain Name System (DNS) name of your EC2 instance. 
> Note: For example,ec2-xx-xxx-xxx-xx.us-east-1.compute.amazonaws.com.

8.	And you will also require the DNS name of your file system. For example, <enter-file-system-id>.efs.us-east-1.amazonaws.com.

> Note: You will require connecting to your EC2 instance to install a client (agent). While this book covers the essentials it does not detail how to remote access manage EC2 instances. However, there is a chapter that describes resources needed for you to continue your learning journey and thus learn how to connect to an EC2   instance post launch. Review Chapter 13, Enhancing the Continuous Learning Journey.

9.	After you have connected to the EC2 instance, we recommend updating the system and installing nfs-utils by entering the following command:
```
sudo yum -y install nfs-utils
```
10.	Use the following commands to mount the Elastic file system on one or more EC2 instances:
```
mkdir ~/efs-mount-point

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport <enter-mount-target-DNS>:/  ~/efs-mount-point
```
11.	After successfully configuring the mount point, you can review the directory and create files.
