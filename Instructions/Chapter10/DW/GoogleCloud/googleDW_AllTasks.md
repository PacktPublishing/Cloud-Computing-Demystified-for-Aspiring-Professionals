# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 10 Developing Database Service Resources at Scale
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Develop Google Cloud BigQuery Service

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)
2.	
3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
4.	
5.	Enable the BigQuery API.
6.	
7.	Search for BigQuery, and then select BigQuery.
8.	
9.	In the type to search field, enter  ` bigquery-public-data `
10.	Select More Actions, and then select Open.
11.	
12.	In the BigQuery page, select + Compose new query and review the Editor field.
13.	
14.	In the Editor field, enter the following commands:
```
SELECT
  name, gender,
  SUM(number) AS total
FROM
  `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY
  name, gender
ORDER BY
  total DESC
LIMIT
    10
```
9.	After you enter the preceding code syntax, select Run


