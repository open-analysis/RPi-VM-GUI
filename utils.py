def getAttributes(listName):
    names = [i[0] for i in listName]
    images = [i[1] for i in listName]
    cmds = [i[2] for i in listName]

    return [names, images, cmds]