a = "{% static '" 
b = "' %}"
c = [0,0,0,0,0,0,0,0,0,0]
for i in range(9):
	c[i] = input()
	c[i] = a + c[i] + b
print(*c, sep = '\n')
