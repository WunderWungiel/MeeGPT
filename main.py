#!/usr/bin/python3.1

import subprocess
import sys
import os
import re

from functions.api import api
from functions.clean import clean
from functions.about import about

blue = '\033[96m'
white = '\033[37m'
red = '\033[31m'
reset = '\033[0m'
green = '\033[32m'
blink = '\033[5m'
yellow = '\033[33m'
cyan = '\033[1;36m'

rgb_75 = '\x1b[38;5;75m'

models = {
    "1": "GPT-4",
    "2": "GPT-3.5"

}

models_names = {
    "GPT-4": "gpt-4",
    "GPT-3.5" : "gpt-3.5-turbo"
}

def options_list():
    print(" {}┌──────────────────────────────────────┐{}".format(rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}       {}╔══════════════════════╗{}       {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}       {}║  Welcome to MeeGPT!  ║{}       {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}       {}╚══════════════════════╝{}       {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))

    string = "AI Model: {}".format(model)
    if len(string) % 2 != 0:
        string += " "
    lenght = " " * int((38 - len(string)) / 2)
    print(" {}│{}{}{}{}{}{}{}│{}".format(rgb_75, reset, lenght, white, string, reset, lenght, rgb_75, reset))

    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}   {}{}Type your message / select option{}  {}│{}".format(rgb_75, reset, white, blink, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}            {}1. Change model{}           {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}            {}2. About{}                  {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}            {}0. Exit{}                   {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}└──────────────────────────────────────┘{} \n ".format(rgb_75, reset))

def model_changer():
    while True:
        print(" {}Supported models:{}".format(rgb_75, reset))
        for i, m in models.items():
            print(" {}. {}".format(i, m))
        print(" ")
        global model
        answer = input(" {}Enter desired model{}: ".format(yellow, white))
        if answer == "0":
            break
        if answer not in models.keys():
            model = "gpt-3.5-turbo"
            print(" {}Wrong model!{}".format(red, reset))
            print(" ")
            continue
        model = models_names[models[answer]]
        with open(".config", "w") as f:
            f.write("model = {}".format(model))
            break

def instance_checker():

    output = api(query="Yes")

    if output == "Error":
        return False
    try:
        if "error" in output.keys() or "invalid_api_key" in output.values():
            working = False
        else:
            working = True
    except:
        working = False

    return working
        
def main():

    clean()

    folder = "."
    #folder = "/opt/MeeGPT"
    if not os.path.isdir(folder):
        if os.path.isfile(folder):
            os.remove(folder)
        os.mkdir(folder)
    os.chdir(folder)

    _ = subprocess.call("ping wunderwungiel.pl -c 2 > /dev/null 2>&1", shell=True)
    if _ != 0:
        print(" {}Failed to connect, please\n check your internet connection.{}".format(red, reset))
        print()
        input(" {}{}Press Enter to continue... {}".format(blink, cyan, reset))
        clean()
        sys.exit(1)

    global model
    if not os.path.isfile(".config"):
        with open(".config", "w") as f:
            f.write("model = gpt-3.5-turbo")

    with open(".config", "r") as f:
        content = f.read()
        model = re.search("model = (.+)", content)
        if model:
            model = model.group(1)
        else:
            with open(".config", "w") as f:
                f.write("model = gpt-3.5-turbo")
                model = "gpt-3.5-turbo"
    instance = instance_checker()
    if instance == False:
        print(" {}I couldn't find working API endpoint...{}".format(red, reset))
        input(" \n {}{}Press Enter to exit... {}".format(blink, cyan, reset))
        sys.exit(0)

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
            if answer == "1":
                model_changer()
                print(" ")
                options_list()
                continue
            elif answer == "2":
                about()
                clean()
                options_list()
                continue
            elif answer == "0":
                sys.exit(0)
        
        else:

            result = api(query=answer, model="gpt-3.5-turbo")
            print(" {}══════════════════════════════════════{}\n ".format(white, reset))
            ai_answer = result['choices'][0]['message']
            if isinstance(ai_answer, dict):
                ai_answer = ai_answer['content']
            ai_answer = ai_answer.splitlines()  # Podzielenie ciągu na linie
            ai_answer = [' ' + line for line in ai_answer]
            ai_answer = '\n'.join(ai_answer)
            ai_answer = " {}ChatGPT:{}".format(yellow, reset) + white + ai_answer + reset

            print(ai_answer)
            print("\n {}══════════════════════════════════════{}\n ".format(white, reset))

if __name__ == "__main__":
    main()