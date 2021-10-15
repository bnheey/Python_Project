class ArrQueue:
    def __init__(self):
        self.arrayQueue = []

    def isEmpty(self):
        return len(self.arrayQueue) == 0

    def enqueue(self, item):
        self.arrayQueue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            pop_item = self.arrayQueue[0]
            del self.arrayQueue[0]
            return pop_item


if __name__ == "__main__":
    # create stack1 and insert 1, 2, 3, 4
    queue1 = ArrQueue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    # check the stack state
    print(queue1.arrayQueue)  # [1, 2, 3, 4]

    # remove last item(because queue is FIFO)
    print(queue1.dequeue())  # 1

    # check the stack state
    print(queue1.arrayQueue)  # [2, 3, 4]
