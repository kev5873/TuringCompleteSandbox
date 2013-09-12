from sys import argv

stack = {}

def setVariable(name, value):
	stack[name] = value

def showVariable(name):
	if stack.has_key(name):
		return stack[name]
	else:
		return "Variable does not exist"

def add(x,y):
	z = float(x) + float(y)
	return z

def subtract(x,y):
	z = float(x) - float(y)
	return z

def multiply(x,y):
	z = float(x) * float(y)
	return z

def divide(x,y):
	if int(y) == 0:
		z = "Error cannot divide by 0"
	else:
		z = float(x) / float(y)
	return z

def main():
	script = open(argv[1], 'r')
	for line in script:
		if line.count(' ') == 2:
			comd = line.split(' ', 2)[0].rstrip()
			var1 = line.split(' ', 2)[1].rstrip()
			var2 = line.split(' ', 2)[2].rstrip()
			if comd == 'var':
				setVariable(var1, var2)
			if not var1.isdigit():
				var1 = showVariable(var1)
			if not var2.isdigit():
				var2 = showVariable(var2)
			if comd == 'add':
				print add(var1, var2)
			if comd == 'sub':
				print subtract(var1, var2)
			if comd == 'mul':
				print multiply(var1, var2)
			if comd == 'div':
				print divide(var1, var2)
		if line.count(' ') == 4:
			comd  = line.split(' ', 4)[0].rstrip()
			varName = line.split(' ', 4)[1].rstrip()
			operation = line.split(' ', 4)[2].rstrip()
			var1 = line.split(' ', 4)[3].rstrip()
			var2 = line.split(' ', 4)[4].rstrip()
			if comd == 'var':
				if not var1.isdigit():
					var1 = showVariable(var1)
				if not var2.isdigit():
					var2 = showVariable(var2)
				if operation == 'add':
					finalValue = add(var1, var2)
				if operation == 'sub':
					finalValue = subtract(var1, var2)
				if operation == 'mul':
					finalValue = multiply(var1, var2)
				if operation == 'div':
					finalValue = divide(var1, var2)
				setVariable(varName, finalValue)
		if line.count(' ') == 1:
			comd  = line.split(' ', 1)[0].rstrip()
			var1 = line.split(' ', 1)[1].rstrip()
			if comd == 'dsp':
				print showVariable(var1)

main()