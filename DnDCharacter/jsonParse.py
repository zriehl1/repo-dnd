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

class JSONParser:
    def __init__(self,string):
        self.objects = []
        self.current = None
        self.pos = 0
        self.parse(string)

    def parse(self,string):
        length = len(string)
        while self.pos < length:
            if string[self.pos] == '{':
                self.current = JsonObject()
                self.pos += 1
                self.parseObject(string)
                self.objects.append(self.current)
                self.current = None
            else:
                self.pos += 1

    def parseObject(self,string):
        while string[self.pos] != '}':
            if string[self.pos] == '"':
                self.parseKey(string)
                self.pos += 1
            else:
                self.pos += 1

    def parseKey(self,string):
        key = ''
        while string[self.pos] != '"':
            key += string[self.pos]
            self.pos += 1
        self.current[key] = None
        self.parseValue(string,key)

    def parseValue(self,string,key): # a value can be a JsonObject {}, a list [], a string "", or a number 99
        numerals = "1234567890"
        reserved = '{["'
        errors = '}]'
        while string[self.pos] not in numerals or string[self.pos] not in reserved:
            if string[self.pos] in errors:
                raise Exception("Invalid JSON formatting")
            self.pos += 1
        if string[self.pos] in numerals:
            self.current[key] = self.parseNumber(string)
        elif string[self.pos] == '"':
            self.current[key] = self.parseString(string)
        elif string[self.pos] == '{':
            raise Exception("This doesn't work yet, sorry")
        elif string[self.pos] == '[':
            self.current[key] = self.parseList(string)

    def parseNumber(self,string):
        None

    def parseString(self,string):
        None

    def parseList(self,string):
        None

    def parseNestedObj(self,string):
        None
