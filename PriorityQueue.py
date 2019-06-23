class PriorityQueue:

    def __init__(self,element):
        self.queue = [element]

    def add(self,element):
        i = 0

        if self.isEmpty():
            self.queue = [element]
            return

        while i<len(self.queue) and element[1] > self.queue[i][1]:
            i += 1

        self.queue.insert(i,element)

    def pop(self):
        return self.queue.pop()[0]

    def contains(self,element):
        return element in self.queue

    def isEmpty(self):
        return len(self.queue) == 0

