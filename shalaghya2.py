from easygui import *
import sys

while 1:
	msgbox("Welcome to ebazar")
	msg ="What would u like to buy?"
	title = "ebazar"
	choices = ["electronics", "Grocery", "fashion", "appliances","home"]
	choice = choicebox(msg, title, choices) 
	msgbox("You chose: " + str(choice), "Survey Result")
	if choice=="electronics":
		choices1=["TV","Mobile","fridge","washing machine"]
		choice1=choicebox(msg,title,choices1)
		msgbox("You choose" +str(choice1), "result")
                if choice1=="TV":
			choices2=["sony","lg","samsung"]
			choice2=choicebox(msg,title,choices2)
			msgbox("You choose" +str(choice2), "result")
		elif choice1=="Mobile":
			choices3=["apple","samsung","nokia"]
			choice3=choicebox(msg,title,choices3)
			msgbox("You choose" +str(choice3), "result")
		elif choice1=="fridge":
			choices3=["samsung","lg"]
			choice3=choicebox(msg,title,choices3)
			msgbox("You choose" +str(choice3), "result")
		elif choice1=="washing machine":
			choices4=["samsung","lg","onida"]
			choice4=choicebox(msg,title,choices4)
			msgbox("You choose" +str(choice4), "result")    		
	elif choice=="Grocery":
		choices5=["cooking","household essintials"]
		choice5=choicebox(msg,title,choice5)
		msgbox("you choose" +str(choice5),"result")
		
	elif choice=="fashion":
		choices6=["Mens wear","shoes","Womens wear"]
		choice6=choicebox(msg,title,choices6)
		msgbox("You choose" +str(choice6), "result")
		if choices6=="Mens wear":
			choices7=["supreme T-shirt=$100","Louis Vitton shirt=$300","CK trousers=$300"]
			choice7=choicebox(msg,title,choices7)
			msgbox("You choose" +str(choice7), "result")
		elif choices6=="shoes":
			choices8=["Air Jordans=$800"]
			choice8=choicebox(msg,title,choices8)
			msgbox("You choose" +str(choice8), "result")
		elif choices6=="Womens wear":
			choices9=["saree=$10","dress=$10"]
			choice9=choicebox(msg,title,choices9)
			msgbox("You choose" +str(choice9), "result")
	
		
			
	msg = "Do you want to continue?"
	title = "Please Confirm"
	if ccbox(msg, title):     
   	 pass  
	else:
	 sys.exit(0)
