# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 8 Launching Compute Service Resources for Scalability
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Deploy an application using App Engine.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

1.	In the Google Cloud console, on the Project selector page, select or create a Google Cloud project.

1.	Make sure that billing is enabled for your Cloud project

1.	In the console, enter App Engine API in the search field, and then select App engine flexible environment.

1.	Select Enable App Engine Flexible Environment.

1.	Search for APIs & Services, select App Engine Admin API, enable the App Engine Admin API.

1.	In the search field, enter App Engine, and then select App engine from the available options.

1.	In the App Engine dashboard, select Create Application.

1.	Select a region near you. Select Next.

1.	In the Resources section, select .NET as a language.

1.	Download and install the following resources to your local machine:

- Install the [Google Cloud SDK](https://cloud.google.com/sdk/)
- Install the [.NET Core SDK, version2.0](https://github.com/dotnet/core/blob/master/release-notes/download-archives/2.0.5-download.md)

1.	(Option #1) Install Google Cloud tools for Visual Studio.

1.	Then select the solution file located in the ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter8/WebApp directory for Google Cloud.

1.	The file is located within the dotnetappengineV3.zip compressed folder. Unzip or decompress the folder to access the files.

1.	Open the solution file and wait for Visual Studio to start. Locate the solution explorer view area.

1.	Right-click the solution in the solution explorer, select rebuild to restore the project files.

1.	Select the project located in the solution explorer area. Right-click the project, and then select publish to Google Cloud.

1.	Select your Google Cloud Project ID, and then select Publish. You may need to add a Google Cloud account and project if you have not already done so.

> Note: This may take several minutes.
1.	(Option #2) Using your local machines command-line tools, change directory to ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter8/WebApp/GoogleCloud/dotnetappengineV3
```
cd ~/Cloud-Computing-Demystified-for-Aspiring-Professionals/Allfiles/Chapter8/WebApp/GoogleCloud/dotnetappengineV3

dotnet restore

dotnet publish -c Release

gcloud app deploy .\bin\Release\netcoreapp2.1\publish\app.yaml
```
1. After successfully deploying, navigate online back to the App Engine dashboard and review your environment.
