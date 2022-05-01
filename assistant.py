from dotenv import load_dotenv
load_dotenv()

import os
import time
import random

FILE_PATH = os.environ.get("FILE_PATH")
PHN_NUMBER = os.environ.get("PHN_NUMBER")
INTERVAL = os.environ.get("INTERVAL")
BOT_NAME = os.environ.get("BOT_NAME")

error = False

if (not FILE_PATH or not PHN_NUMBER or not INTERVAL and not BOT_NAME):
    print("Please provide all required env variables")
    error = True


if (not error):

    sayingsFile = open(FILE_PATH, "r")



    chosen = sayingsFile.read().splitlines()

    def sendMessage(phoneNumber, message):
        os.system('osascript send.scpt {} "{}"'.format(phoneNumber, message))


    def run():
        counter = random.randint(0, len(chosen)-1)
        message = chosen[counter] + f'\n -From {BOT_NAME} :)'

        sendMessage(PHN_NUMBER, message)


    try:
        print("Bot running...")
        count = 0
        while True:
            run()
            count += 1
            print(f"{count} messages sent")
            time.sleep(int(INTERVAL))
    except KeyboardInterrupt:
        print('stopping...')