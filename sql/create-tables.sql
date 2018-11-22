create table person
(
    -- Primary Key
    username text primary key not null,
    -- Fields
    password text not null,
    firstname text not null,
    lastname text not null,
    national_code text not null,
    sexual text not null,
    birthday date not null,
    maried boolean not null,
    section text not null,
    type text not null,
    employee_id text unique,
    employment_date date,
    salary int,
    -- Security Levels
    absolute_security_level int,
    read_security_level int,
    write_security_level int,
    absolute_integrity_level int,
    read_integrity_level int,
    write_integrity_level int
);

create table doctor
(
    -- Primary Key
    id SERIAL primary key not null,
    -- Fields
    major text not null,
    -- Forigen Keys
    username text references person(username) on update cascade on delete cascade
);

create table nurse
(
    -- Primary Key
    id SERIAL primary key not null,
    -- Forigen Keys
    username text references person(username) on update cascade on delete cascade
);

create table employee
(
    -- Primary Key
    id SERIAL primary key not null,
    -- Fields
    carrer text,
    -- Forigen Keys
    username text references person(username) on update cascade on delete cascade
);

create table patient
(
    -- Primary Key
    id SERIAL primary key not null,
    -- Fields
    patient_type text,
    drugs text,
    -- Forigen Keys
    username text references person(username) on update cascade on delete cascade,
    doctor_username text references person(username),
    nurse_username text references person(username)
);