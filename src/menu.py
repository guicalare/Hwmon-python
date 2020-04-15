from utils import *
from os import system
import subprocess

class Menu():

    def __init__(self):

        print("\033c")
        is_vm()

    def user_input(self, options):

        user = ''

        while user not in options.keys():
            print_dict(options)
            user = input('>>> Option: ')
            print("\033c")
        
        return user

    def menu(self):

        options = {'1':'Sensors data', '2':'CPU data', '3':'Memory data',
                    '4':'Network data', '5':'Exit'}
        
        user = self.user_input(options)

        if user == '1':
            try:
                subprocess.call(["watch", "python3", "watch_hwmon.py"])
            except KeyboardInterrupt:
                Menu().menu()
        elif user == '2':
            try:
                subprocess.call(["watch", "python3", "watch_cpumon.py"])
            except KeyboardInterrupt:
                Menu().menu()
        elif user == '3':
            try:
                subprocess.call(["watch", "python3", "watch_memmon.py"])
            except KeyboardInterrupt:
                Menu().menu()
        elif user == '4':
            try:
                subprocess.call(["watch", "python3", "watch_netmon.py"])
            except KeyboardInterrupt:
                Menu().menu()
        elif user == '5':
            exit()

Menu().menu()