# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure VPC firewall rules for built-in network security

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project
> Note: You will need to create a VPC. To create a VPC, use the instructions in Chapter 7.

3.	Make sure that billing is enabled for your Cloud project.

5.	Activate Cloudshell.

7.	In the Cloudshell command line interface enter the following commands replacing all placeholders:
```
gcloud compute firewall-rules create NAME \
    [--network <placeholder>; default="default"] \
    [--priority < placeholder >;default=1000] \
    [--direction (<placeholder >); default="ingress"] \
    [--action (deny | allow )] \
    [--target-tags < placeholder >] \
    [--target-service-accounts=<IAM_SERVICE_ACCOUNT>] \
    [--source-ranges <CIDR_RANGE>] \
    [--source-tags <TAG,TAG>,] \
    [--source-service-accounts=<IAM_SERVICE_ACCOUNT>] \
    [--destination-ranges <CIDR_RANGE>] \
    [--rules (PROTOCOL[:PORT[-PORT]],[PROTOCOL[:PORT[-PORT]],...]] | all ) \
    [--disabled | --no-disabled] \
    [--enable-logging | --no-enable-logging] \
    [--logging-metadata LOGGING_METADATA]
```
8. Using the Google Cloud Console, search and select firewall rules.

9. Review the firewall rules.


