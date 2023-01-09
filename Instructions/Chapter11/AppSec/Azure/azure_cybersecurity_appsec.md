# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure built-in App security using TLS

1.	Sign in to the [Azure Portal](https://portal.azure.com/)
> Note: Select the Azure App Service application you created in the previous chapter. If required, recreate the Azure App Service application using the instructions located in Chapter 8.
> Note: Select any non-free tier App Service plan to add certificates.
2. Add a custom domain.
3. Add binding.
4. Add a certificate for custom domain.
5. Upload a certificate following the instructions located here:
> Link: https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate?tabs=apex%2Cportal#upload-a-private-certificate
6. Configure a binding using the instructions located here:
> Link: https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#prerequisites
7. Require HTTPS by selecting TLS/SSL settings.
8. Set HTTPS Only to On.

> Note: Do not forget to delete all resources immediately to stop incurring charges
