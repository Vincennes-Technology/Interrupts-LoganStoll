#!/usr/bin/python
#Logan Stoll (not made by me)
# Script written by Alex Eames. Http://RasPi.tv. Original comments retained.
# Slight variations made by Justin Limbach (noted in comments)
#Stolen from Justin Limbach (I changed comments)
    #updated LCD messages 

import RPi.GPIO as GPIO
import time
# Displaying to LCD deviation from original code
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 24 set up as inputs. Justin Limbach) modified the original
# Script so both are pulled up and waiting for a falling edge.
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time_stamp = time.time()

# now we'll define the threaded callback function
# This will run in another thread when our event is detected
def my_callback(channel):
    lcd.clear()
    lcd.message('Port 24 \nhas fallen')

    # Omitted extra print lines here, because why not. 

raw_input(lcd.message('  As you want, \n   Logan\n>'))
# Setting up so that when port 24 has falling edge, my_callback happens

GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime = 200)

# Changed the text to talk to me 
try:
    lcd.clear()
    lcd.message('   Aiming at \n    Port 23')
    GPIO.wait_for_edge(23, GPIO.FALLING)
    lcd.clear()
    lcd.message('   The edge \n   has fallen.')

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
