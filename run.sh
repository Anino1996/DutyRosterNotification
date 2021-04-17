#! /bin/bash

# Check if running on local machine of raspberry Pi (Tested on laptop before being deployed on Pi)
appdir=/home/pi/Documents/email_app;
if [ "$USER" == "pi" ]; then
	echo "Running on Pi";
	cd $appdir;
fi;

# Create virtual environment if it doesn't exist
if [ ! -d "mailenv" ]; then
	echo "Creating virtual environment...";
	virtualenv -q -p $(which python3) mailenv;
	echo "Virtual environment created.";

else 
	echo "Virtual environment already exists.";
fi;

# Activate virtual environment
source mailenv/bin/activate;
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
python3 main.py;

#Deactivate virtual environment
deactivate;

echo "All Done!";