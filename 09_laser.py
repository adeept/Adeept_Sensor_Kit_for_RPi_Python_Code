#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LaserPin = 11    # pin11

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)         # Numbers pins by physical location
	GPIO.setup(LaserPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LaserPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the laser

def loop():
	while True:
		GPIO.output(LaserPin, GPIO.LOW)  # led on
		print '...OFF'
		time.sleep(0.5)

		GPIO.output(LaserPin, GPIO.HIGH) # led off
		print 'ON...'
		time.sleep(0.5)

def destroy():
	GPIO.output(LaserPin, GPIO.HIGH)   # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


