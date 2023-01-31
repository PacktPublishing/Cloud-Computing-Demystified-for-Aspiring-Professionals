copy scientist_users from 's3://<s3bucketname>/scientist_users.txt' 
iam_role default
delimiter '|' region '<aws region>';
