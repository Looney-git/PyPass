with open(os.path.expanduser('~')+"/.zprofile", 'a') as f:

	f.write("\nalias pypass=\"sudo python3 ~/.pypass/pypass.py\"")
