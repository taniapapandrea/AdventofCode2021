file1 = open('input1.txt', 'r')
input1 = [x.strip() for x in file1.readlines()]

n_inputs = len(input1)
n_digits = len(input1[0])
gamma_rate_binary = ''
epsilon_rate_binary = ''

for i in range(n_digits):
	ones = ['1' for x in input1 if x[i]=='1']
	if len(ones) > n_inputs/2:
		gamma_rate_binary += '1'
		epsilon_rate_binary += '0'
	else:
		gamma_rate_binary += '0'
		epsilon_rate_binary += '1'

gamma_rate_int = int(gamma_rate_binary, 2)
epsilon_rate_int = int(epsilon_rate_binary, 2)

print(gamma_rate_int*epsilon_rate_int)