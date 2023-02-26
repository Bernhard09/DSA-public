class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    @classmethod
    def length(cls, curr_node):
        count = 0
        while(curr_node != None):
            curr_node = curr_node.next
            count+=1
        return count

head = Node(4)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(10)
nodeE = Node(2)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

length = Node.length(head)

print(length)


