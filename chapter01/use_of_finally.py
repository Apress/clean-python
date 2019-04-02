def write_file(file_name):
    """Read given file line by line""""
    myfile = open(file_name, "w")
    try:
        myfile.write("Python is awesome")           # Raise TypeError
    finally:
        myfile.close()             # Executed before TypeError propagated
