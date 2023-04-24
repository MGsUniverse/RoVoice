from voice_recognizer import *
import speech_recognition as sr
import socket

recognizer = sr.Recognizer()
microphone = sr.Microphone()

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))

# put the socket into listening mode
s.listen(1)

c, addr = s.accept()
print("Connected")

while True:
    text = recognize_speech_from_mic(recognizer, microphone)['transcription']
    print(text)
    if text == "forward":
        c.send("u".encode())
    if text == "back":
        c.send("d".encode())
    if text == "left":
        c.send("l".encode())
    if text == "right":
        c.send("r".encode())

