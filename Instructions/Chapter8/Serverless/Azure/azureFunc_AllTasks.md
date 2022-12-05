# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Implement an Azure Function App

1.	Sign in to the [Azure Portal](https://portal.azure.com/)

1.	In the portal, navigate and select Cloud Shell, if prompted, create the storage account and file share requirements.

1.	In the cloud shell command line environment, ensure Bash mode is enabled, or select Bash from the context menu.

1.	Enter,  ` code . `

1.	Select the upload setting, then select Upload, and then select the azurePythonFunction.sh file from the following directory ~/Cloud-Computing-Demystified-for-    Aspiring-Professionals/Allfiles/Chapter8/Serverless/Azure

1.	Update the azurePythonFunction.sh bash file by replacing the subscription and storage account values with unique values.

1.  In the cloud shell command line interface, enter bash azurePythonFunction.sh.

1.	In the Azure portal search field, enter function app, and then select Function app.

1.	Select your function app.

1.	Select Functions, then select Create, and select Time trigger.

1.	Select Create.

1.	Select Code + Test, and then select Upload.

1.	Select the azureTimerFunction.py file from the following directory ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter8/Serverless/Azure

1.	Select Test/Run, then select Run, and finally select close and review the logs.
