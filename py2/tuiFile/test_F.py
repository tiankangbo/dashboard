# coding:utf8

# import msvcrt
#
# while 1:
#     if msvcrt.kbhit(): # Key pressed
#         a = ord(msvcrt.getch()) # get first byte of keyscan code
#         if a == 0 or a == 224: # is it a function key
#             b = ord(msvcrt.getch()) # get next byte of key scan code
#             x = a + (b*256) # cook it.
#             print "x", x # return cooked scancode
#         else:
#             print "a", a # else return ascii code

import os
import sys
import tty, termios
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
try :
    tty.setraw(fd)
    ch = sys.stdin.read(1)
    print ord(ch)
finally :
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)