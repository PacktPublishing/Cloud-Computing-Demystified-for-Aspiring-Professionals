# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task: Create and configure Eventarc in Google

1.	Sign into the [Google Cloud Console](https://console.cloud.google.com/)

1.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

1.	Enable the Cloud Run, Cloud Logging, Cloud Build, Pub/Sub, Eventarc APIs.

1.	In the Google Cloud console, activate Cloud Shell. Enter the following commands:
```
gcloud components update
gcloud config set project <EnterPROJECT_ID>
gcloud config set run/region us-central1
gcloud config set run/platform managed
gcloud config set eventarc/location us-central1
```
5.	Next, enable audit logs read and write by entering the following commands:
```
gcloud projects get-iam-policy <EnterPROJECT_ID > /tmp/policy.yaml
```
6.	Edit the YAML file by only adding the following information:
```
auditConfigs:
- auditLogConfigs:
  - logType: ADMIN_READ
  - logType: DATA_WRITE
  - logType: DATA_READ
  service: storage.googleapis.com
```
7.	Next, set your YAML policy by entering the following commands:
```
gcloud projects set-iam-policy PROJECT_ID /tmp/policy.yaml
```
8.	Assign the eventarc.eventReceiver role permission to the compute engine service by entering the following commands:
```
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --role='roles/eventarc.eventReceiver'
```
9.	Create the storage bucket event source by entering the following commands:
```
gsutil mb -l us-central1 gs://events-cceb-EnterPROJECT_ID/
```
10.	Create a Cloud Run service that handles the events routed by Eventarc by entering the following commands:
```
git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

cd python-docs-samples/eventarc/audit-storage
```
11.	Build and deploy the container image by entering the following commands:
```
gcloud builds submit --tag gcr.io/PROJECT_ID/helloworld-events

gcloud run deploy helloworld-events \
   --image gcr.io/PROJECT_ID/helloworld-events \
    --allow-unauthenticated
```
12.	Configure the Eventarc trigger that will route events from the storage to the Cloud Run service by entering the following commands:
```
gcloud eventarc triggers create events-cceb-trigger \
      --destination-run-service=helloworld-events \
      --destination-run-region=us-central1 \
      --event-filters="type=google.cloud.audit.log.v1.written" \
      --event-filters="serviceName=storage.googleapis.com" \
      --event-filters="methodName=storage.objects.create" \
      --service-account=<EnterPROJECT_NUMBER>-compute@developer.gserviceaccount.com
```
13.	If you upload a file to Google Cloud Storage bucket. The event will generate event data that will send event messages to the Cloud Run service

> Note: Do not forget to delete all resources immediately to stop incurring charges

