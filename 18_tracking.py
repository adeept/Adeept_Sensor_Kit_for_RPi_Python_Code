#!/usr/bin/env python
import RPi.GPIO as GPIO

TrackSensorPin_S = 11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(TrackSensorPin_S, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set Pin's mode is input, and pull up to high level(3.3V)

def loop():
	while True:
		if GPIO.input(TrackSensorPin_S) == GPIO.LOW:
			print '...White line is detected !'
		else:
			print 'Black line is detected...'

def destroy():
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

