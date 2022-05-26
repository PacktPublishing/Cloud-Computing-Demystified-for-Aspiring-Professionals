subscription="xxxxxxxxxxxxxxxxxxxxxxx" # add subscription ID here

az account set -s $subscription

# Function app and storage account names must be globally unique.

# Variable block
let "randomIdentifier=$RANDOM*$RANDOM"
location="eastus" # Enter and replace with your region value preference
resourceGroup="cceb-azure-functions-rg-$randomIdentifier"
tag="function-app-consumption-python"
storage="ccebaccount$randomIdentifier"
functionApp="cceb-serverless-python-function-$randomIdentifier"
skuStorage="Standard_LRS"
functionsVersion="4"
pythonVersion="3.9"

# Create a resource group
echo "Creating $resourceGroup in "$location"..."
az group create --name $resourceGroup --location "$location" --tags $tag

# Create an Azure storage account in the resource group.
echo "Creating $storage"
az storage account create --name $storage --location "$location" --resource-group $resourceGroup --sku $skuStorage

# Create a serverless python function app in the resource group.
echo "Creating $functionApp"
az functionapp create --name $functionApp --storage-account $storage --consumption-plan-location "$location" --resource-group $resourceGroup --os-type Linux --runtime python --runtime-version $pythonVersion --functions-version $functionsVersion