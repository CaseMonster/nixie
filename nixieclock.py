#===========================================================================================
#init

import RPi.GPIO as GPIO
import time
import datetime
import os
import random

#===========================================================================================
#pin setup

GPIO.setmode(GPIO.BOARD)
PIN_SERIAL = 11
PIN_LATCH = 13
PIN_CLOCK = 12
GPIO.setup(PIN_SERIAL, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

#===========================================================================================
#definitions

#===========================================================================================
#functions

def Clock():
    time.sleep(0.25)
    GPIO.output(PIN_CLOCK, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(PIN_CLOCK, GPIO.LOW)
    time.sleep(0.25)

def Latch():
    time.sleep(0.25)
    GPIO.output(PIN_LATCH, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(PIN_LATCH, GPIO.LOW)
    time.sleep(0.25)

def GetHour():
    now = datetime.datetime.now()
    temp = ((now.hour - 6) % 12)
    if temp == 0:
        return 12
    return temp

def GetMinute():
    now = datetime.datetime.now()
    return now.minute

def GetSecond():
    now = datetime.datetime.now()
    return now.second

def ParseFirstDigit(digit):
    if digit < 10:
        return "0"
    string = str(digit)
    return string[:1]

def ParseLastDigit(digit):
    string = str(digit)
    return string[-1:]

def ConvertTimeToArray(number):
    if number == "0":
        return [False,False,True,True]
    if number == "1":
        return [False,False,True,True]
    if number == "2":
        return [False,False,True,True]
    if number == "3":
        return [False,False,True,True]
    if number == "4":
        return [False,False,True,True]
    if number == "5":
        return [False,False,True,True]
    if number == "6":
        return [False,False,True,True]
    if number == "7":
        return [False,False,True,True]
    if number == "8":
        return [False,False,True,True]
    if number == "9":
        return [False,False,True,True]
    return "error"
	
#def ConvertTimeToArray(number):
#    if number == "0":
#        return [False,False,False,False]
#    if number == "1":
#        return [False,False,False,True]
#    if number == "2":
#        return [False,False,True,False]
#    if number == "3":
#        return [False,False,True,True]
#    if number == "4":
#        return [False,True,False,False]
#    if number == "5":
#        return [False,True,False,True]
#    if number == "6":
#        return [False,True,True,False]
#    if number == "7":
#        return [False,True,True,True]
#    if number == "8":
#        return [True,False,False,False]
#    if number == "9":
#        return [True,False,False,True]
#    return "error"

#===========================================================================================
#main

print("starting")

for val in [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]:
    GPIO.output(PIN_SERIAL, val)
    Clock()
    GPIO.output(PIN_SERIAL, GPIO.LOW)
Latch()

while True:

    hours = GetHour()
    mins = GetMinute()

    for val in ConvertTimeToArray(ParseLastDigit(mins)):
        GPIO.output(PIN_SERIAL, val)
        Clock()
        GPIO.output(PIN_SERIAL, GPIO.LOW)
    for val in ConvertTimeToArray(ParseFirstDigit(mins)):
        GPIO.output(PIN_SERIAL, val)
        Clock()
        GPIO.output(PIN_SERIAL, GPIO.LOW)
    for val in ConvertTimeToArray(ParseLastDigit(hours)):
        GPIO.output(PIN_SERIAL, val)
        Clock()
        GPIO.output(PIN_SERIAL, GPIO.LOW)
    for val in ConvertTimeToArray(ParseFirstDigit(hours)):
        GPIO.output(PIN_SERIAL, val)
        Clock()
        GPIO.output(PIN_SERIAL, GPIO.LOW)

    print(datetime.datetime.now())
    print("hours")
    print(hours)
    print(ConvertTimeToArray(ParseFirstDigit(hours)))
    print(ConvertTimeToArray(ParseLastDigit(hours)))
    print("mins")
    print(mins)
    print(ConvertTimeToArray(ParseFirstDigit(mins)))
    print(ConvertTimeToArray(ParseLastDigit(mins)))

    Latch()
    time.sleep(15)
    
    print("looping")
