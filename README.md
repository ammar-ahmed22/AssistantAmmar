
# Assistant Ammar

As my wife wanted attention while I was busy studying or working, I created a bot that would message her nice things automatically every hour. As it utilizes Apple Scripts and iMessage, it only works with a Mac. 


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`FILE_PATH`: Path to .txt file that contains all the messages you want the bot to say. One message per line.

`PHN_NUMBER`: Phone number to send messages to.  

`BOT_NAME`: Name you want the bot to sign off with. (e.g. Ammar's Assistant)  

`INTERVAL`: Amount of time in seconds between each message.


## Run Locally

Clone the project

```bash
  git clone https://github.com/ammar-ahmed22/AssistantAmmar.git
```

Go to the project directory

```bash
  cd AssistantAmmar
```

Install dependency

```bash
  pip install python-dotenv
```

Create file for messages (e.g. sayings.txt) and add messages (1 per line)

```bash
  touch sayings.txt
  echo "Hello\nHey, This is from a bot\nBot message" >> sayings.txt
```
Ensure .env variables are set and run the program
```bash
python3 assistant.py
```

