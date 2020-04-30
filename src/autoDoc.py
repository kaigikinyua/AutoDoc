import os
import json
import sys

from utils.messages import Message

class AutoDoc:
    targetDir=""
    dType=""
    projectName=""
    def __init__(self,targetDir,dType,projectName):
        self.targetDir=targetDir
        self.dType=dType
        self.projectName=projectName
        print(self.targetDir,self.dType,self.projectName)

    def main(self):
        print("WELCOME to autodoc!!\nPlease enter the project directory to start documenting your project automatically\n")
        if(self.project_dir("/home/antony/fajkfakl")):
            self.get_documentation_type()

    def get_documentation_type(self):
        options={"1":"Full","2":"Web","3":"Word"}
        print("So which option would you like?")
        i=1
        #Print the options of the type of documentation  
        for option in options:
            print(option+" "+options[option])           
        op=input()
        if(int(op)<3):
            print(f"Running option {options[op]}")
            #run the option
            self.doc_type(option[op])
        else:
            print("Invalid option\n Running default option")
            #run default option
            self.doc_type(options["3"])


    def doc_type(self,doc_option):
        if(doc_option=="Full"):
            pass 
        elif(doc_option=="Web"):
            pass
        else:
            pass

    #get project directory from user
    def project_dir(self,directory):
        if(os.path.isdir(directory)):
            Messages.success("Directory is correct")
            return True 
        else:
            Messages.error(str(directory)+" is not a directory")
            return False

    def comment_preceeding(self):
        options={"1":"#","2":"//","3":"/*"}
        pass 

    def existing_docs(self):
        pass

    def html_doc(self):
        pass

    def word_doc(self):
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
    #a=AutoDoc()
    #a.main()