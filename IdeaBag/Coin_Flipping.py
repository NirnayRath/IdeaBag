import random
total=0;
tails=0;
heads=0;

while total<10:
     coin=random.randint(1,2);
     if coin==1:
          total+=1;
          heads+=1;
     if coin==2:
          total+=1;
          tails+=1;
a=input('Enter h for heads and t for tails: ')
if (a=='h'):
     print (heads);
elif (a=='t'):
     print (tails);

print (total);
