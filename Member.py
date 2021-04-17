import smtplib
import datetime
import os
import json
from dotenv import load_dotenv

#Load email credentials safely
load_dotenv('.env')
creds = json.loads(os.getenv('DUTY_ROSTER_LOGIN'))


####################################################
# Define  house member class to handle all methods # 
# and attributes of house members				   #
####################################################

class houseMember:

	
	
	# Constructor takes in the full name and email of the house member
	def __init__(self, name, email):
		self.name=name
		self.email=email
		self.nickname=name.split()[0]
		

	def __repr__(self):
		return self.nickname

	

	# Alert the admin when a message fails
	@staticmethod
	def adminAlert(recipient,excptn):

		server=smtplib.SMTP("smtp.gmail.com",587)
		server.starttls()
		server.ehlo()

		server.login(creds.get('mail'),creds.get('pwrd'))
		message=f"From: 933 Oaklawn Avenue B\r\nTo:{creds.get('mail')}\r\nSubject: Failed to send message\r\n\r\n Hello Admin,\nReminder to {recipient.name} failed.\n Exception raised: {excptn}\n\n"
		server.sendmail(creds.get('mail'),"anino1996.ao@gmail.com",message)
		server.close()


	# Manual logging of alert status
	def _log(self, data):

		# Save old log data
		log_file_name = 'emaillogs.log'
		old_logs = ''
		if log_file_name in os.listdir():
			with open(log_file_name,'r') as file:
				old_logs = file.read()


		# Write feedback on top of old data to log file
		with open(log_file_name,'w') as file:
				file.write(f'{datetime.datetime.now()} - {data} - {self.nickname}\n{old_logs}')



	def alert(self):
		
		# Connect to gmail server, log in and send message to house member
		try:

			server=smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			server.ehlo()

			server.login(creds.get('mail'),creds.get('pwrd'))
			message=f"From: 933 Oaklawn Avenue B\r\nTo:{self.email}\r\nSubject: Clean-up reminder\r\n\r\n Hello {self.nickname},\n\n This is just a kind reminder that tomorrow is your clean-up day.\n Thank you for helping keep the house tidy.\n\n For more information, please visit https://fierce-reaches-38495.herokuapp.com.\n\n Have a great evening!" 
			server.sendmail(creds.get('mail'), self.email, message)
			server.close()

			fdbck = 'Success'

		
		#Alert the admin if send process fails
		except Exception as e:
			fdbck = f"Failed with exception {e}"
			houseMember.adminAlert(self,e)


		# Log the feedback
		self._log(fdbck)

