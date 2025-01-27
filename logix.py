
# Logix Sysman 
# Devon Edwards (xXEthyleneXx)
# Started 2025_27_01

from terminal import echo
from terminal import progress
from time import sleep
import threading
import sys

def main():
    sys.stdout.write("\033[2J\033[H")

    prg = progress()
    prgT = threading.Thread(target=prg.start)
    try:
        echo("\033[1mLogix", "purple")

        prgT.start()
        prg.set_message("Starting System")
        sleep(5)
        prg.set_stat(100)
        sleep(5)
        prg.stop()
        prgT.join()

    except KeyboardInterrupt:
        if prg.running == True:
            prg.stop()
            prgT.join()
    

if __name__ == "__main__":
    main()
    sys.stdout.write("\033[2J\033[H")