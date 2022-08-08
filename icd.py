def isVerified(message):
    try:
        if message.startsWith("VERIFIED") and message.endsWith("END") and (message.find("WORD") == 30):

            SUCCESSFUL_MESSAGE_COUNT += 1
            return(True)

    except Exception as e:
        print(f"Message error: {e}")
        ERROR_MESSAGE_COUNT += 1
    return(False)

def icdParse(message): #parse işlemi tam değil
    message = "VERIFIED " + message
    
