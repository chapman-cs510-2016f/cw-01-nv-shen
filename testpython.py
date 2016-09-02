import random


def main():
	scores = random.randint(0,100)
	
	if 100 >= scores >= 90:
		print('A')
	elif 90 > scores >= 80:
		print('B')
	elif 80 > scores >=60:
		print('C')
	else:
		print('D')

main()
