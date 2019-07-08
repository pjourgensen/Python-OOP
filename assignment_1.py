

class MaxSizeList(object):
    def __init__(self,MaxSize):
        self.MaxSize = MaxSize
        self.MyList = []

    def push(self,strin):
        self.MyList.append(strin)
        if len(self.MyList) > self.MaxSize:
            self.MyList.pop(0)

    def get_list(self):
        return self.MyList


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
