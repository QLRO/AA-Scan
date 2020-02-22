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

import androidhelper
import time
import socket

droid = androidhelper.Android()
droid.wakeLockAcquireDim()

dataReceived=""
i=1
serverAddress=""    # Put your Phone IP here
serverPort=2021
bufferSize=12
photoStoragePath='/storage/emulated/0/qpython/tmp/' # You can change where the photos are stored here!

socketSendCommands = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketSendCommands.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketSendCommands.bind((serverAddress,serverPort))
socketSendCommands.listen(1)
print("Sever {ip} opened at port {port}\n".format(ip=serverAddress,port=serverPort))
(connection, address) = socketSendCommands.accept()
print("Connection established {addr}\n".format(addr=address))

try:
    while True:
        dataReceived=connection.recv(bufferSize).decode()
        if dataReceived!="":
            if dataReceived=="chez":
                path = photoStoragePath
                path += str(i)
                path += '.png'
                droid.cameraCapturePicture(path, True)
                print("{count} photos taken!".format(count=i))
                i=i+1
            if dataReceived=="quit":
                break
except:
    pass

socketSendCommands.close()
droid.wakeLockRelease()
print("DONE! The photos are stored at {path}!".format(path=photoStoragePath))
