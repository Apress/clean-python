class ReadFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self ):
        self.file = open(self.name, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


file_name = "test.txt"


with ReadFile(file_name) as fread:
    fread.write("Learning context manager")
    fread.write("Writing into file")
