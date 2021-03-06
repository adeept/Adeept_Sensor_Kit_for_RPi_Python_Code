#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

MotorPin_A  = 11
MotorPin_B  = 12

def motorStop():
	GPIO.output(MotorPin_A, GPIO.HIGH)
	GPIO.output(MotorPin_B, GPIO.HIGH)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(MotorPin_A, GPIO.OUT)
	GPIO.setup(MotorPin_B, GPIO.OUT)
	motorStop()

def motor(status, direction):
	if status == 0: # stop
		motorStop()
	else:
		if direction == 1:
			GPIO.output(MotorPin_A, GPIO.HIGH)
			GPIO.output(MotorPin_B, GPIO.LOW)
		else:
			GPIO.output(MotorPin_A, GPIO.LOW)
			GPIO.output(MotorPin_B, GPIO.HIGH)

def loop():
	while True:
		motor(1, 1)
		time.sleep(5)
		motor(0, 0) # stop
		time.sleep(5)
		motor(1, 0)
		time.sleep(5)
		motor(0, 0) # stop
		time.sleep(5)

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

