def ArmN(x):
	sum=0			   	#Sum initilized to zero
	a=x				#Value given to a variable			
	while (a>0):			#while loop is used to check the condition
		d=a%10			#modulus taken of the no,
		sum+=d**3		#sum is sum+cube of no
		a=a//10			#then again it is divided to get the quotient
	if sum==x:
		return 'Armstrong no'
	else:
		return 'not armstrong no'
x=int(input("enter the no"))
print(ArmN(x))		
