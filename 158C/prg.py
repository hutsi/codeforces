n = 7#int(input())

c = ['pwd', 'cd /home/vasya/../petya', 'pwd', 'cd ..', 'pwd', 'cd vasya/../petya', 'pwd']

dir = []

for i in range(0, n):
	op_to = c[i].split(' ') #input().split(' ')
	op = op_to[0]
	if op == 'pwd':
		if len(dir) == 0:
			print('/')
		else:
			print('/' + '/'.join(dir))
	else:
		to_parts = op_to[1].split('/')
		if to_parts[0] == '':
			dir = []
			del to_parts[0]
		for to_part in to_parts:
			if to_part == '..':
				dir.pop()
			else:
				dir.append(to_part)
			
		
		
