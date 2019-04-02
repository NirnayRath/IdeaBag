# This will ask you to enter a dictinary of numbers and then give out the number on the position u ask for..
from collections import OrderedDict
a=int(input("Enter the ending of the range 1st:"))
def funct(a):
    pudding=OrderedDict()
    for i in range(1,a+1):
        pudding[i]=int(input("Enter input: "))

    n=int(input("Enter the position of the no.:"))
    if n in pudding.keys():
        print("The no. on that position is ",pudding[n])
        print(str(pudding[n-1])+str(pudding[n]))



funct(a)