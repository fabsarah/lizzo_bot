#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:47:15 2019
The lizzo_bot is a bot that lives in python and prints encouragement 
to the console using the most powerful magic of all: Lizzo lyrics.
@author: fabsarah
"""

def lizzo_bot():

    from random import randint
    a = randint(0,9) #selects a random integer between 0 and 9. Increase this if you wat to add more responses
    if a==0: #the integer selected corresponds to the responses below. Customize as you like.
        print ("Lit up like a crystal ball That's cool, baby, so is you!")
    elif a==1:
        print ("Walk your fine ass out the door!")
    elif a==2:
        print ("BABY, WORSHIP ME!")
    elif a==3:
        print ("You are your inspiration! YOU ARE YOUR INSPIRATION!")
    elif a==4:
        print ("I just took a DNA test, turns out I'm 100% that bitch!")
    elif a==5:
        print ("I don't play tag, bitch, I been it!")
    elif a==6:
        print ("You don't need a crown to know that you're a Queen!")
    elif a==7:
        print ("Independent! Athletic!")
    elif a==8:
        print ("Mirror, mirror on the wall, tell me what you see. It's that, oh my God, it's lookin' heavenly!")
    elif a==9:
        print ("Blame it on my juice, baby!")