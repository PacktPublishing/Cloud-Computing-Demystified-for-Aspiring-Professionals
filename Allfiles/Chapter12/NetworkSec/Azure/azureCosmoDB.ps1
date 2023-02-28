# resource group name
$RESOURCE_GROUP_NAME = "cceb-cosmos-rg"
$LOCATION = "West US"

# Cosmo DB Name
$SUFFIX = Get-Random
$ACCOUNT_NAME = "cceb-$SUFFIX"

$parameters = @{
    Name = $RESOURCE_GROUP_NAME
    Location = $LOCATION
}
New-AzResourceGroup @parameters


$parameters = @{
    ResourceGroupName = $RESOURCE_GROUP_NAME
    Name = $ACCOUNT_NAME
    Location = $LOCATION
}
New-AzCosmosDBAccount @parameters