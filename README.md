# E5IoT_AlarmClock
E5IOT course project to create a smart alarmclock, that awakens the user with music and info such as weather.

## Project Description
The goal of the project is to solve the following problems:
- How can you be woken up in a comfortable manner?
- How will you be woken up in time?
- What else can help in the morning routine?

## Solution
This alarm clock project will solve the problems in the project description, by waking up the user to the tune of their favorite music, or new music suited to their tastes. The way this is achieved is through the use of Spotify's API, as well as the application itself. For this reason a multimedia-freindly platform is required, which is why a Raspberry Pi Zero W has been picked at the platform of choice.
Through data gathered from Google Calendar, the alarm clock will know the morning schedule for each day. And wake up the user accordingly. In case of a missing internet connection or data, the system could work to awaken the user at a preset "safe" time, or simply from the last collected calendar data.
To make the morning routine easier for the user, a display of some sort can be utilized, to show the relevant information, such as weather, historical stock data, sleep data and so on. In addition to this, the system must be controllable through either voice commands or a button interface. If the voice commands are to be implemented, Google Assistant API should be very helpful.

## Minimum requirements:
- Multimedia enabled Raspberry Pi Zero W
	- Has a Spotify installation
	- Can store and play songs from the users library
- Speaker interface
	- First implementation can be through PWM generated Audio
	- Class D amplifier output
- Display interface
	- Will be easiest through a TFT screen
	- Requires Qt graphics.
- Button interface
	- Prototyping with keyboard commands okay
- Google Calendar integration
	- Pi Zero W can get personalized calendar data
- Weather information
	- Display an icon indicating weather

## Optional requirements:
- Google Assistant
	- Voice activated commands require a microphone
- Microphone extension
	- Raspberry Pi Hat, or ADC electret mic
	- Hat is better for prototyping

## To-Do list:
1. - DONE! - Flash a Raspbian Stretch Lite Image onto SD card for booting.
2. Try Spotify installation - Does it work without a GUI?
3. Get PWM Audio output - Lowpassfilter it. Use a Class D amp to amplify.
4. Get access to the Particle IoT environment from Rpi Zero W.
5. Play around with the Spotify API. What can be obtained from it? Is it useful for the project. - Or will another solution be needed?
6. Implement the Alarm Clock feature. - Can be a polling shell script or similar. A Daemon, if there's time.
7. Add a Display to the setup, along with menu buttons. An LCD should be enough for now.
8. Access a Weather Station API through Particle somehow. This will be displayed on the LCD.
9. Figure out a way to take microphone input. USB mic should do the trick?
10. Make Google Assistant available to the Rpi. Google AIY should have some resources for this.
8. 