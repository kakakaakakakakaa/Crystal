def leet(text):
	leest = ["i","e","a","s","t","b","o","I","E","A","S","T","B","O"]
	result = ""
	for letter in text:
		if letter in leest:
			if letter == "i":
				result = result + "1"
			elif letter == "e":
				result = result + "3"
			elif letter == "a":
				result = result + "4"
			elif letter == "s":
				result = result + "5"
			elif letter == "t":
				result = result + "7"
			elif letter == "b":
				result = result + "8"
			elif letter == "o":
				result = result + "0"
			elif letter == "I":
				result = result + "1"
			elif letter == "E":
				result = result + "3"
			elif letter == "A":
				result = result + "4"
			elif letter == "S":
				result = result + "5"
			elif letter == "T":
				result = result + "7"
			elif letter == "B":
				result = result + "8"
			elif letter == "O":
				result = result + "0"
		else:
			result = result + letter
	return result