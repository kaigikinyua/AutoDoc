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

    @check_error
    def parseStart(self):
        for item in self.fileList:
            print("Reading file"+str(item))
            data=Files.read_file(item)
            if(data!=False):
                pass

    def filter_comments(self,filepath,delimeter):
        pass

    def filter_text(self,filepath):
        pass

    def code_blue_print(self,fileComments):
        pass

    def filter_comments(self,filedata):
        pass 

    def code_segment(self):
        pass 

    def group_paragraph(self):
        pass
    
    def adjuscentDocs(self,targetDir):
        pass



    
class Code:
    def get_text_in_between(start,end):
        pass

    def get_commets():
        pass

    def formatComments():
        pass

    def formatCode():
        pass


c=CodeParser("./test")
c.parseStart()