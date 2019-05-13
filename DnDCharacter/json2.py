class Parser:
    def __init__(self,filename):
        self.pos = 0
        self.completed = []
        self.working = []
        self.text = ''
        self.setup(filename)

    def setup(self,filename):
        with open(filename) as file:
            for line in file:
                self.text += line

    def parse(self):
        length = len(self.text)
        while self.pos < length:
            if self.text[self.pos] == '{':
                self.pos += 1
                self.parseObject()
                self.completed.append(self.working.pop(0))
            else:
                self.pos += 1

    def parseObject(self):
        self.working.insert(0,{})
        while self.text[self.pos] != '}':
            if self.text[self.pos] == '"':
                self.pos += 1
                self.parseKeyVal()
            else:
                self.pos += 1

    def parseKeyVal(self):
        key = ''
        while self.text[self.pos] != '"':
            key += self.text[self.pos]
            self.pos += 1
        self.pos += 1
        #print(key)
        value = self.parseVal()
        self.working[0][key] = value

    def parseVal(self):
        num = '1234567890.'
        objs = '{["'
        while self.text[self.pos] not in (num + objs):
            self.pos += 1

        char = self.text[self.pos]
        if char in num:
            return self.parseNum()
        elif char == '{':
            self.pos += 1
            self.parseObject()
            self.pos += 1
            temp = self.working.pop(0)
            return temp
        elif char == '[':
            self.pos += 1
            return self.parseArray()
        elif char == '"':
            self.pos += 1
            return self.parseString()
        else:
            raise Exception("Big error:\n" + char)

    def parseNum(self):
        num = '1234567890.'
        strnum = ''
        while self.text[self.pos] in num:
            strnum += self.text[self.pos]
            self.pos += 1
        #self.pos += 1
        #print(strnum)
        if '.' in strnum:
            return float(strnum)
        return int(strnum)

    def parseString(self):
        string = ''
        while self.text[self.pos] != '"':
            string += self.text[self.pos]
            self.pos += 1
        self.pos += 1
        #print(string)
        return string

    def parseArray(self):
        num = '1234567890.'
        contents = []
        while self.text[self.pos] != ']':
            if self.text[self.pos] in num:
                contents.append(self.parseNum())
            elif self.text[self.pos] == '"':
                self.pos += 1
                contents.append(self.parseString())
            elif self.text[self.pos] == '[':
                self.pos += 1
                contents.append(self.parseArray())
            elif self.text[self.pos] == '{':
                self.pos += 1
                self.parseObject()
                self.pos += 1
                temp = self.working.pop(0)
                contents.append(temp)
            else:
                self.pos += 1
        #print(contents)
        return contents
        

def tests():
    a = Parser('testChar.json')
    a.text = '{"hello" : "friend"}'
    a.parse()
    b = Parser('testChar.json')
    b.text = '{"hello" : 12.31}'
    b.parse()
    c = Parser('testChar.json')
    c.text = '{"Hello" : "Friend", "I Hate" : 3.14}'
    c.parse()
    d = Parser('testChar.json')
    d.text = '{"Hello" : "Friend", "I Hate" : 3.14, "Second" : {"haha" : "killme"}, "123" : 123}'
    d.parse()
    print(a.completed)
    print(b.completed)
    print(c.completed)
    print(d.completed)

def test2():
    a = Parser('testChar.json')
    a.text = '{"hello" : ["hello","goodbye"]}'
    a.parse()
    print(a.completed)
        
        
        
