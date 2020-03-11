
def getJSON():
    f = open("./main_manager/configs.json","rb")
    JSON = f.read()
    f.close()
    return JSON

