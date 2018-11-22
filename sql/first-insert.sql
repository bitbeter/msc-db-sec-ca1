-- Create admin user
INSERT INTO person
    (
    username, password,
    firstname, lastname, national_code, sexual, birthday, maried, section, type, employee_id, employment_date, salary,
    absolute_security_level, read_security_level, write_security_level, absolute_integrity_level, read_integrity_level, write_integrity_level
    )
VALUES
    (
        'admin', 'admin',
        'admin', 'admini', '00000000000', 'man', '2017-10-01', true, 'employee', '1', '1', '2017-10-01', 10000000,
        -1, 10, 0, -1, 0, 10
    );