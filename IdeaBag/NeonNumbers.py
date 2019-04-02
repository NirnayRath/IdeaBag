#Enter a renge and the program will print all the Neon numbers in the range..
#Neon no.:when the sum of the digits of the of the square of a no. is equal to the no. itself..
import math
i=int(input('Enter 1st no.'))
def neon(i):
    for i in range(i,1+int(input("2nd no."))):
        j=pow(i,2);
        #print(j)
        b=j;
        a = 0;
        while (int(j)!=0):
            b=int(j)%10;
            a=a+b;
            j=j/10;
            #print (a)
        if (i==a):
            print (i," is a neon no.")
        else:
            print (i," is not a neon no.")

neon(i)