import time
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
    def loading(message):
        animation=['|','/','-','|','\\']
        i=0
        while True:
            print(str(message)+"....."+animation[i],end="\r")
            i+=1
            if(i==len(animation)-1):
                i=0
            time.sleep(0.4)

