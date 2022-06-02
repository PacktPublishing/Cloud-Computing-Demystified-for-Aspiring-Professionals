az group create --name <EnterUniqueName> --location eastus

az provider register --namespace Microsoft.EventGrid

az provider show --namespace Microsoft.EventGrid --query "registrationState"

az eventgrid topic create --name <EnterUniqueName> -l eastus -g <EnterResourceGroupName>

storagename="<EnterUniqueName>"
queuename="<EnterUniqueName>"

az storage account create -n $storagename -g <EnterResourceGroupName> -l eastus --sku Standard_LRS
az storage queue create --name $queuename --account-name $storagename


