create table doctor
(
    id int primary key not null,
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
    absolute_security_level int,
    read_security_level int,
    write_security_level int
);
create table nurse
(
    id int primary key not null,
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
    absolute_security_level int,
    read_security_level int,
    write_security_level int
);

create table employee
(
    id int primary key not null,
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
    absolute_security_level int,
    read_security_level int,
    write_security_level int
);

create table patient
(
    id int primary key not null,
    firstname text not null,
    lastname text not null,
    national_code int not null,
    sexual text not null,
    birthday date not null,
    maried boolean not null,
    patient_type text,
    drugs text,
    section text,
    doctor_id int references doctor(id),
    nurse_id int references nurse(id),
    absolute_security_level int,
    read_security_level int,
    write_security_level int
);
