#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

FlamePin = 15

def init():
	GPIO.setmode(GPIO.BOARD)	
	GPIO.setup(FlamePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	ADC0832.setup()

def myISR(ev=None):
	print "Flame is detected !"

def loop():
	GPIO.add_event_detect(FlamePin, GPIO.FALLING, callback=myISR)
	while True:
		res = ADC0832.getResult()
		print 'res = %d' %res
		time.sleep(0.1)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()
		print 'The end !'
