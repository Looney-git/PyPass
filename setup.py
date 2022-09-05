import os

os.system("sudo mkdir ~/library/application\ support/clif")

os.system("sudo mv ~/git-drive/clif.py ~/library/application\ support/clif/")

with open(os.path.expanduser('~')+"/.zprofile", 'a') as f:

	f.write("\nalias clif=\"python3 ~/library/application\ support/clif/clif.py\"")

os.system("python3 ~/library/application\ support/clif/clif.py")