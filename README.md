# PyChat

PyChat is a chat room application that uses Mosquitto's test server (test.mosquitto.org)
as a broker to send messages between two or more computers. The UI is built using Tkinter.

Developed by Jake Piccini

j.piccini@icloud.com

## Table of Contents

* [Requirements](#requirements)
* [Run](#run)
* [Features](#features)
  * [Chat Room](#chat-room)
  * [Channel](#channel)
  * [Display Name and Color](#display-name-and-color)
  * [Messaging](#messaging)
  * [Menu Bar](#menu-bar)
  * [Command Line Reader](#command-line-reader)
* [Troubleshooting](#troubleshooting)
* [Version History](#version-history)

## Requirements

* An internet connection
* Python 2.7
* Mosquitto
  * Install on Mac:
    * `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    * `brew install mosquitto`
    * `$ /usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf`
  * Install on PC:
    * Copy `mosquito` directory from `MyChat/Windows Mosquitto/` to `C:/Program Files (x86)`

## Run

Within the `PyChat` directory, run `python PyChat.py`.

## Features

### Chat Room

_Join a room with others to send messages._

When launching the application, the room is `default`.
To change this, enter a new room name in the `Room` box and click `Set Room`.

### Channel

_Customize access to you rooms._

All chat rooms exist within a channel. The default channel is `PyChat/Default/`.
You can change this by editing the `channel` variable within `PyChat.py`.

### Display Name and Color

_Set the name and color that is shown with your messages._

Beneath the message window, you can set the name you want to appear with your messages.
You can also select what color you would like your messages to be through the `Color` dropdown menu.
Changing these will not change past messages.

### Messaging

_Send messages to people in the same chat room._

To send a message, you must first enter a display name and select a color.
Then, type your message in the box next to the `Send` button.
To send the message, press the `Send` button or the `Enter/Return` key on your keyboard.

### Menu Bar

_Get help within the application._

From the menu bar, you can open this README, see an About window, and quit the application.

### Command Line Reader

_View raw data from a chat room._

To run the Command Line Reader, run `python CommandLineReader [channel/room]` where channel is
the channel you wish to use, and room is the room you wish to view.
If no argument is given, the default is `PyChat/Default/default`

## Troubleshooting

|                                        Problem                                        |                  Solution                  |
| :-----------------------------------------------------------------------------------: | :----------------------------------------: |
|        The application will not work if you are not connected to the internet         |          Connect to the internet           |
| Your message won't send if the string of `#!?#@@!` is anywhere in the message or name | Remove `#!?#@@!` from your name or message |
|            If you are using Python 3, the application won't work properly             |               Use Python 2.7               |

## Version History

> **1.1.0** _June 7, 2018_
>
> * Refactor app to be contained in a class

> **1.0.0** _June 5, 2018_
>
> * Ability to change room from application
> * Refactor code to be neater
> * Command Line Reader takes a command line argument for room to view
> * Make README into markdown

> **0.0.0** _September 13, 2015_
>
> * First beta version of application
> * Support for custom name and color
> * Hardcoded chat room
