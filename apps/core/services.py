import os


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        return None


def mail(subject, email_template, recipient, context):
    pass
