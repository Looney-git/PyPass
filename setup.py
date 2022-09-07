import os

os.system("sudo mkdir ~/.PyPass")

os.system("sudo mv ~/PyPass/PyPass.py ~/.PyPass/")

with open(os.path.expanduser('~')+"/.zprofile", 'a') as f:

	f.write("\nalias pypass=\"sudo python3 ~/.PyPass/PyPass.py\"")

os.system("python3 ~/.PyPass/PyPass.py")