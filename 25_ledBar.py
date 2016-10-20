#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

DATA_Pin = 16
CLK_Pin  = 18
  
CmdMode  = 0x0000  # Work on 8-bit mode
ON       = 0x00ff  # 8-bit 1 data
SHUT     = 0x0000  # 8-bit 0 data
 
global s_clk_flag

def send16bitData(data):
	global s_clk_flag
	for i in range(16):
		if data & 0x8000 == True:
			GPIO.output(DATA_Pin, GPIO.HIGH)
		else:
			GPIO.output(DATA_Pin, GPIO.LOW)
  
		if s_clk_flag == True:
			GPIO.output(CLK_Pin, GPIO.LOW)
			s_clk_flag = 0
		else:
			GPIO.output(CLK_Pin, GPIO.HIGH)
			s_clk_flag = 1
		time.sleep(0.00001)
		data = data << 1
  
def latchData():
	latch_flag = 0
	GPIO.output(DATA_Pin, GPIO.LOW)
	time.sleep(0.0005)
	for i in range(8):
		if(latch_flag == True):
			GPIO.output(DATA_Pin, GPIO.LOW)
			latch_flag = 0
		else:
			GPIO.output(DATA_Pin, GPIO.HIGH)
			latch_flag = 1
	time.sleep(0.0005)
  
def sendLED(LEDstate):
	for i in range(12):
		if LEDstate & 0x0001 == True:
			send16bitData(ON)
		else:
			send16bitData(SHUT)
		LEDstate = LEDstate >> 1
  
def setup():
	print "LED bar test code!"
	print "Using DATA = PIN16(GPIO23), CLK = PIN18(GPIO24)"   

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(DATA_Pin, GPIO.OUT)
	GPIO.setup(CLK_Pin,  GPIO.OUT)

	GPIO.output(DATA_Pin, GPIO.LOW)
	GPIO.output(CLK_Pin,  GPIO.LOW)

	global s_clk_flag
	s_clk_flag = 0

def setLedNum(n):
	if n<0 or n >10:
		print "The range of n is [0, 10]"
		return -1;

	send16bitData(CmdMode)
	sendLED((2**n) - 1)
	#sendLED(pow(2,n)-1)
	latchData()

def loop():
	while True:
		for i in range(11):
	 		setLedNum(i)    	
			time.sleep(1)
	
def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup();
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

