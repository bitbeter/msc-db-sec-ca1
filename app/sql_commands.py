SQL_COMMANDS = {
    "update-user-access":
    """
    UPDATE "person"
    SET absolute_security_level = %s ,read_security_level = %s ,write_security_level = %s ,absolute_integrity_level = %s ,read_integrity_level = %s ,write_integrity_level = %s 
    WHERE username = %s;
    """,
    
}
