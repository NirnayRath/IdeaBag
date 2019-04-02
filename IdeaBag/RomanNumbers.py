#This is a program to display the Roman Numerals..
# Input an integer to display its roman equivalent..
i=int(input("Enter an Integer: "))
from collections import OrderedDict
def Roman(i):
    roman=OrderedDict()
    roman[1000]="M"
    roman[900]="CM"
    roman[500]="D"
    roman[400]="CD"
    roman[100]="C"
    roman[90]="XC"
    roman[50]="L"
    roman[40]="XL"
    roman[10]="X"
    roman[9]="IX"
    roman[5]="V"
    roman[4]="IV"
    roman[1]="I"

    def nume(i):
        for r in roman.keys():
            x,y=divmod(i,r)
            yield roman[r]*x
            i-=(r*x)
            if i>0:
                nume(i)
            else:
                break
    print("".join([a for a in nume(i)]))

Roman(i)
