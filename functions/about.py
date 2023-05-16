from .clean import clean

blue = '\033[96m'
white = '\033[37m'
red = '\033[31m'
reset = '\033[0m'
green = '\033[32m'
blink = '\033[5m'
yellow = '\033[33m'
cyan = '\033[1;36m'

rgb_75 = '\x1b[38;5;75m'

def about():

    clean()

    print(" {}┌──────────────────────────────────────┐{}".format(rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}      {}MeeGPT© 2023 WunderWungiel{}      {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}            {}Version: 0.0.1{}            {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}      {}ChatGPT client for Nokia N9{}     {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}      {}written using Python 3.1.{}       {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}      {}Special thanks to:{}              {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}        {}- IarChep{}                     {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}      {}(icon, inexhaustible help{}       {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}       {}and ingenuity!){}                {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}        {}- Python{}                      {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}        {}- LM World community{}          {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}      {}Join our Telegram group:{}        {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}│{}    {}https://t.me/linuxmobile_world{}    {}│{}".format(rgb_75, reset, white, reset, rgb_75, reset))
    print(" {}│{}                                      {}│{}".format(rgb_75, reset, rgb_75, reset))
    print(" {}└──────────────────────────────────────┘{} \n".format(rgb_75, reset))
    input(" {}{}Press Enter to continue... {}".format(blink, cyan, reset))