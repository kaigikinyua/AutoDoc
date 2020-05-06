class Html:
    def __init__(self):
        pass

    def loadConfigs(self):
        pass

    def documentFile(self,data):
        pass

    def create_page(self,pagename,pageData):
        pass


class HtmlComponents:

    #major components
    @staticmethod
    def navigation_links(self,link_title,link_to):
        return "<a href='"+str(link_to)+"'>"+link_title+"</a>" 

    @staticmethod
    def code_segment(self,code):
        return "<code>"+str(code)+"</code>" 

    @staticmethod
    def images(self,image_dir):
        return "<img src='"+str(image_dir)+"'/>" 

    @staticmethod
    def title(self,title):
        return "<h3 class='title'>"+str(title)+"</h3>"

    @staticmethod
    def paragraph(self,text_paragraph):
        return "<p>"+str(text_paragraph)+"</p>"

    @staticmethod
    def unorderdList(self,listdata):
        ul="<ul class='list'>"
        for item in listdata:
            ul+="/n"+"<li>"+item+"</li>"
        return ul+"/n"

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