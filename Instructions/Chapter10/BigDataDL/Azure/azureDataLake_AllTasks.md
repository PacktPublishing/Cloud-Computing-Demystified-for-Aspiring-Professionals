# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 10 Developing Database Service Resources at Scale
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.
> 
> **Note**: The task steps are considered intermediate to expert thus the instructions are highlevel making the task challenging. Try this challenge without using step-by-step instructions. AWS Documentation includes instructions if the challenge is to difficult.

## Task 1: Develop Azure Data Lake

1.	Sign in to the [Azure Portal](https://portal.azure.com/)
2.	
3.	Create a Storage Account.
4.	
5.	Configure Azure Data Lake Storage Gen2 on the Storage Account.
6.	
7.	Download AzCopy.
8.	
9.	Download the Bureau of Transportation Statistic files.
10.	
11.	Copy the files to your Azure Data Lake.
12.	
13.	Create or reuse Azure Synapse Analytics from the section herein titled Developing Data Warehouse Services.
14.	
15.	And lastly, explore your data using SQL queries like the following:
```
SELECT
    TOP 100 *
FROM
    OPENROWSET(
        BULK 'https://<enter-storage-account-name>.dfs.core.windows.net/<container-name>/folder1/On_Time.csv',
        FORMAT='CSV',
        PARSER_VERSION='2.0'
    ) AS [result]
```

