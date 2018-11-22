create table auth
(
    -- Primary Key
    username text primary key not null,
    -- Fields
    password text not null,
    -- Security Levels
    absolute_security_level int,
    read_security_level int,
    write_security_level int
    absolute_integrity_level int,
    read_integrity_level int,
    write_integrity_level int
);

create table doctor
(
    -- Primary Key
    id int primary key not null,
    -- Fields
    firstname text not null,
    lastname text not null,
    national_code int not null,
    sexual text not null,
    birthday date not null,
    major text not null,
    maried boolean not null,
    eployee_id text unique,
    employment_date date,
    section text,
    salary int,
    -- Forigen Keys
    username text references auth(username)
);

create table nurse
(
    -- Primary Key
    id int primary key not null,
    -- Fields
    firstname text not null,
    lastname text not null,
    national_code int not null,
    sexual text not null,
    birthday date not null,
    maried boolean not null,
    eployee_id text unique,
    employment_date date,
    access_level int,
    section text,
    salary int,
    -- Forigen Keys
    username text references auth(username)
);

create table employee
(
    -- Primary Key
    id int primary key not null,
    -- Fields
    firstname text not null,
    lastname text not null,
    national_code int not null,
    sexual text not null,
    birthday date not null,
    major text not null,
    maried boolean not null,
    work text,
    eployee_id text unique,
    employment_date date,
    access_level int,
    section text,
    salary int,
    -- Forigen Keys
    username text references auth(username)
);

create table patient
(
    -- Primary Key
    id int primary key not null,
    -- Fields
    firstname text not null,
    lastname text not null,
    national_code int not null,
    sexual text not null,
    birthday date not null,
    maried boolean not null,
    patient_type text,
    drugs text,
    section text,
    -- Forigen Keys
    username text references auth(username),
    doctor_id int references doctor(id),
    nurse_id int references nurse(id)
);