from files import Files

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
    @staticmethod
    def log_error(message):
        log_message="[error]"+str(message)
        if(Files.append_to_file("./Logs/logs.txt",log_message)):
            Messages.success("Log added")
        else:
            Messages.error("Could not add to logs")

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
    