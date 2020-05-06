import os
from docx import Document
from utils.messages import Messages
from utils.files import Files

class Word:
    def __init__(self,*args, **kwargs):
        pass

    def loadConfigs(self):
        pass
    
    def documentFile(self):
        pass

    def check_existing_doc(self):
        pass 

    def new_word_document(self):
        pass

    def documentation_version(self):
        pass

class WordComponents:
    
    @staticmethod
    def title(obj,title):
        pass
    
    @staticmethod
    def subtitle(obj,subtitle):
        pass

    @staticmethod
    def paragraph(obj,text):
        pass

    @staticmethod
    def addList(obj,text):
        pass

    @staticmethod
    def image(obj,imagePath):
        pass

    @staticmethod
    def italic(text):
        pass