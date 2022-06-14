# Cloud Computing Essentials for Beginners
Initial repo during beta dev
![Logo of the project](https://www.stratospherenetworks.com/blog/wp-content/uploads/2020/05/iStock-1137011043.jpg)

# Name of the project
## Cloud Computing Essentials for Beginners

> A brief description of your project.

>> Cloud Computing Essentials for Beginners is a compendious volume focused on educating beginning practitioners on how to master modern cloud computing essentials required to prepare for accreditation to succeed in any technology centric industry.

>> Initially you’ll be enlightened on cloud computing and its various models. Then you will learn how to plan, and implement infrastructure services, platform services and configure software as a service types, this includes step-by-step demonstrations, review questions, and optimization recommendations derived from certified experts in the industry utilizing Microsoft, Amazon, and Google cloud computing services.

>> Cloud Computing Essentials for Beginners includes hands-on tutorials, and self-assessment questions. This easy-to-follow guide will teach you the essentials of cloud computing services.

## Installing / Getting started

A quick introduction of the minimal setup you need to get started.

1. Visitors can clone the repo or download seperately the directory files to a local machine.

1.  Install the [Google Cloud SDK](https://cloud.google.com/sdk/).  The Google Cloud SDK
    is required to deploy .NET applications to App Engine.

1.  Install the [.NET Core SDK, version 2.0](https://github.com/dotnet/core/blob/master/release-notes/download-archives/2.0.5-download.md)
    or newer.




### Launch an application using the App Engine platform
1. In the Google Cloud Platform console, search for APIs & Services, and then search for Google App Engine Flexible Environment (API), select Enable API.

1. dotnet restore

1. dotnet publish -c Release

1. gcloud app deploy .\bin\Release\netcoreapp2.1\publish\app.yaml

