#! /bin/bash

# Check if running on local machine of raspberry Pi (Tested on laptop before being deployed on Pi)
appdir=/home/pi/Documents/email_app;
if [ "$USER" == "anino1996" ]; then
	echo "Running on Anino's Mac";
	appdir=~/Python/Duty_Roster/DutyRosterNotification;
	pwd;

else
	echo "Running on Anino's Pi";
	appdir=/home/pi/Documents/email_app;
fi;

cd $appdir;

# Create virtual environment if it doesn't exist
if [ ! -d $appdir/mailenv ]; then
	echo "Creating virtual environment...";
	virtualenv -q -p $(which python3) $appdir/mailenv;
	echo "Virtual environment created.";

else 
	echo "Virtual environment already exists.";
fi;

# Activate virtual environment
source $appdir/mailenv/bin/activate;
if grep -q "$(pwd)" <<< "$(which python3)"; then
	echo "Virtual environment activated."
fi;

# Install required dependencies if they do not already exist
if ! grep -q "dotenv" <<< "$(pip freeze)"; then
	echo "Installing dependencies..."; 
	pip3 -q install python-dotenv;
	echo "Dependencies installed.";
fi;

# Run application
python3 $appdir/main.py;

#Deactivate virtual environment
deactivate;

echo "All Done!";
