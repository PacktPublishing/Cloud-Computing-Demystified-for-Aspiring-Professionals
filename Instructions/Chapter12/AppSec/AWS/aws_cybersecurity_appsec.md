# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure built-in App security using TLS

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)
> Note: Select the Elastic Beanstalk you created in a previous chapter. If required, recreate the Elastic Beanstalk using the instructions located in Chapter 8.
2. Create an X509 certificate for your application with OpenSSL.
> Note: OpenSSL is available on Elastic Beanstalk's Linux images. You can connect to an EC2 instance in a running environment.
3. Use the openssl genrsa command. Here is an example:
` openssl genrsa 2048 > privatekey.pem `
> Note: Create and sign an X509 certificate. Please use the following link to complete all necessary tasks: 
> Link: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html

## Task 2: Upload certificate

1. Use the AWS Command Line Interface (AWS CLI) to upload your certificate.
> Note: Upload a self signed certificate. Please use the following link to complete all necessary tasks: 
> Link: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl-upload.html

## Task 3: Configure an HTTPS listener for the load balancer

1. Use the Elastic Beanstalk console to set a listener and assign a certificate.
> Note: Configure a listener and assign a certificate. Please use the following link to complete all necessary tasks: 
> Link: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html

> Note: Do not forget to delete all resources immediately to stop incurring charges
