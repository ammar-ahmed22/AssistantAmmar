import os
import time
import random

sayingsFile = open('sayings.txt', "r")



chosen = sayingsFile.read().splitlines()

def sendMessage(phoneNumber, message):
    os.system('osascript send.scpt {} "{}"'.format(phoneNumber, message))


def run():
    counter = random.randint(0, len(chosen)-1)
    message = chosen[counter] + '\n -From Ammar\'s Assistant :)'

    sendMessage(4168932204, message)



try:
    print("Bot running...")
    count = 0
    while True:
        run()
        count += 1
        print(f"{count} messages sent")
        time.sleep(3600)
except KeyboardInterrupt:
    print('stopping...')