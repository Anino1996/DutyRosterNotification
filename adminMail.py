import smtplib

def adminAlert(recipient,excptn):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.ehlo()

	server.login("oforiaalbert@gmail.com","Pythonist@96")
	message=f"From: 933 Oaklawn Avenue B\r\nTo:anino1996.ao@gmail.com\r\nSubject: Failed to send message\r\n\r\n Hello Admin,\nReminder to {recipient.name} failed.\n Exception raised: {excptn}\n\n"
	server.sendmail("oforiaalbert@gmail.com","anino1996.ao@gmail.com",message)
	server.close()