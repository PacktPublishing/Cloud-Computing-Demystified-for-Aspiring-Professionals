# Chapter 7 : Implementing a Google Cloud VPC


## Why?

Traditional and modern development projects still recommend technical and non-technical controls to be properly assessed. In this case, we started our tutorial by understanding the importance of analyzing the cloud networking service resources before further development. After a thorough but insightful analysis of our network resources, organizations can consider implementing thier line of business application or service in a VPC.

## Objectives

After completing these tasks, you will be able to achieve the following:
-   Describe and configure a VPC
-	Describe and configure IP addresses
-	Describe and configure subnets
-	Describe and configure an internet gateway
-	Describe and configure routes

## Instructions

## Exercise 0

### Task 0: Setup and configure prerequisites

In this task, you will review and setup all required prerequisites

1. Review and follow suggested instructions located in a file named README.md located in the directory ~/Cloud-Computing-for-Beginners/tree/main/Instructions/Chapter7/VNET/GoogleCloud

> Note: After reviewing and complying with all required prerequisites denoted in the file mentioned above return to this file and continue to the next exercise task.

### Exercise 1

#### Task 1: Describe and configure a VPC

In this task, you will implement a VPC by using the Google Cloud Console.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/).

2.	In the search field, enter the search parameter value VPC. And then select
VPC network.

3.	In the VPC networks page select CREATE VPC NETWORK.

4.	In the Create a VPC network page, enter vnet0 in the Name field.

Task 2: Describe and configure IP addresses and subnets.
In this task, you will define and configure VPC IP addresses and subnets.

Insight: Google Cloud VPC supports custom and an automatic subnet... For further information read the book.

1.	In the Create a VPC network page, on the New subnet section, enter public-1 in the Name field.

2.	In the Create a VPC network page, on the New subnet section, select us-east1 in the Region field.

3.	In the Create a VPC network page, on the New subnet section, enter 10.0.0.0/24 in the Name field.

4.	In the Create a VPC network page, select ADD SUBNET.

5.	In the Create a VPC network page, on the New subnet section, enter private-1 in the Name field.

6.	In the Create a VPC network page, on the New subnet section, select us-east1 in the Region field.

7.	In the Create a VPC network page, on the New subnet section, enter 10.0.1.0/24 in the Name field.

8.	In the Create a VPC network page, select ADD SUBNET.

9.	In the Create a VPC network page, on the New subnet section, enter public-2 in the Name field.

10.	In the Create a VPC network page, on the New subnet section, select us-east1 in the Region field.

11.	In the Create a VPC network page, on the New subnet section, enter 10.0.2.0/24 in the Name field.

12.	In the Create a VPC network page, select ADD SUBNET.

13.	In the Create a VPC network page, on the New subnet section, enter private-2 in the Name field.

14.	In the Create a VPC network page, on the New subnet section, select us-east1 in the Region field.

15.	In the Create a VPC network page, on the New subnet section, enter 10.0.3.0/24 in the Name field.

16.	In the Create a VPC network page, select CREATE.

Task 4: Describe and configure routes and an internet gateway.
In this task, you will understand Google Cloud routes and its built-in internet gateway.

How would you go about reviwing the routes, which includes the internet gateway route?

Google Cloud Platform VPCs include their own system generated route tables which by default... For further information read the book.



