import os

class Documentation:

    new_documentation=True
    doc_type=""
    doc_root_dir=""

    def __init__(self,*args, **kwargs):
        pass
    
    def check_existing_doc(self):
        pass 

    def new_word_document(self):
        pass

    def resume_documentation(self):
        pass

    def documentation_version(self):
        pass

class Comments:

    def filter_comments(self,filepath,delimeter):
        pass

    def filter_text(self,filepath):
        pass

    def comment_text(self,comments):
        pass 

    def code_blue_print(self,fileComments):
        pass
    
class CodeDoc:

    def read_code_file(self,path):
        pass

    def filter_comments(self,filedata):
        pass 

    def code_segment(self):
        pass 

    def group_paragraph(self):
        pass 
