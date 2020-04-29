import os
import json

from messages import Messages

class AutoDoc:
    def __init__(*args, **kwargs):
        #python autoDoc.py document 'targetDir' 'doctype' projectName
        #python autoDoc.py logs projectName 
        pass

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
    a=AutoDoc()
    a.main()