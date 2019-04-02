def read_lines_for_python(file_name, file_type):
    if not file_name or file_type not in ("txt", "html"):
         return None
    
    lines = []
    with open(file_name, "r") as fileread:
        for line in fileread:
            if "python" in line:
                return "Found Python"


if not read_lines_for_python("file_without_python_name", "pdf"):
    print("Not correct file format or file name doesn't exist")
