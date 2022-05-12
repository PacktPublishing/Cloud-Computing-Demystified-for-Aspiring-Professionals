# Tasks
## TO DO 1: Implement an Azure Load Balancer.
Important: To help you the reader successfully implement a service; I have elected to utilize IaC like tools and services to streamline creation. However, this may impact your experience mastering all the components and features of the cloud computing service in this chapter.

# Task 1: Describe and configure an Azure Load Balancer.

In this task, you will implement an Azure load balancer using ARM Templates.


1.	Sign in to the [Azure Portal] (https://portal.azure.com/).

2.	In the portal, navigate and select **Create a resource**, and on the **Create a resource page**, enter template in the search services and marketplace field. And then select Template deployment.

3.	On the Template deployment (deploy using custom templates) page, select Create.

4.	On the Custom deployment page, select Build your own template in the editor.

5.	In the Edit template page, select Load file.

6.	Note: If you followed the previous recommendations to FORK, and clone or download the GitHub repository directory and files to your local machine. You can upload any files to help complete tasks.

7.	Select the file named azureloadbalancer.json located in the directory ~ /Cloud-Computing-Essentials-Beg\Allfiles\Chapter7\VNET\Azure. And then select Save on the Edit template page.

8.	In the Custom deployment page, enter the following parameter values:

1.	Resource group: azurelbrg

2.	Region: East US

a.	Any region with available resource capacity.

3.	Admin Username: <place holder for your name>

4.	Admin Password: Pa55w0rd12345

a.	This is not a strong password and is only an example.

b.	Create a strong password instead.

9.	On the Custom deployment page, select Review + create.

10.	After validation has passed, select Create.

11.	Azure template creation can take some time.

12.	Review the Azure resources created by using the search feature in the Azure portal.

13.	Delete the resources to prevent incurring further charges.

a.	Launch the cloud shell in the Azure portal.

b.	At the cloud shell command line prompt enter the following to delete the resources:
Az group delete –name <Enter your resource group name here>

14.	And then enter y at the next prompt.
