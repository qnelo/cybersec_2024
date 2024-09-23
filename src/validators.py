"""Validators decorators"""


def pattern_validator(args):
    """Pattern validator"""
    input_data = args[0]

    # implement a pattern validator here
    if input_data == "not valid":
        raise ValueError('Possible SQL Injection detected')
    return True


def sql_validator(func):
    """SQL Injection validator"""

    def wrapper(*args, **kwargs):
        """
        pattern_validator must
        raise valueError if sql injection detected
        """
        pattern_validator(args)

        return func(*args, **kwargs)

    return wrapper


def number_checker(args):
    """Number checker"""
    number_candidate = args[0]

    # implement a pattern validator here
    if number_candidate == "not valid":
        raise ValueError('Not number detected')
    return True


def number_validator(func):
    """Number validator"""

    def wrapper(*args, **kwargs):
        """
        number_validator must
        raise valueError if sql injection detected
        """
        number_checker(args)

        return func(*args, **kwargs)

    return wrapper
