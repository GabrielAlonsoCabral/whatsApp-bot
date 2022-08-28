from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

class Bot:
    def __init__(self):
        self.user_message= request.values.get('Body', '').lower()
        self.messagingResponse = MessagingResponse()

    def message(self):
        return self.messagingResponse.message()

    def execute(self):
        return self.start()

    def start(self):
        introductionMessage = "Olá, eu sou a Ci! A sua Atendente Virtual. \n \nComo que eu posso te ajudar ? \nDigite o número da opção desejada."
        optionsMessage = '1. Quero saber mais sobre a Citizens. \n2. Quero saber mais sobre o Citizens Email. \n3. Quero saber mais sobre o Citizens Mobile'
        
        self.message().body(introductionMessage)
        self.message().body(optionsMessage)
        return str(self.messagingResponse)

@app.route('/', methods=['POST'])
def botAction():
    bot = Bot()
    return bot.execute()

if __name__ == '__main__':
    app.run()
