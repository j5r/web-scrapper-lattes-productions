
def getJSON():
    f = open("./main_manager/configs.json","r")
    JSON = f.read()
    f.close()
    return JSON

