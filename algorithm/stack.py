class ArrStack:
    def __init__(self):
        self.arrayStack = []

    def isEmpty(self):
        return len(self.arrayStack) == 0

    def push(self, item):
        self.arrayStack.append(item)

    def top(self):
        top_item = None
        if not self.isEmpty():
            top_item = self.arrayStack[-1]
        return top_item

    def pop(self):
        if not self.isEmpty():
            top = self.top()
            del self.arrayStack[-1]
            return top


if __name__ == "__main__":
    # create stack1 and insert 1, 2, 7, 33
    stack1 = ArrStack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(7)
    stack1.push(33)
    # check the stack state
    print(stack1.arrayStack)  # [1, 2, 7, 33]

    # remove last item(because stack is FILO)
    print(stack1.pop())  # 33

    # check the stack state
    print(stack1.arrayStack)  # [1, 2, 7]
