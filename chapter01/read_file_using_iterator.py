def read_file(file_name):
    """Read the file line by line."""
    with open(file_name) as fread:
        for line in fread:
            yield line


for line in read_file("logfile.txt"):
    print(line.startswith(">>")