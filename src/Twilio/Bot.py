from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from time import sleep
from dotenv import dotenv_values

config = dotenv_values(".env")

class Bot:
    def __init__(self, user_message):
        self.user_message = user_message
        self.client = Client(config["TWILIO_ACCOUNT_SID"],config["TWILIO_AUTH_TOKEN"])
        self.messagingResponse = MessagingResponse()

    def __message(self):
        return self.messagingResponse.message()

    def __getTemplates(self):
        templates = [
            {
                "step":"0.0",
                "message":"Olá, eu sou a Ci! A sua Atendente Virtual. \n \nComo que eu posso te ajudar ? \nDigite o número da opção desejada.",
                "options":{
                    "1.0":"Quero ter um Aplicativo para minha empresa!",
                    "2.0":"Quero saber sobre a ferramenta de disparo de emails em massa!",
                    "3.0":"Quero um Chatbot de WhatsApp para minha empresa!",
                    "4.0": "Quero um site personalizado para minha empresa!",
                    "5.0":"Quero um Software personalizado!",
                    "6.0":"Quero saber mais sobre vocês.",
                }
            },
            {
                "step":"1.0",
                "message":"Aplicativo para empresa",
                "options":{
                    "1.1":"teste"
                }
            }
        ]

        return templates

    def __getStep(self, step):
        templates = self.__getTemplates()
        return next(item for item in templates if item['step'] == step)

    def __getOptionsMessageByStep(self, step):
        options = self.__getStep(step)['options']
        optionsMessage = ""
        for option in options:
            optionMessage = options[option]
            optionsMessage += f"\n{option} - {optionMessage}\n"

        return optionsMessage

    def listAllStepsOptions(self):
        templates = self.__getTemplates()
        allStepsOptions = []

        for template in templates:
            options = template['options']
            for option in options:
                allStepsOptions.append(option)
        return allStepsOptions

    def execute(self):
        availableStepsOptions = self.listAllStepsOptions()
        existsInput = self.user_message in availableStepsOptions
        print(existsInput)
        return self.__sendMessagesByStep("0.0")        
    
    def __sendMessagesByStep(self, stepNumber):
        step = self.__getStep(stepNumber)
        stepMessage = step["message"]
        optionsMessage = self.__getOptionsMessageByStep(step=stepNumber)

        self.__message().body(stepMessage)
        sleep(1)
        self.__message().body(optionsMessage)
        return str(self.messagingResponse)
