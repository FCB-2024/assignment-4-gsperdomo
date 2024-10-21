## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	i = 1
	j = 1
	y = 1
	a = 0
	d = 0
	while (i <= x):
		if (x % i == 0):
			d = d + 1
		i = i + 1
	while (y < x):	
		while (j <= y):
			if (y % j == 0):
				a = a + 1
			j = j + 1
		if (a >= d):
			return("no anti-prime")
		else:
			y = y + 1
			j = 1
			a = 0
	if (a < d):
		return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	#print(x)
	x = int(sys.argv[1])
	print(main(x))
