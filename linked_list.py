class Node :
    def __init__(self, data = None, next = None) :
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self) :
        self.head = None #points to head of linked list
    def insert_at_start(self, data) :
        node = Node(data, self.head) #once the node is created, the head will point to this node as it is in the beginning of the linked list
        self.head = node
    def insert_at_end(self,data) :
        #if linked list is blank
        if self.head is None :
            self.head = Node(data,None)
            return
        #if linked list is not blank
        iterator = self.head
        while iterator.next :
            iterator = iterator.next
        iterator.next = Node(data,None)
    def print(self) :
        if self.head is None :
            print("Empty linked list")
            return 
        llst = ''
        iterator = self.head
        while iterator :
            llst += str(iterator.data) + '->'
            iterator = iterator.next
        print(llst)
    def insert_list(self,array):
        self.head = None
        for data in array :
            self.insert_at_end(data)
if __name__ == "__main__" :
    ll = LinkedList()
    ll.insert_at_start(55)
    ll.insert_at_start(120)
    ll.insert_at_end(1113)
    ll.insert_at_end(12)
    ll.insert_list([1,2,4,6])
    ll.print()