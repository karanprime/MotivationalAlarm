# MotivationalAlarm
Disclaimer: Though I think it will work 100% of the time, please don't use it as your main alarm yet. I am not responsible if you miss your assignment/flight/solar eclipse.

Wake up pumped up with your computer waking up before you, setting volume and brightness to max and playing a motivational video full screen.

Note: If using on a laptop, it is recommended you keep the charger plugged in. Also, don't close the lid unless connected to an external display.

1. Open your browser (new tab is fine)
2. Open the terminal
3. Go to the script directory
4. Run the script by running it in terminal using "python web.py".
  * Enter hour (Millitary time)
  * Enter minute (Millitary time)
  * Enter your password (Note: It echoes now, will implement a hidden password field using getpass later)

5. It will say "Alarm set for time and date"
6. A settings pane will open. 
  * Uncheck "Require password on wake up" box if you have a wake up password. 
  * Click on Turn off password and then Keep using Keychain in the dialog boxes that appear.
7. Close the settings pane.

Your computer will sleep in about 30 seconds.

* It will wake up a few seconds before the set alarm.
* It will override your volume settings to 10 (full).
* It will play a motivational video . (You can pick one using the vid variable where vid is the youtube video id)

8. After waking up, the settings pane will open again. To again lock your computer on sleep, just tick the "Require password on wake up" box. 

To add:
Spotify playlists
Hidden passwords

Bugs:
Won't work if alarm is set upto 3 minutes in the future.

