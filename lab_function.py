def ArmN(x):
	sum=0			   
	a=x							
	while (a>0):		
		d=a%10
		sum+=d**3		
		a=a//10			
	if sum==x:
		print( 'Armstrong no')
	else:
		print( 'not armstrong no')

