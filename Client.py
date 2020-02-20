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

serverAddress="192.168.1.3"    # Put your Phone IP here
serverPort=2021
bufferSize=12

serialConnection = serial.Serial('/dev/ttyACM0',9600)   # Change this to COMx if you are on Windows, COMx is the port where Arduino serial is connected
print("Serial connection established on {name}".format(name=serialConnection.name))

socketSendCommands = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketSendCommands.connect((serverAddress,serverPort))

nPhotos=input("How many photos to take?")

for i in range(nPhotos+1):
    time.sleep(3)
    socketSendCommands.send("chez".encode())
    serialConnection.write("go\n".encode())

time.sleep(1)
serialConnection.close()
socketSendCommands.send("quit".encode())
socketSendCommands.close()
