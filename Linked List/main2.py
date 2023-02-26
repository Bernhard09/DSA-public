class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.__head = None
    

    def add(self, data) -> None:
        node = Node(data)

        if self.__head == None:
            self.__head = node
        else:
            node.next = self.__head
                

    def length(self) -> int:
        current_node = self.__head
        count = 0

        while(current_node != None):
            current_node = current_node.next
            count+=1
        
        return count

    def get_data(self):
        current_node = self.__head
        while(current_node != None):
            print(current_node.data)
            current_node = current_node.next
        






nodeA = LinkedList()
nodeA.add(3)

nodeA.get_data()


