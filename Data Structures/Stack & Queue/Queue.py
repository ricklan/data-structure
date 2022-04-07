class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return self.queue.length == 0
    
    def peek(self):
        return self.queue[0]
    
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