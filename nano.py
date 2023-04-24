import RPi.GPIO as GPIO
import time
import socket

# for 1st Motor on ENA
ENA = 33
IN1 = 35
IN2 = 36
IN3 = 37
IN4 = 38
ENB = 32

# Create socket
s = socket.socket()

# Define port
port = 12345

# Connect to server
s.connect(("192.168.1.83", port))

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)


def setup_motor():
    # initialize EnA, In1 and In2
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)


def stop(seconds=1):
    # Stop
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(seconds)


def forward(seconds=1):
    # Forward
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(seconds)


def backward(seconds=1):
    # Backward
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(seconds)


def left(seconds=1):
    # Left
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(seconds)


def right(seconds=1):
    # Right
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(seconds)


# set up the motor
setup_motor()

while True:
    # read the data received
    data = s.recv(1).decode()
    print(data)
    # check where you must move
    if data == "u":
        forward(1)
    if data == "d":
        backward(1)
    if data == "l":
        left(1)
    if data == "r":
        right(1)
    if data == "s":
        stop(1)

GPIO.cleanup()
