def get_file_name(file_name, file_type):
    if not file_name:
         raise ValueError("File name not found", file_type)
    return file_name, file_type

try:
    get_file_name('', txt)
except ValueError as err:
    print(err.args)
