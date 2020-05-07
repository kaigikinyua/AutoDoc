from messages import Message
from files import Files

class CodeParser:
    targetDir=""
    fileList=[]
    docDir=""
    error=False
    def __init__(self,targetDir):
        self.targetDir=targetDir
        self.fileList=Files.listTargetDir(targetDir)
        self.docDir=Files.create_dir(targetDir+"/autoDoc")
        self.languages=Files.load_json("./Configs/formats/languages.json")
        self.comments_delimeters=self.languages["languages"][0]["delimeters"]

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
        comments=[]
        for delimeter in self.comments_delimeters:
            #print(delimeter["start"])
            lineIndex=0
            for line in filedata:
                if delimeter["start"] in line:
                    comments+=[line]
                lineIndex+=1
        return comments

    def formated_comments(self,comments):
        refined_comments=[]
        for comment in comments:
            split_comment=comment.split(":")
            comment_start=""
            for char in split_comment[0]:
                if(char!="\t" and char!=" "):
                    comment_start+=char
            split_comment[0]=comment_start[1:len(comment_start)]
            refined_comments+=[split_comment]
        print(refined_comments)

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
        formats=Files.load_json("./Configs/formats/comments.json")
        pass

p=CodeParser("/home/antony/Pit/Projects/desktop/autoDoc/src/test")
p.parseStart()