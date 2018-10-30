from easygui import *
import sys
sum=0
while 1:
    msgbox("Welcome to Amazon")

    msg ="What is your requirement?"
    title = "Amazon"
    choices = ["Mobiles", "T-shirts", "Shoes", "Watches"]
    choice = choicebox(msg, title, choices)
    #msgbox("You chose: " + str(choice))

   
    if choice=="Watches":
        msg1="Which Brand you choose"
        title1="Brands"
        choices1=["Fossil","Armani","Rado"]
        choice1 = choicebox(msg1,title1,choices1)
        if choice1 =="Rado":
                  m1="Best Prices are"
                  t1="Vendors"
                  cs1=["A-Rs.2000","B-Rs.2500"]
                  c1=boolbox(m1,t1,cs1)
                  if choice==1:
                       sum=sum+2500
                  elif choice==0:
                       sum=sum+2000

        elif choice1 =="Armani":
                  m1="Price is Rs.10000"
                  sum=sum+10000             
        elif choice1=="Fossil":
                  m1="Price is Rs.8000"
                  sum=sum+8000


    elif choice=="Shoes":
        msg2="Which Brand you choose"
        title2="Brands"
        choices2=["Nike","Puma","Adidas"]
        choice2 = choicebox(msg2,title2,choices2)
        if choice2 =="Nike":
                  m2="Price is Rs.5000"
                  sum=sum+5000
        elif choice2 =="Puma":
                  m2="Price is Rs.3500"
                  sum=sum+3500             
        elif choice2=="Adidas":
                  m2="Price is Rs.8000"
                  sum=sum+8000

    elif choice=="Mobiles":
         msg3="Which Brand you choose"
         title3="Brands"
         choices3=["Apple","Samsung","LG"]
         choice3 = choicebox(msg3,title3,choices3)
         if choice3 =="Apple":
                  m3="Price is Rs.111000"
                  sum=sum+111000
         elif choice3 =="Samsung":
                  m3="Price is Rs.19000"
                  sum=sum+19000             
         elif choice3=="LG":
                  m3="Price is Rs.18000"
                  sum=sum+18000 
    
    elif choice=="T-shirts":
         msg4="Which Brand you choose"
         title4="Brands"
         choices4=["levis","LP","U.S Polo"]
         choice4 = choicebox(msg4,title4,choices4)
         if choice4 =="Levis":
                  m4="Price is Rs.1700"
                  sum=sum+700
         elif choice4 =="LP":
                  m4="Price is Rs.1550"
                  sum=sum+1550             
         elif choice4=="U.S Polo":
                  m4="Price is Rs.1100"
                  sum=sum+1100 
    

    msg = "Do you want to shop more?"
    title = "Please Confirm"
    if ccbox(msg, title):         
       pass                    
    else:
         textbox(msg="bill",title="bill",text=str(sum))
         sys.exit(0)
