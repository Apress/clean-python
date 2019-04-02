import re


def get_unique_emails(file_name):
    """
    Get all unique emails.
    """
    emails = set()
    for line in read_file(file_name):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in match:
            emails.add(email)
    return emails


def read_file(file_name):
    """
    Read file and yield each line.
    """
    with open(file_name) as fread:
        for line in fread:
            yield line
