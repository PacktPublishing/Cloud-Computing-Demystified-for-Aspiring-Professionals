create table scientist_users(
    userid integer not null distkey sortkey,
    username char(20),
    firstname varchar(100),
    lastname varchar(100),
    email varchar(100)
);