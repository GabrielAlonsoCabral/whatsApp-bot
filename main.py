from flask import Flask, request
from src.services.twilio.Bot import Bot
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def botAction():
    user_message = request.values.get('Body', '').lower()
    bot = Bot(user_message=user_message)
    return bot.execute()

if __name__ == '__main__':
    app.run(port=3306)
