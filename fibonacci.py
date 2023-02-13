number=int(input("Enter the Value"))
first=0
second=1
print(first)
print(second)
for i in range(number-2):
	third=first+second
	print(third)
	first=second
	second=third
#if you Enter 5 produce 5 numbers in fibbonacci series
#0
#1
#1
#2
#3