import CrystalUtils
import os
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("Commands/") if isfile(join("Commands/", f))]

print("Welcome to CrystalOS")

while True:
	uinput = input("> ")
	if uinput == "exit":
		break
	elif uinput == "leetify":
		print("Input text to be leetified")
		uinput2 = input("> ")
		print(CrystalUtils.leet(uinput2))
	elif uinput == "help":
		print("Command List:")
		print("help: shows this message")
		print("leetify: leetifies a text")
		print("exit: exits Crystal")
	elif uinput == "reverse":
		print("Input text to be reversed")
		uinput = input("> ")
		result = ""
		for letter in uinput:
			result = letter + result
		print(result)
	else:
		filename=uinput+".py"
		if filename in onlyfiles:
			os.system("python3 Commands/"+uinput+".py")
		else:
			print("Invalid Command!")