"""SQL Injection Validator tests"""
import unittest

from src.inputs import sql_user_input

sql_injections = [
    "1; DROP TABLE users",
    "' OR '1'='1",
    "'; EXEC xp_cmdshell('dir') --",
    "'; SHUTDOWN --",
    " ORDER BY 1--",
    " admin' --",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "' OR '1'='1' {",
    "' OR '1'='1' /*",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "' OR '1'='1' {",
    "' OR '1'='1' /*",
    "'; DROP TABLE users --",
    "'; SELECT * FROM users WHERE 'a'='a",
    "'; INSERT INTO users (username, password) VALUES ('admin', 'password') --",
    "'; UPDATE users SET password='password' WHERE username='admin' --",
    "'; DELETE FROM users WHERE 'a'='a",
    "'; EXEC sp_executesql N'SELECT * FROM users' --",
    "'; EXEC xp_cmdshell('net user hacker hacker /add') --"
]

valid_input_list = [
    "dropbox",
    "organization"
]


class TestSQLInjectionValidator(unittest.TestCase):
    """SQL Injection Validator test cases"""

    def test_user_input_with_valid_data(self):
        """Test user_input with valid data"""
        for valid_input in valid_input_list:
            self.assertTrue(sql_user_input(valid_input))

    def test_user_input_with_sql_injection(self):
        """Test user_input with SQL injection patterns"""
        for injection in sql_injections:
            with self.assertRaises(ValueError):
                sql_user_input(injection)


if __name__ == '__main__':
    unittest.main()
