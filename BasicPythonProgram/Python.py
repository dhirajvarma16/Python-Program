import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 503)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('varmad211@gmail.com', 'Bandodkar@Jun2017')
smtpserver.quit()