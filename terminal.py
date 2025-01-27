#!/bin/env python3

import sys
from time import sleep

# Allowed Colors
aColors = {
    "white":"\033[38;2;255;255;255m",
    "blue":"\033[38;2;0;150;255m",
    "purple":"\033[38;2;150;0;255m",
    "green":"\033[38;2;0;255;150m",
    "orange":"\033[38;2;255;150;0m",
    "reset":"\033[0m"
}

def echo(text:str="", color:str="white") -> None:
    try:
        aColors[color]
    except KeyError:
        color = "white"

    print(f"""{aColors[color]}{text}{aColors["reset"]}""")

class progress:
    def __init__(self):
        self.length = 25
        self.stat = 0
        self.running = False
        self.message = ""
        self.msgSet = False

    def start(self):
        self.running = True
        mAge = 1
        c = 1
        steps = ["\\", "|", "/", "\u2014"]
        while self.running:
            lengthGreen = int(round(self.length * (self.stat / 100), 0))
            lengthWhite = self.length - lengthGreen
            print(f"  {steps[c-1]} [{self.stat}%] ", f"{aColors['green']}\u2588"*lengthGreen, f"{aColors['white']}\u2500"*lengthWhite, f"{aColors['reset']}", sep="")
            try:
                print(f"    \033[2m- {self.message}{aColors['reset']}")
            except IndexError:
                print("")

            sleep(0.1)
            sys.stdout.write("\033[F")
            if self.msgSet == True:
                sys.stdout.write("\033[K")
                self.msgSet = False
            sys.stdout.write("\033[F")


            c += 1
            mAge += 1
            if c > 4:
                c = 1

    def stop(self):
        self.running = False

    def set_message(self, msg:str=""):
        self.message = msg
        self.msgSet = True

    def set_stat(self, stat:int=0):
        self.stat = stat 