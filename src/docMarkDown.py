class MarkDown:
    def __init__(self):
        pass

    def loadConfigs(self):
        pass

    def documentFile(self):
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
        return listD

    @staticmethod
    def italic(text):
        return "*"+text+"*"
        
    @staticmethod
    def image(imagePath):
        pass

