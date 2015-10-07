# MotivationalAlarm
Wake up pumped up with your computer waking up before you, setting volume and brightness to max and playing a motivational video full screen.

1. Open your browser (new tab is fine)
2. Open the terminal
3. Go to the script directory
4. Run the script by running it in terminal using "python web.py".
  * Enter hour (Millitary time)
  * Enter minute (Millitary time)
  * Enter your password (Note: It echoes now, will implement a hidden password field using getpass later)

5. It will say "Alarm set for time and date"
6. A settings pane will open. 
  * Uncheck require password on wake up if you have a wake up password. 
  * Click on Turn off password and then Keep using Keychain in the dialog boxes that appear.
7. Close the settings pane.

Your computer will sleep in about 30 seconds.

* It will wake up a few seconds before the set alarm.
* It will override your volume settings to 10 (full).
* It will play a motivational video . (You can pick one using the vid variable where vid is the youtube video id)

To add:
Spotify playlists
Hidden passwords

