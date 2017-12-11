#!/usr/bin/python

# For the Google Calendar API
from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools # Tools to work operations for Oauth2.
from oauth2client.file import Storage # Method to store Oauth2 credentials.
import datetime
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# For time delays, and sleeping
import time

# For driving an LCD to display results.
import Adafruit_CharLCD as LCD

# Raspberry Pi LCD pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 27
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
lcd.show_cursor(False)
lcd.clear()

# Setup client secrets and Application Name for Calendar.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_PATH = '/media/certs_n_sounds/certs/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'radIoT Alarm Clock'

def getCalCredentials():
    home_dir = os.path.expanduser('~') # Sets the home directory to the user home directory.
    credential_dir = os.path.join(home_dir, '.credentials') # Appends the credentials directory to the user directory.
	# Checks if the path exists. If not, os method creates the dir.
    if not os.path.exists(credential_dir):
    	os.makedirs(credential_dir)
	# Adds the file to the credential path.
    credential_path = os.path.join(credential_dir,
                                   'radIoT_Alarm_Clock.json')

    store = Storage(credential_path) # Stores secret in the path.
    credentials = store.get() # Retrieve credentials.
	# If no credentials are found, or they are invalid:
    if not credentials or credentials.invalid:
		# Create the credentials from the Client Secret File. 
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_PATH + CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
		# Depending on the import of the argparse:
        if flags:
            credentials = tools.run_flow(flow, store, flags) # Store the credentials.
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getCalPosts():
    credentials = getCalCredentials() # Gets the credentials if they exist.
    http = credentials.authorize(httplib2.Http()) # Authorizes the credentials using httplib2.
    service = discovery.build('calendar', 'v3', http=http) # Defines the service, that provides the calendar dates.

    # Get the upcoming calendar dates for the next 10 days:
    # Define "now".
    now = datetime.datetime.utcnow()
    span = datetime.timedelta(days=10)
    end = now + span
    end = end.isoformat() + 'Z'
    now = now.isoformat() + 'Z'
    # Write out to LCD:
    lcd.clear()
    lcd.message('Getting Calendar')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, timeMax=end, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    lcd.clear()
    lcd.message('Done :)')
    time.sleep(1)
    return events

def main():
    lcd.set_backlight(0)
    events = getCalPosts()
    # Check if anything was received:
    if not events:
        # clear LCD, and write that nothing was found.
        lcd.clear()
        lcd.message('Nothing found...')
    for event in events:
        # Print out the start of the event:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(type(start))
        # Clear LCD, and print events, and their start time.
        lcdout = event['summary'].encode('ascii','replace')
        lcd.clear()
        lcd.message('Got event:\n' + lcdout)
        time.sleep(1)
        
if __name__ == '__main__':
    main()
