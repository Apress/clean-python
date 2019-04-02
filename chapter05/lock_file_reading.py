from filelock import FileLock

def write_file(file_name):
    with FileLock(file_name):
        # work with the file as it is now locked
        print("Lock acquired.")
