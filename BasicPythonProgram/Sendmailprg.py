
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 465)
server.ehlo()
server.starttls()
server.login("varnmd211", "Bandodkar@Jun2017")
 
msg = "Python Automation....."
checkfun=server.sendmail("varmad211@gmail.com", "varmad211@gmail.com", msg)

server.quit()