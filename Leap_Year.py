r=int(input("enter the leap year"))
if(r%4==0):
	if(r%100==0):
		if(r%400==0):
			print("year is leap year")
		else:
			print("year is not leap year")
	else:
		print("year is not leap year")
else:
	print("year is not leap year")
