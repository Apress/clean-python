import re


def get_unique_emails(file_name):
    """
    Get all unique emails.
    """
    for line in read_file(file_name):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in match:
            yield email


def read_file(file_name):
    """
    Read file and yield each line.
    """
    with open(file_name) as fread:
        for line in fread:
            yield line

def print_email_list():
    """
    Print list of emails
    """
    for email in get_unique_emails('duplicate_emails'):
        print(email)
