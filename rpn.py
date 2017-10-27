#!/usr/bin/python

def calculate(myarg): 
	stack = list()
	for token in myarg.split:
		if token == '+':
			arg1 = stack.pop();
			arg2 = stack.pop();
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg2 - arg1
			stack.append(result)
		else:
			stack.append(int(token))
	print (stack)
	return stack.pop()

def main():
	a = calculate("1 1 +")
	print (a)

if __name__ == "__main __":
	main()
	
