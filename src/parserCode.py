from utils.messages import Message
from utils.files import Files

class CodeParser:
    targetDir=""
    fileList=[]
    docDir=""
    error=False
    def __init__(self,targetDir):
        self.targetDir=targetDir
        self.fileList=Files.listTargetDir(targetDir)
        self.docDir=Files.create_dir(targetDir+"/autoDoc")
        if(self.docDir==False):
            self.error=True
    
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

    def parseStart(self):
        for item in self.fileList:
            Message.success("Reading file "+item+".....")
            data=Files.read_file(item)
            if(data!=False):
                comments=self.filter_comments(data)
                formatted_comments=self.formated_comments(comments)
            else:
                print(data)

    def filter_comments(self,filedata):
        languages=Files.load_json("./Configs/formats/languages.json")
        comments_delimeters=languages["languages"][0]["delimeters"]
        comments=[]
        for delimeter in comments_delimeters:
            print(delimeter["start"])
            lineIndex=0
            for line in filedata:
                for char in line:
                    if(char==delimeter["start"] and line[len(line)-1]!=delimeter["end"]):
                        comment=Code.get_text_in_between(delimeter["start"],delimeter["end"],line)
                        comments.append(comment)
                
                
        return comments

    def formated_comments(self,comments):
        for comment in comments:
            split_comment=comment.split(":")
            print(split_comment)

    def code_blue_print(self,fileComments):
        pass

    def code_segment(self):
        pass 

    def group_paragraph(self):
        pass
    
    def adjuscentDocs(self,targetDir):
        pass


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

    def formatComments():
        pass

    def formatCode():
        pass

class AutoDocParser:
    pass

c=CodeParser("./test")
c.parseStart()