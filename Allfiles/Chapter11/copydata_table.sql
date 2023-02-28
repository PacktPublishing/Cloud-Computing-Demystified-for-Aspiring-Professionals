copy patient_users from 's3://<s3bucketname>/patient_users.csv' 
iam_role default
delimiter ',' region '<aws region>';
