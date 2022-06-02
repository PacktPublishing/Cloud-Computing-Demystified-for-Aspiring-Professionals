storageid=$(az storage account show --name $storagename --resource-group <EnterResourceGroupName> --query id --output tsv)
queueid="$storageid/queueservices/default/queues/$queuename"
topicid=$(az eventgrid topic show --name <EnterTopicName> -g gridResourceGroup --query id --output tsv)

az eventgrid event-subscription create \
  --source-resource-id $topicid \
  --name <EnterUniqueName> \
  --endpoint-type storagequeue \
  --endpoint $queueid \
  --expiration-date "<Enteryyyy-mm-dd>"