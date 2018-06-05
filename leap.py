y=int(input("enter the value"))
if(y%4==0):
	if(y%100==0):
		if(y%400==0):
			print("\ny is leap year")
		else:
			print("\ny is not leap year")
	else:
		print("\ny is leap year")
else:
	print("\ny is not leap year")
