# AAScan: Open source, minimalist, fully automated 3D scanner based on Arduino and Android!

# Server program - To be run on computer (I recommend LINUX)

# Copyright (C) 2020 redditNewUser2017
# Check out my page https://www.reddit.com/user/redditNewUser2017 and my subreddit https://www.reddit.com/r/Simulations/

"""     This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/agpl-3.0.en.html>. """

import serial,time
import socket

serverAddress=""    # Put your Phone IP here
serverPort=2021
bufferSize=12
nPhotos=180                      # How many photos do you want? (~180 for best quality)

serialConnection = serial.Serial('/dev/ttyACM0',9600)   # Change this to COMx if you are on Windows, COMx is the port where Arduino serial is connected
print("Serial connection established on {name}".format(name=serialConnection.name))
time.sleep(3)
serialConnection.write((str(nPhotos)+"\n").encode())
time.sleep(1)

socketSendCommands = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketSendCommands.connect((serverAddress,serverPort))

for i in range(nPhotos):
    socketSendCommands.send("chez".encode())
    serialConnection.write("go\n".encode())
    print("Progress: {count}/{total}".format(count=i+1,total=nPhotos))
    time.sleep(3)

print("DONE! The photos will be available at /qpython/tmp folder!")
time.sleep(1)
serialConnection.close()
socketSendCommands.send("quit".encode())
socketSendCommands.close()
