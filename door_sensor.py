# This program is for use with GPIO, raspberry pi, picamera and a magnetic door sensor

import RPi.GPIO as GPIO #import the GPIO library  
import datetime
import picamera
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

name = "Girlpower"  
print("Hello " + name)

door = 0

with picamera.PiCamera() as camera:
  while True:
    if GPIO.input(11) and door == 1:
      now = datetime.datetime.now()
      current_time = datetime.time(now.hour, now.minute, now.second)
      with open('/home/pi/alarm_logs', 'a') as f:
        f.write('Door was opened at %s, check your stuff!!\n' % current_time)
      n = 1
      while n < 4  and door == 1:
        print("DOOR OPENED: %s" % current_time)
        print("YOU ARE SOOOO CAUGHT, SAY CHEESE!!!!")
      
        camera.hflip = True
        camera.vflip = True
        now = datetime.datetime.now()
        current_time = datetime.time(now.hour, now.minute, now.second)
        camera.capture('/home/pi/Pictures/pic-%s.jpg' % current_time)
        print("EVIDENCE !!!!! Picture 'pic-%s.jpg' is in your 'Pictures' folder" % current_time)
        sleep(1)
        n += 1
      now = datetime.datetime.now()
      current_time = datetime.time(now.hour, now.minute, now.second)
      print("Door still open at %s" % current_time)
      door = 0
    if (GPIO.input(11) == False and door != 1):
      n = 1
      while n < 2:
        now = datetime.datetime.now()
        current_time = datetime.time(now.hour, now.minute, now.second)
        print("DOOR CLOSED: %s" % current_time)
        with open('/home/pi/alarm_logs', 'a') as f:
          f.write('Door was closed at %s, your stuff is safe....\n' % current_time)
        n += 1
      now = datetime.datetime.now()
      current_time = datetime.time(now.hour, now.minute, now.second)
      print("Door still closed at %s" % current_time)
      door = 1
     
