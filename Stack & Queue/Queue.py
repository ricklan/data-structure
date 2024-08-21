class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.insert(0, data)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        return None
    
    def print(self):
        for item in self.queue:
            print(item)

if(__name__ == "__main__"):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print()
    print(queue.dequeue())