#!/usr/bin/python

# For time delays and sleeping
import time

# For FSM
from fysom import Fysom

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

def main():
    while True:
        if fsm.isstate('start')
            print(fsm.current)
            time.sleep(1)
            fsm.showWelcome()
        
        elif fsm.isstate('welcome')
            print(fsm.current)
            time.sleep(1)
            fsm.showMenu()
            
        elif fsm.isstate('menu')
            print(fsm.current)
            time.sleep(1)
            fsm.alarmTrigger()

        elif fsm.isstate('calendarAPI')
            print(fsm.current)
            time.sleep(1)
            fsm.showMenu()
        
        elif fsm.isstate('weatherAPI')
            print(fsm.current)
            time.sleep(1)
            fsm.showMenu()
        
        elif fsm.isstate('startSong')
            print(fsm.current)
            time.sleep(1)
            fsm.showMenu()
    
if __name__ == '__main__':
    main()