class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, element):
        return self.storage.append(element)

    def dequeue(self):
        return self.storage.pop(0)

    def peak(self):
        return self.storage[0]
