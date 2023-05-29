# MeeGPT

**MeeGPT** is a **first**, **brand-new**, **working** ChatGPT client for Nokia N9 / N950 devices running MeeGo Harmattan.

[Join our Linux Mobile World group](https://t.me/linuxmobile_world).

## Installing

The easiest way to install is to use [MeeShop](https://github.com/WunderWungiel/MeeShop). Alternatively, proceed with steps below:

You need to have [Developer Mode](http://wunderwungiel.pl/MeeGo/posts/devmode-22.04.2023.html) enabled and [Aegis-hack](https://talk.maemo.org/showthread.php?t=90750).
Python needs to be installed. Run **Terminal**, and type following commands:

    devel-su
    (enter "rootme" without quotes as password)
    aegis-apt-get install python3 python3.1 -y --force-yes

Download latest release (`.deb` file) from [Releases](https://github.com/WunderWungiel/MeeGPT/releases) page, and transfer it to N9, saving in **MyDocs** (i.e. **Nokia N9** drive when connected to PC).
Run the **Terminal** again, and type following commands:

    devel-su
    (enter "rootme" without quotes as password)
    cd /home/user/MyDocs
    aegis-dpkg -i meegpt_RELEASE_armel.deb
    (replace RELEASE with the proper number, i.e. 0.0.1)

If you don't see any errors, you're ready to use MeeGPT!

## How to use

**MeeGPT** is a **CLI** app with no native **GUI**. However, it has been designed to make the usage as easy as possible! You don't need to enter any commands.
Just **run MeeGPT** from applications menu while being connected to Internet. You will see a retro-style menu with few options, like **Change model** and "**Your message**" prompt. Below is a quick description of functions.

- **Change model** - change OpenAI model to GPT-3.5 or GPT-4
- **About** - name suggest the action.

Type any message to send it to ChatGPT, or press desired number to use a selected option.

To **go back** (almost) anytime, press **0** when MeeGPT asks you for something.

## Screenshots

![Screenshot1](https://i.imgur.com/nCHUiNP.png)

## Credits

 - [IarChep / Ярослав](https://t.me/iaroslavchep) - icon and inexhaustible help and ingenuity!
 - [Python](https://python.org) for making an easy to learn, power programming language
 - [Linux Mobile World](https://t.me/linuxmobile_world) community for testing this app
