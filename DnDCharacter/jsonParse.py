class JsonObject:
    # assumes the text is stored line by
    # line in a list, and only the text between
    # the braces is in the array
    def __init__(self, jsonText):
        self.dataTable = {}
        self.parseText(jsonText)

    def __getitem__(self,index):
        return self.dataTable[index]

    def __setitem__(self,index,value):
        self.dataTable[index] = value

class JSONParser:
    def __init__(self,string):
        self.pos = 0
        self.parse(string)

    def parse(self,string):
        while self.pos < len(string):
            if string[self.pos] == '{':
                self.pos += 1
                self.parseObject(string)
# pretty sure this is actually useless
##            ignore = 0
##            notDone = True
##            while notDone: # this makes this loop skip nested objects
##                self.pos += 1
##                if string[self.pos] == '}' and ignore == 0:
##                    notDone = False
##                elif string[self.pos] == '{':
##                    ignore += 1
##                elif string[self.pos] == '}':
##                    ignore -= 1
##            self.pos += 1

    def parseObject(self,string):
        numerals = '1234567890'
        while string[self.pos] != '}':
            if string[self.pos] == '"':
                self.parseString(string)
            elif string[self.pos] == '[':
                self.parseList(string)
            elif string[self.pos] in numerals:
                self.parseNum

    def parseList(self,string):
        print("Parsing list")

    def parseString(self,string):
        print("Parsing string")

    def parseNum(self,string):
        print("Parsting Num")
