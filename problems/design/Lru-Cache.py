
class Node:
    def __init__(self,value,key,next=None, prev = None):
        self.value =value
        self.key =key
        self.next = next
        self.prev = prev
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head =Node(-1,-1)
        self.tail =Node(-1,-1)
        self.index ={}
        

    def get(self, key: int) -> int:
        if key  not in self.index:return -1
        self.move_front(self.index[key])
        return self.index[key].value

    def put(self, key: int, value: int) -> None:
        
        if key in self.index:
            self.index[key].value=value
            self.move_front(self.index[key])
            return 
        newNode = Node(value,key)
        if len(self.index)+1 > self.capacity:
            del self.index[self.tail.prev.key]
            self.delete(self.tail.prev)
        self.index[key] =newNode
        self.insert(newNode)
    
    def insert(self,node):
        if self.head.next is None: 
            self.head.next = node
            node.prev = self.head
            self.tail.prev= node
            node.next =self.tail
            return
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def delete(self, node):
        node.prev.next= node.next
        if node.next is not None:
            node.next.prev = node.prev
            
    def move_front(self,node):
        self.delete(node)
        self.insert(node)




        


