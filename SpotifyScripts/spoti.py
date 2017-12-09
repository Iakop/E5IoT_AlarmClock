#!/usr/bin/python

import spotify # Imports Spotify methods.
import threading # Imports Threading methods.
logged_in_event = threading.Event() # Tracks when the user is logged in.

# A login state tracker thread.
def connection_state_listener(session):
	if session.connection.state is spotify.ConnectionState.LOGGED_IN:
		logged_in_event.set()
	
session = spotify.Session() # Spotify Session object.
audio = spotify.AlsaSink(session) # Audio object for output - sinks to alsa.
loop = spotify.EventLoop(session) # Event loop for the session.
loop.start() # Starts the spotify session loop.

session.on(
	spotify.SessionEvent.CONNECTION_STATE_UPDATED,
	connection_state_listener)
	
session.connection.state
session.login('1217631550', 's3cretpassword')
session.connection.state
logged_in_event.wait()
session.connection.state
session.user

track = session.get_track('spotify:track:3N2UhXZI4Gf64Ku3cCjz2g')
track.load()
session.player.load(track)
session.player.play()