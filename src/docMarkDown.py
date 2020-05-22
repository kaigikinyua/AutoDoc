from utils.files import Files
class MarkDown:
    def __init__(self,markDownFile,parsedData):
        self.markDownFile=markDownFile
        self.parsedData=parsedData
        self.configs=self.loadConfigs("./Configs/formats/comments.json")

    def loadConfigs(self,configsPath):
        return Files.load_json(configsPath)

    def documentFile(self):
        for elem in self.parsedData:
            self.documentElement(element)

    def documentElement(self,element):
        splitElement=element.split(":")
        return {
            "T":lambda: MarkDownComponents.title(splitElement[1],1),
            "sT":lambda: MarkDownComponents.title(splitElement[1],2),
            "P":lambda: MarkDownComponents.paragraph(splitElement[1]),
            "I":lambda: MarkDownComponents.image(splitElement[1]),
            "i":lambda: MarkDownComponents.italic(splitElement[1])
            #"L":lambda: MarkDownComponents.title(splitElement[1])
        }.get(splitElement[0],lambda: None)()

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
        return "![Screenshot]"+str(imagePath)

