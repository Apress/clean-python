def read_file(file_name):
    """Read given file and print lines."""
    try:
        fread = open("temp.txt")
        for line in fread:
            print(f"Line:  {line}")
    except IOError as error:
        print("Having issue while reading the file")
        raise
