-- Create admin user
INSERT INTO "person"
    (username, password,type,id,absolute_security_level,read_security_level,write_security_level,absolute_integrity_level,read_integrity_level,write_integrity_level)
VALUES('admin', 'admin', 'employee', 1, -1, 10, 0, -1, 0, 10);

INSERT INTO "employee"
    (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,carrer,username)
VALUES('admin', 'admin', 'admin', 'man', '2017-10-13', 'true', '1', '1', '2017-10-13', 100000, 'admin', 'admin');