from sys import argv

def main():
	script = open(argv[1])
	print script.read()
	print "Hello"

main()