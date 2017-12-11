#!/usr/bin/python

# For time delays and sleeping
import time

# Separate scripts
from radIoT_googleCal import getCalPosts
from radIoT_LCD import initLCD
#import radIoT_spotify

global lcd

def main():
    lcd = initLCD()
    lcd.set_backlight(0)
    lcd.message('Welcome!')

    lcd.clear()
    lcd.message('Getting Google\nCalendar info...')
    events = getCalPosts()
    lcd.clear()
    lcd.message('Done!')
    time.sleep(1)
    # Check if anything was received:
    if not events:
        # clear LCD, and write that nothing was found.
        lcd.clear()
        lcd.message('Nothing found...')
    for event in events:
        # Print out the start of the event:
        start = event['start'].get('dateTime', event['start'].get('date')).encode('ascii','replace')
        title = event['summary'].encode('ascii','replace')
        # Clear LCD, and print the time and title of the events gotten:
        lcd.clear()
        lcd.message(start + '\n' + title)
        time.sleep(1)

if __name__ == '__main__':
    main()
