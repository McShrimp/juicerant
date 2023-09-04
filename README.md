<h1 align="center">Juicerant🍇 - Valorant Colorbot </h1>

![](https://img.shields.io/github/downloads/McShrimp/juicerant/total) ![](https://img.shields.io/discord/1069832469622304841)


Juicerant is a highly efficient color aimbot designed to rapidly scan for a range of purple color of the valorant enemy player outlines on your screen and precisely aim/shoot at it, without any interference with the game memory or files of Valorant.

Unlike conventional video game cheats that rely on the process memory to function, Juicerant adopt a unique approach by avoiding any memory reading altogether. This innovative approach has the potential to remain undetectable by anti-cheat mechanisms that typically attempt to block memory reads. Additionally, sending input to the video game without triggering any flags can be a challenging aspect to consider.

The primary objective of this project is to showcase a proof of concept, demonstrating the potential of Colorant's novel approach to aimbot technology.

![image](https://i.ibb.co/Zcn0n8g/juicer.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Join Our Discord Community](#join-our-discord-community)
- [License](#license)

## Introduction

Juicerant is a unique tool developed to help you enhance your aiming skills in Valorant. By combining advanced software algorithms with customizable settings, it empowers you to train and improve your aim like never before.

![Juicerant in Action](juicerant-action.gif)

## Features

- **Precision Training**: Juicerant offers a range of training scenarios and drills designed to improve your accuracy and reflexes (aims for you).

- **Customizable Settings**: Tailor your training experience with adjustable sensitivity, target tracking, and more.

- **Premium Version**: Unlock additional features and benefits with our premium version such as triggerbot, silent flickbot, flickbot, better tracking, and more, available exclusively on our Discord community.

## Requirements
1. Brain (optional with premium)
2. [Arduino Leonardo](https://www.amazon.com/Arduino-org-A000057-Arduino-Leonardo-Headers/dp/B008A36R2Y)
3. [Soldered Usb Host Shield (Will need to solder if not pre-soldered)](https://www.amazon.com/HiLetgo-Shield-Arduino-Support-Android/dp/B01MTU9OLM) (optional with premium and more work and $$$ than buying premium)
4. [Arduino Ide](https://www.arduino.cc/en/software) (optional with premium)
5. [Python](https://www.python.org/)

## Installation

1. Clone this repository to your local machine.
2. Put your COM port in for the COM port section (You can check this in device manager)
3. Start main.py
4. Profit ???



## Getting Started

The initial setup can be a bit challenging, as you will need to set up your Arduino and USB host shield **THE SETUP IS AUTOMATED WITH PREMIUM AND NO HOST SHIELD REQUIRED**. It is important to note that some USB shields may come unsoldered, so you may need to solder both 5V ports and the bottom 3.3V port to ensure that it works correctly. For further clarification, you can refer to [THIS](https://www.youtube.com/watch?v=1dxwU87GQVM) video.

Next, you will need to download and install Python, with [Version 3.8](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe) being recommended as it was the version used to develop this project. Once Python is installed, you can download Colorant and install the necessary dependencies by using the command `pip install -r requirements.txt`.

To utilize the Arduino board as a computer mouse, now you upload the Arduino.ino sketch to the board via the Arduino IDE. This sketch can be located within the [Arduino folder](https://github.com/lovelylemons/juicerant/tree/main/Arduino). The process involves connecting the Arduino board to the computer, opening the Arduino IDE software, selecting the appropriate board and port, and uploading the sketch. By completing these steps, you can transform their Arduino board into a functional computer mouse, allowing for the control of the computer's cursor and clicking functions through the board's hardware.

With the prerequisites and dependencies installed, you can now run the `main.py` file, which is the main entry point of the program. You do not need to make any changes to the code, as it is ready to use.

By following these steps, you can enjoy using Juicerant to quickly and accurately aim and shoot within your favorite Valorant gamemode.

Finally you can start Juicerant and are good to go!

![](https://i.gifer.com/origin/46/460284f4bfacd7f34bbdae886a46ea06_w200.gif)

## Configuration
You can customize Juicerant to suit your preferences:

- Enemy outlines should be set to PURPLE, as this is how the color aimbot operates.
- The FOV size can be adjusted by editing the value located in settings.ini, please note that the existing code is optimized for the use of a 100 FOV, so adjustments to the code may be required to ensure proper functionality for other fov sizes.
- Modify keybinds by changing the virtual-key codes in the settings.ini file aswell. Refer to [This](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes) link for virtual-key codes.

## Join Our Discord Community

Unlock the full potential of Juicerant by joining our Discord community. Here, you'll get access to the premium version, exclusive tips and tricks, and the chance to connect with other Valorant enthusiasts.

[Join Juicerant Discord](https://discord.gg/freMnBpdVM)


## License

Juicerant is released under the MIT License.
