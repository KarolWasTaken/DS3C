import json, variables

class JSON(object):
    def writeToJSONFile(path, fileName, data):
        try:
            filePathNameWExt = path + '/' + fileName + '.json'     # for saving the data
            with open(filePathNameWExt, 'w') as fp:
                json.dump(data, fp)
                variables.path = path
        except:
            filePathNameWExt = "./" + fileName + '.json'     # incase 'path' messses up
            with open(filePathNameWExt, 'w') as fp:
                json.dump(data, fp)
                variables.path = "./"