import os

with open(os.path.expanduser('~')+"/.zprofile", 'a') as f:

	f.write("\nalias {}=\"{}\"".format(input("name of function   --> "), input("function contents  --> ")))