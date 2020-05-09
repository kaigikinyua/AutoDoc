import os
import json
import shutil
from utils.messages import Message
#t:CRUD file operations
#p:Create,Read,Update/Append,Delete
class Files:
    def __init__(self):
        pass
    @staticmethod
    def listTargetDir(targetDir):
        if(Files.dir_exists(targetDir)):
            dirList=os.listdir(targetDir)
            fileList=[]
            for item in dirList:
                if(os.path.isfile(targetDir+"/"+item)):
                    fileList.append(targetDir+"/"+item)
                elif(os.path.isdir(targetDir+"/"+item)):
                    newFileList=Files.listTargetDir(targetDir+"/"+item)
                    for item in newFileList:
                        fileList.append(item)
                else:
                    pass
            return fileList
        else:
            return False

    @staticmethod
    def dir_exists(dir_path):
        if(os.path.isdir(dir_path)):
            return True
        else:
            Message.error("Directory "+dir_path+" does not exists")
            return False

    @staticmethod
    def create_dir(dir_path):
        if(Files.dir_exists(dir_path)):
            Message.error("Directory "+dir_path+" already exists")
            return False
        else:
            try:
                os.mkdir(dir_path)
                Message.success("Directory "+dir_path+" created")
                return dir_path
            except:
                Message.error("Could not create directory "+dir_path)
                return False


    @staticmethod
    def file_exists(file_path,error):
        if(os.path.isfile(file_path)):
            return True
        else:
            if(error==True):
                Message.error("File "+str(file_path)+" does not exist")
            return False

    @staticmethod
    def read_file(file_path):
        if(Files.file_exists(file_path,True)):
            f=open(file_path,'r')
            data=f.readlines()
            f.close()
            return data
        else:
            Message.error("Could not read file "+str(file_path))
            return False

    @staticmethod
    def write_file(file_path,data):
        try:
            f=open(file_path,"w")
            f.write(data)
            f.close()
            return True
        except:
            Message.error("Could not write to file "+str(file_path))
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
            Message.error("Could not append to file "+str(file_path))
            return False

    @staticmethod
    def copy_file(origin_path,destination_path):
        if(Files.file_exists(origin_path)):
            try:
                shutil.copy(origin_path,destination_path)
                Message.success("Copied file "+str(origin_path)+" to "+str(destination_path))
            except:
                Message.error("Could not copy file "+str(origin_path)+" to "+str(destination_path))
        else:
            Message.error("File "+str(origin_path)+" does not exist")

    @staticmethod
    def delete_file(file_path):
        if(Files.file_exists(file_path,True)):
            try:
                os.remove(file_path)
                return True
            except:
                Message.error("Could not delete file "+str(file_path))
                return False
        else:
            Message.error("Could not delete file "+str(file_path))
            return False

    @staticmethod
    def load_json(file_path):
        if(Files.file_exists(file_path,True)):
            with open(file_path,"r") as data:
                mydata=json.load(data)
                return mydata
            Message.error("Could not load JSON data")
            return False
        else:
            Message.error("File "+file_path+" does not exist")
            return False
