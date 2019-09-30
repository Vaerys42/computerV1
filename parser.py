import sys

def check_char(char):
	ok = 0
	if (char.isdigit() == False and char != '^' and char != '.' and char != "*" and char != '-' and char != '+' and char != '=' and char != "X" and char != ' '):	
		return False
	return True

def check_power(equation, length):
	i = 0
	while i < length:
		if (i + 1 < length and equation[i] == 'X' and equation[i + 1] != ' '):
			if (equation[i + 1] == '^'):
				if i + 2 >= length:
					return False
				if (equation[i + 2] != '2' and equation[i + 2] != '1' and equation[i + 2] != '0'):
					if (equation[i + 2].isdigit() and int(equation[i + 2]) > 2):
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
	return split_eq

def spliter_part2(eq):
	factor_eq = []
	j = 0
	while (j < len(eq)):
		tmp = []
		neg = 0
		if (j < len(eq) and eq[j] == '-'):
			neg = 1
		if (j!= 0):
			j += 1
		while (j < len(eq) and (eq[j][0] != '+' and eq[j][0] != '-' and eq[j][0] != '=')):
			tmp.append(eq[j])
			j +=1
		if neg == 1:
			tmp[0] = '-'+ tmp[0]
		factor_eq.append(tmp)
	return factor_eq


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

def parser(equation):
	if checker(sys.argv[1]) == False:
		print("Equation not well formated")
		sys.exit()
	split_eq = spliter(sys.argv[1], len(sys.argv[1]))
	split_eq = spliter_part2(split_eq)
	print(split_eq)
