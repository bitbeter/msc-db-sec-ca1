SQL_COMMANDS = {
    "login":  # Username and Password checking
    """
    SELECT * FROM person WHERE username=%s AND password=%s
    """,

    "create-user":  # Create New Person
    """
    INSERT INTO "person"
        (username,password,type,absolute_security_level,read_security_level,write_security_level,absolute_integrity_level,read_integrity_level,write_integrity_level)
    VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """,

    "create-doctor":  # Create New Doctor
    """
    INSERT INTO "doctor"
        (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,major,username)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """,

    "create-nurse":  # Create New Nurse
    """
    INSERT INTO "nurse"
        (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,username)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """,

    "create-employee":  # Create New Employee
    """
    INSERT INTO "employee"
        (firstname,lastname,national_code,sexual,birthday,maried,section,employee_id,employment_date,salary,carrer,username)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """,

    "create-patient":  # Create New Patient
    """
    INSERT INTO "patient"
        (firstname,lastname,national_code,sexual,birthday,maried,section,patient_type,drugs,username,doctor_username,nurse_username)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """,

    "update-user-access":
    """
    UPDATE "person"
    SET absolute_security_level = %s ,read_security_level = %s ,write_security_level = %s ,absolute_integrity_level = %s ,read_integrity_level = %s ,write_integrity_level = %s 
    WHERE username = %s;
    """,
    
}
