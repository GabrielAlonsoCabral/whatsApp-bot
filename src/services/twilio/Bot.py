from dotenv import dotenv_values
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from time import sleep
from src.infra.repositories.MessageTemplateRepository import MessageTemplateRepository

config = dotenv_values(".env")

class Bot:
    def __init__(self, user_message):
        self.user_message = user_message
        self.client = Client(config["TWILIO_ACCOUNT_SID"],config["TWILIO_AUTH_TOKEN"])
        self.messagingResponse = MessagingResponse()
        self.MessageTemplateRepository = MessageTemplateRepository()

    def __message(self):
        return self.messagingResponse.message()

    def __getTemplate(self):
        messageTemplate = self.MessageTemplateRepository.findOne(condition={"active":True})
        return messageTemplate['templates']

    def __getStep(self, step):
        templates = self.__getTemplate()
        return next(item for item in templates if item['step'] == step)

    def __getOptionsMessageByStep(self, step):
        options = self.__getStep(step)['options']
        optionsMessage = ""
        for option in options:
            optionMessage = options[option]
            optionsMessage += f"\n{option} - {optionMessage}\n"

        return optionsMessage

    def listAllStepsOptions(self):
        templates = self.__getTemplate()
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

        self.__message().body(stepMessage.replace('\\n','\n'))
        sleep(1)
        self.__message().body(optionsMessage.replace('\\n','\n'))
        return str(self.messagingResponse)
