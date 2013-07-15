#!/usr/bin/python
import os
import time # For sleep timer
import sys
import zipfile # Creating the zip file
from time import gmtime, strftime # For setting the time on the zipped file

"""
@author: Justin Block
@created: July 14, 2013
@purpose: This script checks if a folder has been updated since the script has
been run. 
@usage: python fileSaver.py folderName timeInMinutesToCheck
        example parameters: python fileSaver.py folderName 60
@credits: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python for the skeleton of the zip
function.
"""

# Checks if the folder directory passed in has been updated since the last
# time the script ran
class FolderUpdater:
    def __init__(self):
        # Check that a parameter was passed in otherwise end and print out an error
        if(not sys.argv[1:]):
            sys.exit("You must pass in a folder to check. Example usage: python fileSaver.py testFolder 60")
        if(not sys.argv[2:]):
            sys.exit("You must pass in how many minutes the script should wait to check if the folder was updated. Example usage: python fileSaver.py testFolder 60")
        # If the folder doesn't exist then we stop execution
        if(not os.path.isdir(sys.argv[1])):
              sys.exit("No directory found based on the passed in directory")
        # Define the variables
        self.path = sys.argv[1] # Path to check if it has been updated
        self.timeInSeconds = int(sys.argv[2]) * 60 # Time between checks (passed in as minutes then converted to seconds for sleep function)
        self.lastUpdateTime = self.checkUpdate()
    # Checks when the folder was last updated
    def checkUpdate(self):
        return time.ctime(os.path.getmtime(self.path))
    # Checks if the folder has been updated
    def isUpdated(self):
        # Gets the current time that the file was updated on
        self.currentUpdateTime = self.checkUpdate()
        # Checks if the current time is greater (newer then the last time the script ran to check the folder update time)
        if(self.currentUpdateTime > self.lastUpdateTime):
            # If it has been updated then we want to zip the file up
            zip = zipfile.ZipFile('Backup-'+ strftime("%Y-%m-%d-%H-%M-%S", gmtime()) +'.zip', 'w') # Name of file and what to do (w) is write
            zipdir(self.path, zip) # The directory of the file to zip up
            zip.close()
            print "A backup has been made"
        else:
            print "Their have been no changes since the script last checked, note the first time the script runs it does not backup anything"

# Function from http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python user http://stackoverflow.com/users/189179/ben-james  
def zipdir(path, zip):
    for dirname, subdirs, files in os.walk(path):
            zip.write(dirname)
            for filename in files:
                zip.write(os.path.join(dirname, filename))

# Create an object of the class, and passes in the folder that this object will be checking for updates
update_check = FolderUpdater()

# Called everytime the script repeats itself
def scriptLoop():
    # Checks if the folder has been updated
    update_check.isUpdated()
    
    print "The script is now sleeping for " + str(update_check.timeInSeconds/60) + " minute(s) hit Ctrl + C on your keyboard if you wish to stop this script at any time"
    # The script now sleeps until it should go again
    time.sleep(update_check.timeInSeconds)
    # Calls itself again
    scriptLoop()

# Runs the script and then repeats to the update all the information again
scriptLoop()