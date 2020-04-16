import os

from messages import Messages
class Files:

    @staticmethod
    def file_exists(file_path):
        if(os.path.isfile(file_path)):
            return True
        else:
            Messages.error("File "+str(file_path)+" does not exist")
            return False

    @staticmethod
    def dir_exists(dir_path):
        if(os.path.isdir(dir_path)):
            return True
        else:
            Messages.error("Directory "+str(dir_path)+" does not exist")
            return False

    @staticmethod
    def read_file(file_path):
        if(Files.file_exists(file_path)):
            f=open(file_path,'r')
            data=f.readlines()
            f.close()
            return data
        else:
            Messages.error("Could not read file "+str(file_path))
            return False

    @staticmethod
    def write_file(file_path,data):
        try:
            f=open(file_path,"w")
            f.write(data)
            f.close()
            return True
        except:
            Messages.error("Could not write to file "+str(file_path))
            return False 

    @staticmethod
    def append_to_file(file_path,data):
        original_data=Files.read_file(file_path)
        if(original_data!=False):
            all_data=original_data+"\n"+data
            if(Files.write_file(file_path,data)):
                return True
            else:
                return False
        else:
            Messages.error("Could not append to file "+str(file_path))
            return False
