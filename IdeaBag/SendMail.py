#This sends emails to any to address..

import smtplib
fromaddr='nirnayrath1998@gmail.com'
toaddr='spruhapadhi@gmail.com'
mssg='Hi spruha!'
username='nirnayrath1998@gmail.com'
password='canigomad'
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,mssg)
server.quit()