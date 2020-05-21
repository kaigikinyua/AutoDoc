from utils.files import Files
class MarkDown:
    def __init__(self,markDownFile,parsedData):
        self.markDownFile=markDownFile
        self.parsedData=parsedData
        self.configs=self.loadConfigs("./Configs/formats/comments.json")

    def loadConfigs(self,configsPath):
        return Files.load_json(configsPath)

    def documentFile(self):
        for data in self.parsedData:
            #switch case
            if(data=="t"):
                pass
            elif data=="p":
                pass
            elif data=="i":
                pass
            elif data=="sT":
                pass
            elif data=="list":
                pass

class MarkDownComponents:
    
    @staticmethod
    def title(title,level):
        t="#"
        while(level>0):
            t+="#"
            level-=1
        return title+" "+level+"\n"

    @staticmethod
    def paragraph(text):
        return text+"/n"

    @staticmethod
    def unOrderedList(listData,listTitle):
        listD=""
        for item in listData:
            listD+="* "+item+"\n"
        return listD+"\n"

    @staticmethod
    def italic(text):
        return "*"+text+"*"

    @staticmethod
    def image(imagePath):
        pass

