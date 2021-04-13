import smtplib
import datetime
import os
from adminMail import adminAlert

class houseMember:
	def __init__(self, name, email):
		self.name=name
		self.email=email
		self.nickname=name.split()[0]

	def __repr__(self):
		return self.nickname

	def alert(self):
		old_logs=''

		if 'emaillogs.txt' in os.listdir():
			with open('emaillogs.txt','r') as file:
				old_logs=file.read()

		try:

			server=smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			server.ehlo()

			server.login("oforiaalbert@gmail.com","Pythonist@96")
			message=f"From: 933 Oaklawn Avenue B\r\nTo:{self.email}\r\nSubject: Clean-up reminder\r\n\r\n Hello {self.nickname},\n\n This is just a kind reminder that tomorrow is your clean-up day.\n Thank you for helping keep the house tidy.\n\n For more information, please visit https://fierce-reaches-38495.herokuapp.com.\n\n Have a great evening!" 
			server.sendmail("oforiaalbert@gmail.com",self.email,message)
			server.close()

			with open('emaillogs.txt','w') as file:
				file.write(f'{datetime.datetime.now()} - Success - {self.nickname}\n{old_logs}')
		
		except Exception as e:
			with open('emaillogs.txt','w') as file:
				file.write(f'{datetime.datetime.now()} - Failed with exception: {e} \n{old_logs}')
			adminAlert(self,e)

