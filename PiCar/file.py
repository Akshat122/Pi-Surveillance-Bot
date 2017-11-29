#!/usr/bin/env python

# servo_key.py
# 2015-04-10
# Public Domain

import time
import curses
import atexit

import pigpio 

SERVO = 4

MIN_PW = 500
MID_PW = 1000
MAX_PW = 2000

NONE        = 0
LEFT_ARROW  = 1
RIGHT_ARROW = 2
UP_ARROW    = 3
DOWN_ARROW  = 4
HOME        = 5
QUIT        = 6

def getch():
   global in_escape, in_cursor
   c = stdscr.getch()

   key = NONE

   if c == 27:
      in_escape = True
      in_cursor = False
   elif c == 91 and in_escape:
      in_cursor = True
   elif c == 68 and in_cursor:
      key = LEFT_ARROW
      in_escape = False
   elif c == 67 and in_cursor:
      key = RIGHT_ARROW
      in_escape = False
   elif c == 65 and in_cursor:
      key = UP_ARROW
      in_escape = False
   elif c == 66 and in_cursor:
      key = DOWN_ARROW
      in_escape = False
   elif c == ord('q'): 
      key = HOME
#      in_escape = False
   elif c == 113 or c == 81:
      key = QUIT
   else:
      
      in_escape = False
      in_cursor = False

   return key

def cleanup():
   curses.nocbreak()
   curses.echo()
   curses.endwin()
   pi.stop()

pi = pigpio.pi()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

atexit.register(cleanup) # Ensure original screen state is restored.

in_escape = False
in_cursor = False

pulsewidth = MID_PW

pi.set_servo_pulsewidth(SERVO, pulsewidth)

while True:

   time.sleep(0.01)

   c = getch()

   if c == QUIT:
      break

   pw = pulsewidth

   if c == HOME:
      pw = MID_PW # MID
   elif c == UP_ARROW:
      pw = MAX_PW # RIGHT
   elif c == DOWN_ARROW:
      pw = MIN_PW # LEFT
   elif c == LEFT_ARROW:
      pw = pw - 100 # Shorten pulse.
   elif c == RIGHT_ARROW:
      pw = pw + 100 # Lengthen pulse.
      
   if pw != pulsewidth:
      pulsewidth = pw
      pi.set_servo_pulsewidth(SERVO, pulsewidth)
