from contextlib import contextmanager


@contextmanager
def write_file(file_name):
    try:
        fread = open(file_name, "w")
        yield fread
    finally:
        fread.close()


with read_file("accounts.txt") as f:
    f.write("Hello, how you are doing")
    f.write("Writing into file")
