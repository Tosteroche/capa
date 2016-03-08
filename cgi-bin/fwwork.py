import os
from config import rule


def addToRule(mac):
    os.popen(rule % mac)
