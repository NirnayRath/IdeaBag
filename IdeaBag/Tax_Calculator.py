salary=int(input('Enter your overall salary: '))
def stax(salary):
     calc=int(salary*16/100)
     print ("State tax is :Rs",calc)
     print ("You get Rs. ",salary-calc)
     return
def ctax(salary):
     calc=int(salary*5/100)
     print ("Country tax is :Rs",calc)
     print ("You get Rs. ",salary-calc)
     return
a=input("Enter S for State tax and C for Country tax: ")
if (a=="S"):
     stax(salary)
elif (a=="C"):
     ctax(salary)
else:
     print ("Enter a valid input")
