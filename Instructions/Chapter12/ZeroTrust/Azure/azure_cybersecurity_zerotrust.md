# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 11 Implementing Native Cyber Security Controls
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Managing Azure Directory MFA

1.	Sign in to the [Azure Portal](https://portal.azure.com/)

3.	Select Azure Active Directory.
>**Note**: If prompted to trial a free premium Azure Active Directory account to use this feature, proceed accepting each prompt to activate premium features.

5.	Select Security.
![image](https://user-images.githubusercontent.com/61672321/212175079-677b423a-5225-4fac-b7b0-88bc9f7e273d.png)


7.	Select Conditional Access.

9.	Select New Policy and create a new policy.

11.	Enter a unique name for your policy. Enter the following text, MultiFactorAuth.

13.	Select Users or workload

15.	Select the option labeled, Select users and groups.

17.	Enter your username in the search field and then click Select.

19.	Next, select Cloud apps or actions.

21.	Select, All cloud apps

23.	Select Grant, and then select Grant access.

25.	Select Require multi-factor authentication.
**Note** Review and comply with the following information on step 14.

14.	Configure and Managing Identity and Access Management MFA
> **Note**: Use the following link to review the steps required to enable MFA:

> Link: https://learn.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa

> Note: Do not forget to delete all resources immediately to stop incurring charges
