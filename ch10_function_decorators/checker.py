from functools import wraps

from flask import session


def check_logged_in(func: object) -> 'function':
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session.keys():
            return func(*args, **kwargs)
        return 'You are NOT logged in.'

    return wrapper
