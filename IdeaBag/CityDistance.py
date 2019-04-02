import math
def distance(dist):
     a1=int(input("Enter latitude 1 in km: "))
     b1=int(input("Enter longitude 1 in km:"))
     a2=int(input("Enter latitude 2 in km: "))
     b2=int(input("Enter longitude 2 in km:"))
     d=pow((a1-a2),2)+pow((b1-b2),2);
     dist=math.sqrt(d);
     q=input("Enter a unit of dist :");
     if (q=="km"):
          print (dist, "km")
     elif (q=="mtr"):
          print(dist*1000,"mtr")
     elif (q=="cm"):
          print (dist*100000,"cm")
     else:
          print ("Enter a valid unit")
     return;
distance("Letz rock n roll");
