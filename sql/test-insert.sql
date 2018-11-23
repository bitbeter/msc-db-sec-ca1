INSERT INTO "person"
    (username,password,type,id,absolute_security_level,read_security_level,write_security_level,absolute_integrity_level,read_integrity_level,write_integrity_level)
VALUES
    ('doctor', 'doctor', 'doctor', 1, -1, 9, 1, -1, 1, 9),
    ('nurse', 'nurse', 'nurse', 1, -1, 8, 2, -1, 2, 8),
    ('servicer', 'servicer', 'servicer', 2, -1, 7, 3, -1, 3, 7),
    ('patient', 'patient', 'patient', 1, -1, 6, 4, -1, 4, 6);

INSERT INTO "employee"
    (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,carrer,username)
VALUES
    ('servicer', 'servicer', 'servicer', 'man', '2017-10-13', 'true', '1', '2', '2017-10-13', 100000, 'admin', 'admin');

INSERT INTO "doctor"
    (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,major,username)
VALUES
    ('doctor', 'doctor', 'doctor', 'man', '2017-10-13', 'true', '1', '1', '2017-10-13', 1230213, 'Master of Doctors', 'doctor');

INSERT INTO "nurse"
    (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,username)
VALUES
    ('nurse', 'nurse', 'nurse', 'woman', '2017-10-13', 'true', '1', '1', '2017-10-13', 123124, 'nurse');

INSERT INTO "patient"
    (firstname,lastname,national_code,sexual,birthday,maried,section,patient_type,drugs,username,doctor_username,nurse_username)
VALUES
    ('patient', 'patient', 'patient', 'man', '2017-10-13', 'false', '1', 'canser', 'canser drug', 'patient', 'doctor', 'nurse');