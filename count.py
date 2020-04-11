"""compteur de mountons
"""

import time

SHEEP_COUNTER = 1
WAITING_TIME = 0.3333333333333333


def print_sheep(file):
    """ afiche a l ecran le fichier demander
"""
    animation = open(file)
    print(chr(27) + "[2J")
    for line in animation:
        line = line[:-1]
        print(line)
    if SHEEP_COUNTER == 1:
        print("%s putain de mouton" % SHEEP_COUNTER)
    else:
        print("%s putain de moutons" % SHEEP_COUNTER)
    time.sleep(WAITING_TIME)

while True:
    print_sheep("sheep1")
    print_sheep("sheep2")
    print_sheep("sheep3")
    SHEEP_COUNTER = SHEEP_COUNTER + 1
