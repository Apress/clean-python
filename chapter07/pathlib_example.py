import pathlib

path = pathlib.Path("error.txt")
path.resolve()
#  PosixPath("/home/python/error.txt")
 
path.resolve().parent == pathlib.Path.cwd()  #  False
