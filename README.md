# WhatsApp Bot
This is an WhatsApp Bot developed using Python, MongoDB, Twilio, Flask and Ngrok

## Preview

missing field

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


# Start the App - does not require venv activated
zsh commands/dev.zsh
```
