class Queue:

    def __init__(self):
        self.items = []
    
    def __str__(self):
        return self.items

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append[item]

    def dequeue(self):
        if len(self.items) == 0:
            return "Cannot pop, queue is empty"
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            return "Cannot peek, queue is empty"
        
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            return "cannot read, queue is empty"
        
        return self.items[-1]
    
    def size(self):
        if len(self.items) == 0:
            return "cannot pop, queue is empty"
        
        return len(self.items)
    
    queue = Queue()
    

    