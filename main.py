import sqlite3
#import csv
import Member
from datetime import date, timedelta
import os

def main():
	os.chdir('/home/pi/Documents/email_app')

	con=sqlite3.connect('House_members.db')

	curr=con.cursor()

	curr.execute('SELECT name, email FROM Members')

	data=curr.fetchall()

	members=[Member.houseMember(*info) for info in data]
	
	curr.close()

	capacity=len(members)

	start_date=date(2021,1,2)

	next_scrub=date.today()+timedelta(days=(5-date.today().weekday())%7)

	in_charge=members[int((next_scrub-start_date).days/7)%capacity]

	in_charge.alert()

	
if __name__=='__main__':
	main()
