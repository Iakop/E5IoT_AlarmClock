#!/usr/bin/python

# For time delays and sleeping
import time
import datetime

# For Audio
import pyaudio
import wave

# For file system
import sys

# For FSM
from fysom import Fysom

# Separate scripts
from radIoT_googleCal import getCalPosts
from radIoT_LCD import initLCD
#import radIoT_spotify

global fsm
fsm = Fysom({
  'initial': 'start',
  'events': [
    {'name': 'showWelcome', 'src': 'start', 'dst': 'welcome'},
    {'name': 'showMenu', 'src': ['welcome','songStart','weatherAPI','calendarAPI'], 'dst': 'menu'},
    {'name': 'alarmTrigger', 'src': 'menu', 'dst': 'startSong'},
    {'name': 'alarmTrigger', 'src': 'startSong', 'dst': 'weatherAPI'},
    {'name': 'getCalendar', 'src': 'menu', 'dst': 'calendarAPI'},
    {'name': 'getWeather', 'src': 'menu', 'dst': 'weatherAPI'},
    {'name': 'getSong', 'src': 'menu', 'dst': 'startSong'},
    {'name': 'getCalendar', 'src': 'voiceAPI', 'dst': 'calendarAPI'},
    {'name': 'getWeather', 'src': 'voiceAPI', 'dst': 'weatherAPI'},
    {'name': 'getSong', 'src': 'voiceAPI', 'dst': 'startSong'}
  ]
})

SOUNDS_PATH = '/media/certs_n_sounds/sounds/'

global lcd
global events
global wf
wf = wave.open(SOUNDS_PATH + 'Daytona_USA_Theme.wav', 'rb')

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True,
    stream_callback=callback)

def main():
    lcd = initLCD()
    
    while True:
        if fsm.isstate('start')
            fsm.showWelcome()
        
        elif fsm.isstate('welcome')
            lcd.set_backlight(0)
            lcd.message('Welcome!')
            time.sleep(1)
            fsm.showMenu()
            
        elif fsm.isstate('menu')
            fsm.getCalendar()

        elif fsm.isstate('calendarAPI')
            lcd.clear()
            lcd.message('Getting Google\nCalendar info...')
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
            lcd.clear()
            lcd.message('Done!')
            time.sleep(1)
            fsm.showMenu()
        
        elif fsm.isstate('weatherAPI')
            fsm.showMenu()
        
        elif fsm.isstate('startSong')
            wf = wave.open(SOUNDS_PATH + 'Daytona_USA_Theme.wav', 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
            stream.start_stream()
            fsm.showMenu()
    
if __name__ == '__main__':
    main()
