#Password generator draft..

import random

name=set(str(input("Enter your name: ")))

fav_teach=set(str(input("Enter the name of your favorite teacher: ")))
pet_name=set(str(input("Enter the name of pet:")))
dob=int(input("Enter your date of birth: "))
no=set(str(dob))

total=set()
total.update(name)
total.update(fav_teach)
total.update(pet_name)
total.update(no)
Total=list(total)
Totally=list(total)
Totally.extend(map(str.upper,Total))
type=input("Type e for easy n d for difficult\n")

password=[]
def easy():
    for a in range(9):
        password.append(random.choice(Total))
def hard():
    for a in range(9):
        password.append(random.choice(Totally))
if type is 'e':
    easy()
else:
    hard()

print(''.join(password))