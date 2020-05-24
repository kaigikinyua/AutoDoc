from utils.files import Files
from utils.messages import Message
class Html:
    def __init__(self,pagename,parsedData,targetDir):
        self.pagename=pagename
        self.parsedData=parsedData
        self.configs=self.loadConfigs("./Configs/formats/comments.json")

    def loadConfigs(self,configFilePath):
        return Files.load_json(configFilePath)

    def startDocumentation(self):
        formated_data=""
        for element in self.parsedData:
            formated_data+=self.documentElement(element)
        #print(formated_data)
        return formated_data
        
    def documentElement(self,element):
        split_element=element.split(":")
        return {
            "T":lambda:HtmlComponents.title(split_element[1]),
            "sT":lambda:HtmlComponents.subTitle(split_element[1]),
            "P":lambda:HtmlComponents.paragraph(split_element[1]),
            "I":lambda:HtmlComponents.images(split_element[1]),
            #"L":lambda:HtmlComponents.title(split_element[1]),
        }.get(split_element[0],lambda: None)()
        


class HtmlComponents:

    #major components
    @staticmethod
    def createPage(pageData,title):
        pre_html=HtmlComponents.pageTitle(title)
        post_html=Files.read_file("./Configs/html/postHtml.txt")
        if(pre_html!=False and post_html!=False):
            pass

    @staticmethod
    def pageTitle(title,predata):
        pre_html=Files.read_file("./Configs/html/preHtml.txt")
        line_index=0
        for line in pre_html:
            if("~" in line):
                line="<title>"+str(title)+"</title>"
            else:
                line_index+=1
        return pre_html


    @staticmethod
    def navigation_links(link_title,link_to):
        return "<a href='"+str(link_to)+"'>"+link_title+"</a>\n" 

    @staticmethod
    def code_segment(code):
        return "<code>"+str(code)+"</code>\n" 

    @staticmethod
    def images(image_dir):
        return "<img src='"+str(image_dir)+"'/>\n" 

    @staticmethod
    def title(title):
        print(title)
        return "<h3 class='title'>"+str(title)+"</h3>\n"

    @staticmethod
    def subTitle(subTitle):
        return "<h3 class='subtitle'>"+str(subTitle)+"</h3>"
    @staticmethod
    def paragraph(text_paragraph):
        return "<p>"+str(text_paragraph)+"</p>\n"

    @staticmethod
    def unorderdList(listdata):
        ul="<ul class='list'>"
        for item in listdata:
            ul+="/n"+"<li>"+item+"</li>"
        return ul+"/n"

    @staticmethod
    def italic(text):
        return "<i>"+text+"</i>"

    #layout
    """
    @staticmethod
    def slider(self):
        pass
     
    @staticmethod
    def contacts(self):
        pass 

    @staticmethod
    def sidenav(self):
        pass 

    """