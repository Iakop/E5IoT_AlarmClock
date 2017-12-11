#!/usr/bin/python

import radIoT_googleCal
import radIoT_LCD
#import radIoT_spotify

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
        start = event['start'].get('dateTime', event['start'].get('date')).encode('ascii','replace')
        title = event['summary'].encode('ascii','replace')
        # Clear LCD, and print the time and title of the events gotten:
        lcd.clear()
        lcd.message(start + '\n' + title)
        time.sleep(1)
        
if __name__ == '__main__':
    main()