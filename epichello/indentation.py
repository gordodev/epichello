#!/usr/bin/env python

import time
import logging

print ("Welcome to Indentation Land!")
print ("")
print ("Hello World")

logging.basicConfig(filename='myFirstLog.log',level=logging.DEBUG)

logging.info('While loop begining')
while True: 
	print ("what are you up to")
	print ("")
	time.sleep(0.8)
print " "

