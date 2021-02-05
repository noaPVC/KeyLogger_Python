

def getChars(path):
    file = open(path, "r")
    data = file.read()
    number_of_characters = len(data)
    return number_of_characters


def deleteContentFile(path):
    file = open(path, "r+")
    file. truncate(0)
    file. close()


def deleteLast(path):
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(0, len(lines)):
        if i == (len(lines)-1):
            lines[i] = str(lines[i])[:-1]
    file = open(path, 'w')
    file.writelines(lines)
