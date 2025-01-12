
def u_cal(u, n):
	temp = u
	for i in range(n):
		temp = temp * (u + i)
	return temp

def fact(n):
	f = 1
	for i in range(2, n + 1):
		f *= i
	return f

n = 5
x = [100, 150, 200, 250, 300]

y = [[0.0 for _ in range(n)] for __ in range(n)]
y[0][0] = 958
y[1][0] = 917
y[2][0] = 865
y[3][0] = 799
y[4][0] = 712

for i in range(1, n):
	for j in range(n - 1, i - 1, -1):
		y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

for i in range(n):
	for j in range(i + 1):
		print(y[i][j], end="\t")
	print()

value = 275

sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1, n):
	sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)

print("\n Value at", value, "is", sum)

