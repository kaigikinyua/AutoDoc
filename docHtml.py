class Configs:
    links=""
    title=""
    def __init__(self):
        try:
            with open("index_spec.json","r") as j:
                config=json.load(j)
                self.links=config['links']
                self.title=config['title']
                Messages.success("Configs Loaded")
        except:
            Messages.error("Opening index_spec.json file")

class Components:
    theme="default"
    def __init__(self):
        pass

    #major components
    def navigation_links(self,link_title):
        pass 

    def code_segment(self,code):
        pass 

    def images(self,image_dir):
        pass 

    def title(self,title):
        pass

    def paragraph(self,text_paragraph):
        pass

    #layout
    def slider(self):
        pass 

    def contacts(self):
        pass 

    def sidenav(self):
        pass 

 