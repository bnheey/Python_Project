class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class ArrLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def append(self, item):
        if self.head is None:
            self.count += 1
            self.head = item
        else:
            self.count += 1
            now = self.head
            while now.next:
                now = now.next
            now.next = item

    # can insert node in index idx
    def idxInsertNode(self, item, idx):
        now = self.head
        nowIdx = 0
        preNode = None

        # insert new node in index = 0
        if idx == 0:
            # there are something in linked list before
            if self.head:
                newNext = self.head
                self.head = item
                self.head.next = newNext
            # there are nothing in linked list before
            else:
                self.head = item

        # insert new node in index is not 0
        else:
            while nowIdx < idx:
                # if head point out something
                if now:
                    preNode = now
                    now = now.next
                # if head point out nothing
                else:
                    break
                nowIdx += 1

            if nowIdx == idx:
                item.next = now
                preNode.next = item
            else:
                return -1

    # can delete node in index idx
    def idxDeleteNode(self, idx):
        now = self.head
        newNext = self.head.next
        nowIdx = 0
        preNode = None

        if idx == 0:
            self.head = newNext
        else:
            while nowIdx < idx:
                if now.next:
                    preNode = now
                    now = newNext
                    newNext = newNext.next
                else:
                    break
                nowIdx += 1
            if nowIdx == idx:
                preNode.next = newNext
            else:
                return -1

    # find data and return the index
    def getDataIdx(self, data):
        now = self.head
        idx = 0

        while now:
            if now.data == data:
                return idx
            now = now.next
            idx += 1
        return -1

    # insert item in front of data
    def dataInsertNode(self, item, data):
        idx = self.getDataIdx(data)
        if 0 <= idx:
            self.idxInsertNode(item, idx)
        else:
            return -1

    # delete item the data
    def dataDeleteNode(self, data):
        idx = self.getDataIdx(data)
        if 0 <= idx:
            self.idxDeleteNode(idx)
        else:
            return -1

    # make the print format
    def print(self):
        now = self.head
        string = ""

        while now:
            string += str(now.data)
            if now.next:
                string += " => "
            now = now.next
        print(string)


if __name__ == "__main__":
    # create linked list and insert 1, 7, 3, 10, 20
    linkedList1 = ArrLinkedList()

    linkedList1.append(Node(1))
    linkedList1.append(Node(7))
    linkedList1.append(Node(3))
    linkedList1.append(Node(10))
    linkedList1.append(Node(20))
    linkedList1.print()  # 1 => 7 => 3 => 10 => 20

    # node what data == 100, insert in index == 3
    linkedList1.idxInsertNode(Node(100), 3)
    linkedList1.print()  # 1 => 7 => 3 => 100 => 10 => 20

    # delete the node where index == 2
    linkedList1.idxDeleteNode(2)
    linkedList1.print()  # 1 => 7 => 100 => 10 => 20

    # node what data == 27, insert in front of the node what data == 7
    linkedList1.dataInsertNode(Node(27), 7)
    linkedList1.print()  # 1 => 27 => 7 => 100 => 10 => 20

    # delete the node what data == 100 (if the same node is exist, first thing is delete)
    linkedList1.dataDeleteNode(100)
    linkedList1.print()  # 1 => 27 => 7 => 10 => 20
