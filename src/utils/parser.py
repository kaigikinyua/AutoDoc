from utils.messages import Message
from utils.files import Files

#import re

class CodeParser:
    targetDir=""
    fileList=[]
    docDir=""
    error=False

    def __init__(self):
        #self.targetFile=targetFile
        #self.fileList=Files.listTargetDir(targetDir)
        #self.docDir=Files.create_dir(targetDir+"/autoDoc")
        self.languages=Files.load_json("./Configs/formats/languages.json")
        self.comments_delimeters=self.languages["languages"][0]["delimeters"]

        #if(self.docDir==False):
        #    self.error=True
    
    #decorators
    def check_error(original_function):
        def wrapper_function(self):
            if(self.error==True):
                Message.error("Could not continue with execution")
                return False
            else:
                return original_function(self)
        return wrapper_function
    #dec end

    def parseStart(self,filePath):
        Message.success("Reading file "+filePath+".....")
        data=Files.read_file(filePath)
        if(data!=False):
            comments=self.filter_comments(data)
            formatted_comments=self.formated_comments(comments)
            return comments
        else:
            Message.error("Could not parse file "+str(filePath))
            return False

    def filter_comments(self,filedata):
        comments=[]
        for delimeter in self.comments_delimeters:
            #print(delimeter["start"])
            lineIndex=0
            for line in filedata:
                if delimeter["start"] in line and delimeter["end"]==line[len(line)-1]:
                    comments+=[Code.get_text_in_between(delimeter["start"],delimeter["end"],line)]
                #finding the start delimeter and the last delimeter[multiple line comment]
                elif(delimeter["start"] in line and line[len(line)-1]=="\n"):
                    print("Multiple line comment")
                    multiple_comments=self.multiple_line_comment(lineIndex,filedata,delimeter["start"],delimeter["end"])
                    combined=""
                    for c in multiple_comments:
                        combined+=str("P:"+c[0])
                    comments+=[combined]
                lineIndex+=1
        return comments

    def formated_comments(self,comments):
        refined_comments=[]
        for comment in comments:
            try:
                split_comment=comment.split(":")
                comment_start=""
                for char in split_comment[0]:
                    if(char!="\t"):
                        comment_start+=char
                #split_comment[0]=comment_start[1:len(comment_start)]
                split_comment[0]=comment_start
                refined_comments+=[split_comment]
            except:
                refined_comments+=[comment]
        #print(refined_comments)
        return refined_comments

    def multiple_line_comment(self,lineIndex,filedata,start,end):
        #print(filedata[lineIndex])
        comment=[]
        while(lineIndex<len(filedata)):
            if end in filedata[lineIndex]:
                comment+=[lineIndex]
            elif filedata[lineIndex]!="\n":
                comment+=[filedata[lineIndex]]
            lineIndex+=1
        revised_comments=comment[1:len(comment)-1]
        revised_comments=self.formated_comments(revised_comments)
        return revised_comments

class Code:
    @staticmethod
    def get_text_in_between(start,end,line):
        lastChar=len(line)
        index=0
        for char in line:
            if(char==" " or char=="\t"):
                index+=1
            elif(char==start):
                break
            else:
                pass
        return line[index+1:lastChar-1]            

    @staticmethod
    def get_multiple_line_comments(start,end,lines):
        pass

#p=CodeParser("/home/antony/Pit/Projects/desktop/autoDoc/src/test")
#p.parseStart()