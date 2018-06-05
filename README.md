# Messenger

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Developed by Jake Piccini

j.piccini@icloud.com


## Table of Contents
* [Project Description](#project-description)
* [Features](#features)
* [Requirements](#requirements)
* [Execution](#execution)


## Project Description
* Messenger is an application that uses Mosquitto's test server (test.mosquitto.org) as a broker to send messages between two or more computers.


## Features
* Name: You can set what name is displayed with your messages
* Color: You can change the color that your messages are displayed in
* Menubar: Allows you to open this README file as well as an About window
* Resizable: You can drag from a corner to make the window bigger
* Command Line Reader: A separate Python file to be run along Messenger that allows you to see the raw data from the chat


## Requirements
* An internet connection
* Mosquitto (follow instructions to install)
  * Mac:
    * in Terminal, run `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    * in Terminal, run `brew install mosquitto`
    * in Terminal, run `$ /usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf`
  * PC:
    * from the folder containing the messenger app, open 'Windows Mosquitto'
    * copy the folder 'mosquitto' to C:/Program Files (x86)


## Execution
* Mac:
  * Open the file 'Messenger.py' using your Python Editor (ex. IDLE, PyCharm)
  * Run the program (F5)
* PC:
  * Double click the 'Messenger.py' file


## To view/edit the code
* Mac:
  *Open the file 'Messenger.py' using your Python Editor (ex. IDLE, PyCharm)
* PC:
  * Right click the 'Messenger.py' file and select 'Edit with IDLE'


## To run Command Line Reader
* Mac:
  * Open the file 'Command Line Reader.py' using IDLE
  * In the title bar, you will find the pathway for the file
  * In Terminal, type 'python ' followed by the pathway after your user directory, inserting a '\' before every space
    * Ex: The pathway is '/Users/bob/Documents/Messenger/Command Line Reader.py' 
            Type 'python Documents/Messenger/Command\ Line\ Reader.py' into Terminal
* PC:
  * Double click the 'Command Line Reader.py' file


## To send a message
* Enter the name you want to be displayed with your message into the Name Box
* Select the color you want the message to be displayed in from the Color Dropdown Menu
* Type your message into the long box under the Message Window (displaying 'You have joined a chat with the topic...’)
* Press 'Send' or the Enter/Return key on your keyboard


## Make a unique chatroom
* The default topic is 'jakepic/messenge'
* To make a different room, edit the 'topic' string variable in the first line of code in 'Messenger.py'
* Ensure that all computers wanting to connect to this chatroom have changed it to the same thing
* If you want to use the Command Line Reader, change the ‘topic' string variable in the first line of code in 'Command Line Reader.py' as well


## Possible errors
* If you are not connect to the internet, the app will not work
  * FIX: Connect to the internet
* If the string of "#!?#@@!" is anywhere in the message or name, it will not allow you to send the message
  * FIX: Remove "#!?#@@!" from your name or message
* If you are using Python 3 versus Python 2.7, Tkinter won’t import properly 
  * FIX: In line 3, change 'Tkinter' to 'tkinter', and change line 5 to 'from tkinter import ttk' 