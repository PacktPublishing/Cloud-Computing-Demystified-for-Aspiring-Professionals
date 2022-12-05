# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Describe and implement a container application with Kubernetes service.

1. Sign in to the [Azure Portal](https://portal.azure.com/)

3. In the portal, navigate and select Cloud Shell, follow the prompts, and complete the cloud shell creation.

5. In the cloud shell command line prompt, enter the following: ``` az group create --name pharmaResourceGroup --location eastus. ```

7. And then create an Azure Container Registry (ACR). Enter the following: ``` az acr create --resource-group pharmaResourceGroup --name <YourAcrName> --sku Basic ```

8. Create an AKS cluster using the following command, enter the following:
``` 
    az aks create \
    --resource-group pharmaResourceGroup \
    --name pharmaAKSCluster \
    --node-count 2 \
    --generate-ssh-keys \
    --attach-acr <EnterYourAcrName>
```
1. Install the Kubectl client, enter the following command:
```
az aks install-cli
```
7.	To connect to AKS, enter the following command:
```
az aks get-credentials --resource-group pharmaResourceGroup --name pharmaAKSCluster
```

