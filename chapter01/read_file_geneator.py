def read_file(file_name):
    """Read the file line by line."""
    fread = open(file_name, "r")
    data = [line for line in fread if line.startswith(">>")]
    return data
