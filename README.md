# INET4031 Add Users Script and User List
## Program Description

Automates the use of the "adduser" command to create multiple user accounts from one input file. The script reads user info line by line and fills in all the requirements automatically.

## Program User Operation

This progran reads an input file with user information and automatically inputs those accounts into the relevant files. Sudo privledges required when adding users and changing passwords.

## Input File Format
Each line of input file requires 5 fields seperated by colons.

username, 
password, 
lastname,  
firstname, 
groups - a user can be in multiple

## Command Excuction
IF NOT WORKING RUN "sudo chmod +x create-users.py".
The +x allows it be executed.
Run "sudo python3 ./create-users.py < create-users.input" to start the autonomous process.
Requires sudo privledges since we're adding users and adjusting passwords.


## "Dry Run"
COMMENT OUT ALL LINES THAT UTILIZE THE "import os" BEFORE RUNNING!!! 
If these lines are not commented out you run the risk of inputting incorrect data and then you'll need to manually remove it after this code automatically adds users... large waste of time don't ignore this.
