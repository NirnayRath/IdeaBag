per=6.5;
value=0;
w=int(input("Enter 1 for mortage calc. and 2 for changing interest rate: "));

if (w==1):
     def mortage(value):
          value=float(input("Enter the value of your mortage: "));
          t_mort=1;
          while(t_mort>0):
               intrst=value*per/100;
               t_mort=value+intrst;
               m_mort=t_mort/36;
               print ("Pay Rs. ",m_mort," this month");
               input("Press Enter");
               value=value-m_mort;
          return;

elif (w==2):
     def change(per):
          per=float(input("Enter the rate of interest: "));
          input("Are You Sure to save the changes??");



else:
     print ("Enter a valid input");


mortage(value)
change(per)
