file1 = open('input.txt', 'r')
input1 = [x.strip() for x in file1.readlines()]
file1.close()

p_horizontal = 0
p_depth = 0

for i in input1:
	direction, distance = i.split()
	match direction:
		case 'forward': p_horizontal += int(distance)
		case 'down': p_depth += int(distance)
		case 'up': p_depth -= int(distance)		

print(p_horizontal*p_depth)