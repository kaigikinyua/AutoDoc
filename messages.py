class Messages:
    @staticmethod
    def error(message):
        WARNING='\033[93m'
        print(f"{WARNING}Error: {message}")

    @staticmethod 
    def success(message):
        OKGREEN='\033[92m'
        print(f"{OKGREEN}Success: {message}")

    @staticmethod
    def message(message):
        print(f"{message}") 

class Log:
    #log messages to an error file
    #get project name, curr_time, and error message
    @staticmethod
    def log_error(message):
        pass 

    #current time, documentation verion and type of documentation and state
    @staticmethod
    def log_doc_versioning(doc_type):
        pass 
    