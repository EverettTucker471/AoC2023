from Node import Node


class Stacker:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        self.head = Node(val, self.head)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Stacker is Empty")
        rtn = self.head.val
        self.head = self.head.next
        self.size -= 1
        return rtn

    def isEmpty(self):
        return self.size == 0

    def toString(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next
