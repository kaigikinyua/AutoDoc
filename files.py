import os

from messages import Messages
#CRUD file operations
class Files:
    #sub: Directory methods
    @staticmethod
    def dir_exists(dir_path):
        if(os.path.isdir(dir_path)):
            return True
        else:
            Messages.error("Directory "+str(dir_path)+" does not exist")
            return False

    @staticmethod
    def create_dir(dir_path):
        if(Files.dir_exists(dir_path)):
            Messages.error("Directory already exists")
        else:
            Messages.error("Created dir method in Files has to be updated")

    #endsub
    #sub: File methods
    #func:file_path-> Path to file, error->{Boolean Values: if true display error if any else hide error}
    @staticmethod
    def file_exists(file_path,error):
        if(os.path.isfile(file_path)):
            return True
        else:
            if(error==True):
                Messages.error("File "+str(file_path)+" does not exist")
            return False

    @staticmethod
    def read_file(file_path):
        if(Files.file_exists(file_path,True)):
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

    @staticmethod
    def delete_file(file_path):
        if(Files.file_exists(file_path,True)):
            try:
                os.remove(file_path)
                return True
            except:
                Messages.error("Could not delete file "+str(file_path))
                return False
        else:
            Messages.error("Could not delete file "+str(file_path))
            return False
    #endsub

    @staticmethod
    def load_json(file_path):
        if(Files.file_exists(file_path)):
            try:
                with open(file_path,"r") as data:
                    mydata=json.load(data)
                    return mydata
            except:
                Messages.error("Could not load JSON data")
                return False
        else:
            Messages.error("File "+file_path+" does not exist")
            return False