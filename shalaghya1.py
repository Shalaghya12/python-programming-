from easygui import *
import sys

while 1:
        msgbox("Welcome to ebazar")

	msg ="What would u like to buy?"
	title = "ebazar"
	choices = ["electronics", "mobiles", "fashion", "home"]
	choice = choicebox(msg, title, choices) 
	msgbox("You chose: " + str(choice), "Survey Result")
	if choice=="electronics":
		choices1=["applicaces"]
		choice1=choicebox(msg,title,choices1)
		msgbox("You choose" +str(choice1), "result")
	elif choice1=="mobiles":
		choices2=["vendor 1=$2"]
		choice2=choicebox(msg,title,choice2)
		msgbox("you choose" +str(choice2),"result")
	msg = "Do you want to continue?"
	title = "Please Confirm"
	if ccbox(msg, title):     
   	 pass  
	else:
   	 sys.exit(0)
