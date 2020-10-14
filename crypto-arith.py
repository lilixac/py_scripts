'''
How to get solution:
>>> python3 crypto-arith.py
>>> Enter the string to evaluate: send + more = money
>>> Solution found: <solution>
'''

import itertools

def solve(problem):
	y,w3 = problem.replace(' ','').split('=')
	w1,w2 = y.split('+')

	variables = set(w3)
	for i in w1:
		variables.add(i)
	for i in w2:
		variables.add(i)

	domain = range(10)
	for perm in itertools.permutations(domain, len(variables)):
		soln = dict(zip(variables, perm))

		def word_value(word):
			val = [soln[str(i)] for i in word]
			return sum(d*10**i for i,d in enumerate(val[::-1]))

		if not (soln[w1[0]] == 0 or soln[w2[0]] == 0 or soln[w3[0]] == 0):
			if word_value(w1) + word_value(w2) == word_value(w3):
				print("Solution found: ", word_value(w1), " + ", word_value(w2), " = ", word_value(w3))
				exit(1)

a = input("Enter the string to evaluate: ")
solve(a)
