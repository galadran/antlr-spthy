
# Iterate through the file
# ignore every character until you get to rule. 
# Then get every character until the end (])
# Return a string filled with the rules
# and a string filled with not the rules and a unique 
# symbol to replace to reinsert the rules

import sys

def handleComments(s,i,limit):
	pt = ''
	if s[i:i+2] == '//':
		while s[i] != '\n' and i < limit:
			pt += s[i]
			i += 1
	elif s[i:i+2] == '/*':
		while s[i:i+2] != '*/' and i < limit:
			pt += s[i]
			i += 1
	return (pt,i)

s = open(sys.argv[1],'r').read()

pt = ''
first = True
rules = ''
i = 0
limit = len(s)
s += '\n\n\n\n'
while i < limit:
	ptc, i = handleComments(s,i,limit)
	pt = pt + ptc 
	if s[i:i+4] == 'rule':
		count = 0
		while count < 3:
			if s[i] == ']':
				count += 1
			elif s[i:i+3] == '-->':
				count += 1
			if first:
				first = False
				pt = pt + '\n RULESUBHERE \n'
			ptc, i = handleComments(s,i,limit)
			# Throwing away comments in rules
			rules += s[i]
			i += 1
		rules += '\n\n'
	else:
		pt += s[i]
		i += 1

print(pt)
print('###')
print(rules)


