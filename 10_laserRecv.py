#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LaserRecvPin = 11

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LaserRecvPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set LaserRecvPin's mode as input, and pull up to high level(3.3V)

def loop():
	while True:
		if GPIO.input(LaserRecvPin) == GPIO.LOW:
			print 'Laser received...'
		else:
			print '...Laser not received'
		time.sleep(0.1)

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

