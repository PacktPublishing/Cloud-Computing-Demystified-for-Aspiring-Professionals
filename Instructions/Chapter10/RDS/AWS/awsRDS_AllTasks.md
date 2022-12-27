# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Developing Amazon Aurora DB table

1.	Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/)

3.	Using the search field, enter cloudformation, and then select Ccloud formation.

5.	Select Create stack and then choose, select Select with new resources, from the menu.

7.	Select Upload a template file, select Choose file, and then select auroraDB.yml from the directory path ~ Cloud-Computing-Demystified-for-Aspiring-Professionals/tree/main/Allfiles/Chapter10/RDS/AWS.

9.	Select View in designer, and in the CloudFormation designer dashboard, locate and update the YAML templates Description property value.

11.	Select the create stack icon.

13.	On the Create stack page, select Nnext, and then enter a unique password, and username value in the parameters section, and then select Next.

15.	Select Next, and then select Create stack.

17.	Enter RDS in the search field, and then select RDS.

19.	In the Amazon RDS dashboard, select Databases and review the database instance you created utilizing Amazon CloudFormation’s template and designer.
