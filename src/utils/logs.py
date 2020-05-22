from .files import Files
class Log:
    @staticmethod
    def log_error(message):
        log_message="[error]"+str(message)
        if(Files.append_to_file("./Logs/logs.txt",log_message)):
            Messages.success("Log added")
        else:
            Messages.error("Could not add to logs")

    @staticmethod
    def log_new_project():
        pass


    @staticmethod
    def log_routine(message):
        log_message="[routine]"+str(message)
        if(Files.append_to_file("./Logs/logs.txt",log_message)):
            Messages.success("Log added")
        else:
            Messages.error("Could not add to logs")

    @staticmethod
    def log_doc_versioning(doc_type):
        pass 
    

class DataBase:
    @staticmethod
    def project_exists(projectName,projectPath):
        pass
    @staticmethod
    def add_project(projectName,projectPath):
        pass

    @staticmethod
    def getCurrentTime():
        pass
