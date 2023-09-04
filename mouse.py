import sys
import time
import pyautogui
import serial
import serial.tools.list_ports

from termcolor import colored
from settings import Settings

class Mouse:
    
    settings = Settings()
    
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 0
        self.serial_port.port = self.find_serial_port()
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(colored('[Error]', 'red'), colored('Juicerant is already open or Arduino is being used by another app. Close Colorant & other apps before retrying.', 'white'))
            print(colored('Exiting...', 'red'))
            time.sleep(10)
            sys.exit()

    def find_serial_port(self):
        com_port = self.settings.get('Settings', 'COM-PORT')
        port = next((port for port in serial.tools.list_ports.comports() if com_port in port.description), None)
        if port is not None:
            return port.device
        else:
            print(colored('[Error]', 'red'), colored(f'Unable to detect your specified Arduino ( {com_port} ). Please check its connection & the COM port setting in \nsettings.ini file then try again.', 'white'))
            print(colored('Exiting...', 'red'))
            time.sleep(10)
            sys.exit()

    def move(self, x, y):
        self.serial_port.write(f'M{x},{y}\n'.encode())

    def click(self):
        self.serial_port.write(b'C\n')
