from src.infra.DatabaseManager import DatabaseManager


class MessageTemplateRepository:
    def __init__(self):
        database = DatabaseManager().start()
        self.collection = database['templates']
                
    def findOne(self, condition):
        return self.collection.find_one(condition)
