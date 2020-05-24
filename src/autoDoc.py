import os
import json
import sys
import threading

from utils.messages import Message
from utils.files import Files
from utils.parser import CodeParser

class AutoDoc:
    targetDir=""
    dType=""
    projectName=""

    def __init__(self,targetDir,dType,projectName):
        self.targetDir=targetDir
        self.dType=dType
        self.projectName=projectName

    def start_documentation(self):
        if(Files.dir_exists(self.targetDir)):
            
            DocumentationType.dirList=Files.listTargetDir(self.targetDir)

            if(self.dType=="all"):
                self.word=threading.Thread(target=DocumentationType.word,args=(self.targetDir,))
                self.markdown=threading.Thread(target=DocumentationType.markdown,args=(self.targetDir,))
                self.html=threading.Thread(target=DocumentationType.html,args=(self.targetDir,))

                self.word.start()
                self.markdown.start()
                self.html.start()

            elif(self.dType=="markdown"):
                self.markdown=threading.Thread(target=DocumentationType.markdown,args=(self.targetDir,))
                self.markdown.start()

            elif(self.dType=="word"):
                self.word=threading.Thread(target=DocumentationType.word,args=(self.targetDir,))
                self.word.start()

            elif(self.dType=="html"):
                self.html=threading.Thread(target=DocumentationType.html,args=(self.targetDir,))
                self.html.start()
            else:
                Message.error("Unkown documentation type: "+str(self.dType))
        else:
            Message.error(str(self.targetDir)+" is not a directory or does not exist")
    

class Logs:
    def allProjectsData(self):
        pass

    def particularProject(self):
        pass

    def successFullProjectBuilds(self):
        pass

    def failedProjectBuilds(self):
        pass

    def requestInput(self,message):
        pass




class DocumentationType:
    dirList=[]
    parsedData=[]
    word_state={"error":False,"message":"","dumpDir":"","fileIndex":0}
    html_state={"error":False,"message":"","dumpDir":"","fileIndex":0}
    mrkdown_state={"error":False,"message":"","dumpDir":"","fileIndex":0}

    @staticmethod
    def word(targetDir):
        Message.loading("Creating Auto_WordDocs")
        #Files.create_dir(targetDir+"/Auto_WordDocs")
        for item in DocumentationType.dirList:
            DocumentationType.word_state["fileIndex"]+=1
        print(DocumentationType.word_state["fileIndex"])

    @staticmethod
    def html(targetDir):
        from docHtml import Html

        Message.loading("Creating Auto_HtmlDocs")
        DocumentationType.html_state["dumpDir"]=targetDir+"/Auto_HtmlDocs"
        #Files.create_dir(targetDir+"/Auto_HtmlDocs")
        
        for item in DocumentationType.dirList:
            parsedData=DocumentationType.parseFile(item)
            filename=Files.getfileName(item)
            h=Html(filename,parsedData,DocumentationType.html_state["dumpDir"])
            
            documented=h.startDocumentation()

            DocumentationType.html_state["fileIndex"]+=1
        #print(DocumentationType.html_state["fileIndex"])
    
    @staticmethod
    def markdown(targetDir):
        from docMarkDown import MarkDown, MarkDownComponents
        Message.loading("Creating Auto_MarkDownDocs")
        #Files.create_dir(targetDir+"/Auto_MrkDownDocs")
        documented=""
        for item in DocumentationType.dirList:
            parsedData=DocumentationType.parseFile(item)
            filename=Files.getfileName(item)
            m=MarkDown(filename,parsedData)
            
            documented+=MarkDownComponents.italic(filename)
            documented+="\n"

            documented+=m.documentFile()
            
            DocumentationType.mrkdown_state["fileIndex"]+=1
        Files.write_file("test.md",documented)

        print(DocumentationType.mrkdown_state["fileIndex"])
    
    @staticmethod
    def parseFile(filepath):
        p=CodeParser()
        comments=p.parseStart(filepath)
        if(comments!=False):
            return comments
        else:
            Message.error("Could not parse file "+filepath)




if __name__=="__main__":
    arguments=sys.argv
    if(len(arguments)<2 or len(arguments)>5):
        print("Available commands are : document <documentation_type> <target_directory> <project_name>")
        print(":log <project_name>")
    else:
        #documenting entire source code
        if(arguments[1]=="document"):
            a=AutoDoc(targetDir=arguments[3],dType=arguments[2],projectName=arguments[4])
            a.start_documentation()

        #documenting single autoDoc Files
        elif(arguments[1]=="documentFile"):
            pass

        #logs
        elif(arguments[1]=="log"):
            print(arguments)
        else:
            print(arguments[1]+" is unknown")
            print("Available commands are : document <documentation_type> <target_directory> <project_name>")
            print(":log <project_name>")
