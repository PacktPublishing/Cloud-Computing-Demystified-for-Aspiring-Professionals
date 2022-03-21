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

1. Visitors can clone the repo or download seperately the sample files to a local machine.

   a. Review the code and configuration files located in the directory path ~\Allfiles\Chapter5\paasGCPexample\paasDockerApp\hello-app

   b. This app has been containerized and the image is stored in Google's sample container registry. This registry is referenced in the command listed in the heading labeled "_Deploying / Publishing_"

2. Create an Google Cloud Platform account.
    a. Or use an existing Googl Cloud Platform account.
3. Activate Cloud Shell (recommended option)
4. Google Cloud SDK
5. Google Cloud CLI



what actually happens when you execute.

Deploys a web application to Google Kubernetes Engine Cluster

### Initial Configuration

1. Google Cloud Platform account is required.
2. Create a project
  a. Or use an existing project



## Developing

2. Learn Cloud Shell
3. Learn CLI
3. Learn Google Cloud GKE

This example does not include step-by-step instructions.
Readers are recommended to return and attempt recreating these examples after they have read the cloud computing essentials for beginners book.

### Building

If your project needs some additional steps for the developer to build the
project after some code changes, state them here:

Provide unique parameter values

### Deploying / Publishing

In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.
1. Create a GKE cluster
2. Deploy an application to the cluster
```
  a.kubectl create deployment hello-server --image=us-docker.pkg.dev/google-samples/containers/gke hello-app:1.0
```
3. Reveal the application to the internet

## Features

What can the features for this project accomplish?
* What's the main functionality
Create a GKE cluster and then deploy an application to the cluster

### Architecting
> Optionally readers can design a cloud computing architecture similar to examples illustrated in the book.
>> Readers can use either the pptx, powerpoint file and architecting icons or image files located in the directory ~/Allfiles/Chapter5/ to support diagramming a cloud computing PaaS resources.

## Contributing


"If you'd like to contribute, please fork(copy) the repository and use a feature (non master)
branch. Pull (colloborative review) requests are warmly welcome."

If there's anything else the developer needs to know (e.g. the code style
guide), you should link it here. If there's a lot of things to take into
consideration, it is common to separate this section to its own file called
`CONTRIBUTING.md` (or similar). If so, you should say that it exists here.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://github.com/PacktPublishing/Cloud-Computing-for-Beginners
- Repository: https://github.com/PacktPublishing/Cloud-Computing-for-Beginners
- Issue tracker: https://github.com/PacktPublishing/Cloud-Computing-for-Beginners
  - In case of sensitive bugs like security vulnerabilities, please contact
    david3651@live.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects: <place holder>
  - Your other project: <place holder>
  - Someone else's project: <place holder>


## Licensing

"The project is licensed under Packt Publishing."
