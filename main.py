import sqlite3
import Member
from datetime import date, timedelta
import os

 
def main():

	# Connect to the House members database
	

	con=sqlite3.connect('House_members.db')

	# Initialize cursor
	curr=con.cursor()

	# Select all members from database
	curr.execute('SELECT name, email FROM Members')

	data=curr.fetchall()

	# Create a member instance for all members
	members=[Member.houseMember(*info) for info in data]
	
	curr.close()

	# Number of all members in the house
	capacity=len(members)

	# Define a hard start date for the first member based on which calculations will be made
	start_date=date(2021,1,2)

	# Calculate the next saturday from the current day
	next_scrub=date.today()+timedelta(days=(5-date.today().weekday())%7)

	# Find the number of weeks of scrub day from start date
	# Determine member in charge using modular arithmetic
	in_charge=members[int((next_scrub-start_date).days/7)%capacity]

	# Alert the member
	in_charge.alert()

	
if __name__=='__main__':
	main()
