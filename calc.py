print("\nВведите пример,или exit для входа:",end=' ')
num = input()
result = eval(num)
print(result,end='')
res = result
while(True):
	x = input()
	if x=='exit':
		print('\nСпасибо за использования....\n')
		exit(0)
	num = str(res) + x
	res = eval(num)
	print(res,end='')
