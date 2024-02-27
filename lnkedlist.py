class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertion_at_beg(self,data):
        new_node=ListNode(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_at_end(self,data):
        new_node=ListNode(data)
        
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return  # Key not found
        prev.next = current.nextt
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
            
            
        