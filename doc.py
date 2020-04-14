import os

class Documentation:
    new_documentation=True
    doc_type=""
    code_root_dir=""
    target_root_dir=""

    def __init__(self,*args, **kwargs):
        doc_type=kwargs['doc_type']
        code_root_dir=kwargs['code_root_dir']
        target_root_dir=kwargs['target_root_dir']
        print(kwargs)
    
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

    def read_code_file(self,path):
        pass

    def filter_comments(self,filedata):
        pass 

    def code_segment(self):
        pass 

    def group_paragraph(self):
        pass 

#D=Documentation(doc_type="Full",code_root_dir="/home/antony",target_root_dir="./home")