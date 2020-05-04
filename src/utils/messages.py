
class Message:    
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

    @staticmethod
    def loading(message,waiting):
        animation=['|','/','--','\']
        i=0
        while waiting:
            print(f"{message} ..... {animation[i]}")
            if(i==len(animation)-1):
                i=0
