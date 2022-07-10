# Chapter 8 : Launching Compute Service Resources for Scalability


## Why?

Traditional and modern development projects still recommend technical and non-technical controls to be properly assessed. In this case, we started our tutorial by understanding the importance of analyzing the Google Cloud Compute Engine service VM instance resource before further development. After a thorough but insightful analysis of our resources, we can consider implementing a line of business application or service in a VM instance.

## Objectives

In these tasks, you will learn how to configure and create virtual machine cloud resources in Google Cloud. You will also learn helpful tips, and potential pitfalls that encumber beginners.
Objectives
After completing these tasks, you will be able to achieve the following:
•	Describe and configure a VM instance
•	Describe and configure Machine type
•	Describe and configure Boot disk
•	Describe and configure Networking
Prerequisites
Recommended requirements for completing all tasks:
•	An updated version of Windows 8.1 or later, MAC 10.15 or later, or Linux Ubuntu 18.04 or later, computer operating system.
•	An up to date and secure internet browser (Chrome or Edge are recommended)
•	Instructions are located either:
o	In chapter 8, titled, Launching Compute Service Resources for Scalability, in the section labeled Virtual Machines.
o	Navigate online to https://github.com/PacktPublishing/Cloud-Computing-for-Beginners/tree/main/Instructions/Chapter8/VM
•	Access to a Google Cloud Platform account with the required privileges to create and manage all VPC resources and dependencies.
o	How to create a Google Cloud Platform free account for training purposes only?
	https://cloud.google.com/free/.
	https://cloud.google.com/resource-manager/docs/manage-google-cloud-resources

Note: The author is using a Windows 10 OS (operating system), and Chrome or Edge browser.
Important: You should FORK, Clone or Download and follow along with the step-by-step tasks in GitHub or described herein. I recommend using GitHub in conjunction with the book because any parts written in code are more clearly defined in GitHub. However, that’s my preference, you may prefer the book format.
“READY?”
Start the tasks to launch a Google Cloud Compute Engine VM instance.
TO DO 0: Subscribing to Google Cloud Platform
Task 1: Sign into Google Cloud Platform
1.	Select the Edge or Chrome browser on your computer and search for https://cloud.google.com/free/.
2.	After the website loads, select Get started for free.
3.	In the accounts.google.com website select Create account. And then select Create a new Gmail address instead. Here are several email account name examples: (Replace Example with your name or alias)
a.	 Example.lastname@gmail.com
b.	Example98765@gmail.com
4.	Follow the remaining prompts and populate all required fields to conclude the new account creation process.
5.	Note: I have elected to exclude any guidance pertaining to billing details which include personal identifiable information.
6.	Insight: Here are several resources to help you create and manage your Google Cloud Platform free account to ensure you don’t incur substantial costs.
a.	https://cloud.google.com/free/

Tasks
TO DO 3: Launch a Google Cloud VM instance.
Task 1: Describe and configure a VM instance.
In this task, you will launch a VM instance using the Google Cloud Compute Engine.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/).
2.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
3.	Make sure that billing is enabled for your Cloud project
4.	In the search field, enter the search parameter VM. And then select VM instances.
5.	In the Compute Engine page select CREATE INSTANCE.
6.	Update the following settings:
1.	Name: instance-1
2.	Region: <Select a region>
3.	Zone: us-central1-a
a.	The zone refers to an availability zone location in a region.
Task 2: Describe and configure Machine type.
In this task, you will configure a Machine type.

1.	In the Machine configuration section, review the series, which correlates with the machine family, and the machine type which denotes the compute capacity size.
Task 3: Describe and configure a boot disk.
In this task, you will configure a boot disk.

1.	In the Machine configuration section, review the series which correlates with the machine family, and the machine type which denotes the compute capacity size.

Task 4: Describe and configure Networking
In this task, you will review and configure the network settings.


1.	Review the Firewall section, select Allow HTTPS traffic, which in-turn configures an inbound rule. Deselect Allow HTTPS traffic.
2.	Access the context menu in the Networking section, and then review the settings that support custom hostnames, and Network interfaces.
3.	Select, Create, and wait for the instance status.
In these tasks, you have created a Google Cloud Compute Engine virtual machine instance and dependencies

