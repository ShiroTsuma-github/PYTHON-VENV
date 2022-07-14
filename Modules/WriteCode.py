import pyautogui
from pathlib import Path
import regex as re

class AutoText:
    def __init__(self) -> None:
        self.__file = None
        self.__tabdepth = 0

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, filename: str) -> None:
        temp = Path(filename)
        if temp.is_file():
            self.__file = open(temp, encoding='utf-8')
        else:
            print('File doesn\'t exist or path is not correct')
            self.__file = None

    def Write(self, speed: int = 0.1) -> None:
        if self.__file is None:
            return
        for line in self.__file.readlines():
            depth_get = re.match(r'(^\s*)\w', line)
            if depth_get:
                spaces = len(depth_get.group(1))
                print(spaces)
            else:
                spaces = 0
            pyautogui.write(line.replace('\n', ''), interval=speed)
            if line.endswith('\n'):
                pyautogui.press('enter')
            for _ in range(spaces - 1):
                pyautogui.press('spacebar')

"""
NOTE:
    It idk why doesn't work in vs code. 
    propably cuz of autoindentation in python.
    It does work when tested in notepad.
USAGE:
    a = AutoText()
    a.file = 'Filepath'
    a.Write(0.1)
"""