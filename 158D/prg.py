c = "1 2 -3 4 -5 5 2 3"


n = len(c.split(' '))#int(input())

marks = [int(i) for i in c.split(' ')]

cnt = init_cnt = len(marks)
maxim = sum(marks)

init_angle = 360 / cnt 
cnt -= 1

while cnt >= 3:
	part = (360 / cnt) / init_angle
	print(360 / cnt)
	print((360/cnt).is_integer())
	if part.is_integer():
		part = int(part)
		maxim = max(maxim, 
			sum([m for idx, m in enumerate(marks) if idx % part == 0])
		)

	cnt -= 1

print(maxim)

		
		
