# WhatsApp Bot
This is an WhatsApp Bot developed using Python, MongoDB, Twilio, Flask and Ngrok

## Preview

![alt text](preview-bot.jpeg)

## Usage

```
# Setting Virtual Environment
virtualenv venv

# Activate venv
source venv/bin/activate

# Install dependencies
pip3 install twilio flask ngrok 'pymongo[srv]'

# setting ngrok
ngrok config add-authtoken your_token_here
ngrok http 3306

Now you must insert ngrok https post on twilio console.


# Start App from using zsh
zsh commands/dev.zsh

# Start App without zsh
source venv/bin/activate

flask --app main.py --debug run --port=3306

```
