# Import Spotify API
import spotify # Imports Spotify methods.
import threading # Imports Threading methods.

# Initialize Spotify session, and sinks for audio.
logged_in_event = threading.Event() # Tracks when the user is logged in.
session = spotify.Session() # Spotify Session object.
audio = spotify.AlsaSink(session) # Audio object for output - sinks to alsa.
loop = spotify.EventLoop(session) # Event loop for the session.

# A login state tracker thread.
def spotifyConnectionState(session):
    if session.connection.state is spotify.ConnectionState.LOGGED_IN:
	logged_in_event.set()	

# Logs into Spotify
def spotifyLogIn():
    loop.start() # Starts the spotify session loop.
    session.on(
	spotify.SessionEvent.CONNECTION_STATE_UPDATED,
	connection_state_listener)
    session.login('1217631550', 's3cretpassword')
    logged_in_event.wait()

# Plays random Spotify songs from playlist. Query format = u'Discover Weekly'
def spotifyPlayRandom(playlistQuery):
    # Load the playlist from search query.
    playlist = spotify.search(session, query=playlistQuery).load(timeout=60) # Search with timeout of 60s.
    tracks = playlist.tracks()
    playlist.load(60) # Timeout the loading in 60s.
    playTrack = random.randint(1,len(tracks)) # Randomly pick the track to be played.

    # Play the specific Track:
    track = session.get_track(playTrack)
    track.load()
    session.player.load(track)
    session.player.play()