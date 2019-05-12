class JsonObject:
    # assumes the text is stored line by
    # line in a list, and only the text between
    # the braces is in the array
    def __init__(self):
        self.dataTable = {}

    def __getitem__(self,index):
        return self.dataTable[index]

    def __setitem__(self,index,value):
        self.dataTable[index] = value

    def keys(self):
        return dataTable.keys()

    def values(self5):
        return dataTable.values()
        

class JSONParser:
    def __init__(self,string):
        self.objects = []
        self.current = []
        self.pos = 0
        self.parse(string)

    def parse(self,string):
        length = len(string)
        while self.pos < length:
            if string[self.pos] == '{':
                self.objects.append(self.parseObject(string))
            else:
                self.pos += 1
        return self.objects

    def parseObject(self,string):
        self.current.insert(0,JsonObject)
        while string[self.pos] != '}':
            if string[self.pos] == '"':
                self.pos += 1
                self.parseKeyVal(string)
            else:
                self.pos += 1
        return self.current.pop(0)

    def parseKeyVal(self,string):
        key = ''
        while string[self.pos] != '"':
            key += string[self.pos]
            self.pos += 1
        self.pos += 1
        self.current[0][key] = self.parseVal(string)

    def parseVal(self,string):
        numerals = "1234567890."
        starts = '{["'
        None
