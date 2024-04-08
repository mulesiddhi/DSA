"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40 
"""
from collections import defaultdict
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        
    def removeDups(self):
        if self.head==None:
            return
        prev=None
        curr=self.head
        seen=defaultdict(int)
        while curr!=None:
            if curr.data not in seen.keys():
                seen[curr.data]=1
                prev=curr
                curr=curr.next
            else:
                prev.next=curr.next
                curr=curr.next
        return self.head
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.append(3)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(1)
    ll.append(10)
    ll.printList()
    ll.removeDups()
    ll.printList()