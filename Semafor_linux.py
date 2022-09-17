#!/usr/bin/env python3

#variable initialization
delay = int(1)
led_1 = str("[GREEN][BLUE]")
led_2 = str("[WHITE][RED]")


#import libraris
import time
import os


#start up
os.system("clear")
print("Thanks for download! -- Atlas11x")
time.sleep(delay * 2)
os.system("clear")

#main code (loop)
while True:
	print(led_1)
	time.sleep(delay)
	os.system("clear")
	print(led_2)
	time.sleep(delay)
	os.system("clear")
