-- Create tests users
INSERT INTO person
    (
    username, password,
    firstname, lastname, national_code, sexual, birthday, maried, section, type, employee_id, employment_date, salary,
    absolute_security_level, read_security_level, write_security_level, absolute_integrity_level, read_integrity_level, write_integrity_level
    )
VALUES
    (
        'doctor', 'doctor',
        'doctor', 'doctor', '11111111111', 'man', '2017-03-14', true, 'doctor' , '1', '2', '2017-03-14', 1000000,
        -1, 9, 1, -1, 1, 9
    ),
    (
        'nurse', 'nurse',
        'nurse', 'nurse', '22222222222', 'women', '2017-03-15', false, 'nurse', '1', '3', '2017-03-15', 500000,
        -1, 8, 2, -1, 2, 8
    ),
    (
        'servicer', 'servicer',
        'servicer', 'servicer', '44444444444', 'women', '2017-03-16', false, 'employee', '1', '4', '2017-03-16', 250000,
        -1, 7, 3, -1, 3, 7
    ),
    (
        'patient', 'patient',
        'patient', 'patient', '33333333333', 'women', '2017-03-17', false, 'patient', '1', null, null, null,
        -1, 6, 4, -1, 4, 6
    );

INSERT INTO doctor
    (major, username)
VALUES
    ('Master of Doctors', 'doctor');

INSERT INTO nurse
    (username)
VALUES
    ('nurse');

INSERT INTO employee
    (carrer, username)
VALUES
    ('servicer', 'servicer');

INSERT INTO patient
    (patient_type, drugs, username, doctor_username, nurse_username)
VALUES
    ('canser', 'canser drug', 'patient', 'doctor', 'nurse');