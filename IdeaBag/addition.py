# Addition of stack..

a=list()
class add:
    def __init__(self):
        self.stack=[]
        self.store=[]
        self.top=-1

    def push(self):
        if (self.top == -1):
            self.top = 0
            self.stack.append(int(input("input: ")))
            return
        else:

            self.stack.append(int(input("input: ")))
            self.top = self.top + 1
            return
    def pop(self):
        if (self.top == -1):
            print("Invalid operation!")
            return
        else:
            self.m = self.stack[self.top]
            print(self.m)
            self.top = self.top - 1
    