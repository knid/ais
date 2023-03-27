# -*- coding: utf-8 -*-
import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
