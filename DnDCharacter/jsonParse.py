class JsonObject:
    # assumes the text is stored line by
    # line in a list, and only the text between
    # the braces is in the array
    def __init__(self, jsonText):
        self.dataTable = {}
        self.parseText(jsonText)

    def parseText(self, text):
        None
            
            
        
    def getKey(self, key):
        return self.dataTable[key]
