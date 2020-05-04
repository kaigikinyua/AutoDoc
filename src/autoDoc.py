import os
import json
import sys
from threading import *
from utils.messages import Message

class AutoDoc:
    targetDir=""
    dType=""
    projectName=""
    def __init__(self,targetDir,dType,projectName):
        self.targetDir=targetDir
        self.dType=dType
        self.projectName=projectName

    def start_documentation(self):
        pass

    def get_documentation_type(self):
        pass

class DocumentationType:
    @staticmethod
    def word(targetDir):
        pass
    
    @staticmethod
    def html(targetDir):
        pass
    
    @staticmethod
    def markdown(targetDir):
        pass
    
    @staticmethod
    def all(targetDir):
        pass



if __name__=="__main__":
    arguments=sys.argv
    if(len(arguments)<2 or len(arguments)>5):
        print("Available commands are : document <documentation_type> <target_directory> <project_name>")
        print(":log <project_name>")
    else:
        if(arguments[1]=="document"):
            a=AutoDoc(targetDir=arguments[3],dType=arguments[2],projectName=arguments[4])
        elif(arguments[1]=="log"):
            print(arguments)
        else:
            print(arguments[1]+" is unknown")
            print("Available commands are : document <documentation_type> <target_directory> <project_name>")
            print(":log <project_name>")
