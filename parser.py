import sys

def check_char(char):
	ok = 0
	if (char.isdigit() == False and char != '^' and char != '.' and char != "*" and char != '-' and char != '+' and char != '=' and char != "X" and char != ' '):	
		return False
	return True

def check_power(equation, length):
	i = 0
	while i < length:
		if (equation[i] == 'X'):
			if (equation[i + 1] == '^'):
				if (equation[i + 2] != '2' and equation[i + 2] != '1' and equation[i + 2] != '0'):
					if (int(equation[i + 2]) > 2):
						print("Le degré de l'équation est trop élevé")
					return False
			else:
				return False
		i += 1
	return True
		
def spliter(equation, length):
	split_eq = []
	i = 0
	j = 0
	while (i < length):
		while (i < length and equation[i] == ' '):
			i += 1
		split_eq.append(equation[i])
		i += 1
		while (i < length and equation[i] != ' '):
			split_eq[j] += equation[i]
			i += 1
		j += 1
	print(split_eq)
	return split_eq

def checker(equation):
	length = len(equation)
	i = 0
	while i < length:
		if check_char(equation[i]) == False:
			return False
		i += 1
	if check_power(equation, length) == False:
		return False
	return True

def reuniter(split_eq):
	reunite_eq = []
	i = 0
	while (i < len(split_eq)):
		

def parser(equation):
	if checker(sys.argv[1]) == False:
		print("Bad character into the equation")
		sys.exit()
	split_eq = spliter(sys.argv[1], len(sys.argv[1]))
	print(len(split_eq))