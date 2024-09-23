"""sql injection validator example"""
from src.validators import number_validator, sql_validator


@sql_validator
def sql_user_input(data):
    """User input"""

    query = f"SELECT * FROM users WHERE name = '{data}'"
    # execute_query(query)
    return True


@number_validator
def number_input(num):
    """Number input"""
    # process_number(num)
    return True
