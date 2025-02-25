#!/usr/bin/python3.1

import subprocess
import sys
import os
import re

from lib.api import api
from lib.clean import clean
from lib.about import about

blue = '\x1b[38;5;75m'
white = '\033[37m'
red = '\033[31m'
reset = '\033[0m'
green = '\033[32m'
blink = '\033[5m'
yellow = '\033[33m'
cyan = '\033[1;36m'


def options_list():
    print(" {}┌──────────────────────────────────────┐{}".format(blue, reset))
    print(" {}│{}                                      {}│{}".format(blue, reset, blue, reset))
    print(" {}│{}       {}╔══════════════════════╗{}       {}│{}".format(blue, reset, white, reset, blue, reset))
    print(" {}│{}       {}║  Welcome to MeeGPT!  ║{}       {}│{}".format(blue, reset, white, reset, blue, reset))
    print(" {}│{}       {}╚══════════════════════╝{}       {}│{}".format(blue, reset, white, reset, blue, reset))
    print(" {}│{}                                      {}│{}".format(blue, reset, blue, reset))
    print(" {}│{}   {}{}Type your message / select option{}  {}│{}".format(blue, reset, white, blink, reset, blue, reset))
    print(" {}│{}                                      {}│{}".format(blue, reset, blue, reset))
    print(" {}│{}            {}1. About{}                  {}│{}".format(blue, reset, white, reset, blue, reset))
    print(" {}│{}                                      {}│{}".format(blue, reset, blue, reset))
    print(" {}│{}            {}0. Exit{}                   {}│{}".format(blue, reset, white, reset, blue, reset))
    print(" {}│{}                                      {}│{}".format(blue, reset, blue, reset))
    print(" {}└──────────────────────────────────────┘{} \n ".format(blue, reset))
        
def main():

    clean()

    #folder = "."
    folder = "/opt/MeeGPT"
    if not os.path.isdir(folder):
        if os.path.isfile(folder):
            os.remove(folder)
        os.mkdir(folder)
    os.chdir(folder)

    _ = subprocess.call("ping gnu.org -c 2 > /dev/null 2>&1", shell=True)
    if _ != 0:
        print(" {}Failed to connect, please\n check your internet connection.{}".format(red, reset))
        print()
        input(" {}{}Press Enter to continue... {}".format(blink, cyan, reset))
        clean()
        sys.exit(1)
    
    options_list()

    while True:
        
        try:
            answer = input(" {}Your message:{} ".format(yellow, white))
        except KeyboardInterrupt:
            print(" {}KeyboardInterrupt, exiting...{}".format(red, reset))
            sys.exit(0)

        supported = ["1", "2", "0"]

        print(" ")

        if answer.isnumeric():
            if answer not in supported:
                print(" {}Wrong number, select a correct one!{}".format(red, reset))
                print(" ")
                continue
            elif answer == "1":
                about()
                clean()
                options_list()
                continue
            elif answer == "0":
                sys.exit(0)
        
        else:

            result = api(query=answer)
            print(" {}══════════════════════════════════════{}\n ".format(white, reset))
            ai_answer = result['choices'][0]['message']
            if isinstance(ai_answer, dict):
                ai_answer = ai_answer['content']
            ai_answer = ai_answer.splitlines()
            ai_answer = [' ' + line for line in ai_answer]
            ai_answer = '\n'.join(ai_answer)
            ai_answer = " {}Gemini:{}".format(yellow, reset) + white + ai_answer + reset

            print(ai_answer)
            print("\n {}══════════════════════════════════════{}\n ".format(white, reset))

if __name__ == "__main__":
    main()
