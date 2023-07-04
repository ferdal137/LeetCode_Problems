class Stack:
    def __init__(self):
        self.Top = None
        self.Stack = []

    def GetTop(self):
        return self.Top

    def Add(self, Element):
        self.Top = Element
        self.Stack.append(Element)

    def Remove(self):
        self.Stack.pop()
        self.Top = self.Stack[-1]

    def __str__(self):
        return str(self.Stack)

    def __len__(self):
        return len(self.Stack)

MyStack = Stack()

MyStack.Add(1)
MyStack.Add(2)
MyStack.Add(3)
print(MyStack)

MyStack.Remove()
print(MyStack)
print(len(MyStack))