# This is Fizz Buzz fun game..
r1=int(input("Enter 1st no. of range: "))
r2=int(input("Enter 2st no. of range: "))

def FizzBuzz(r1,r2):
    for i in range(r1,r2+1):
        if i%3==0:
            if i%5==0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%5==0:
            print ("Buzz")
        else:
            print(i)


FizzBuzz(r1,r2)