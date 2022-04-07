class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        return self.stack.length == 0
    
    def peek(self):
        return self.stack[-1]
    
    def print(self):
        for item in self.stack:
            print(item)

if(__name__ == "__main__"):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()
    print(stack.pop())