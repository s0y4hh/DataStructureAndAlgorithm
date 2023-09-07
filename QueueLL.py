# queue implementation using linked list
class Node:
    """Node class
    """
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
        
# a linked list class with a single head node

class QueueLL:
    def __init__(self):
        self.head = None
        # insert at the tail of the linked list
    def enqueue(self,data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else: # for the first element/head
            self.head = new_node
    # delete an element from the head of the linked list
    def dequeue(self):
        temp = self.head
        if temp is not None:
            element = temp.data
            self.head = temp.next
            temp = None
            return element
    # display an element from the tail of the linked list
    def peek(self):
        if self.head:
            current = self.head
            while current.next:
                current =current.next
            return current.data
    # print method for the linked list
    def printLL(self):
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next

# A queue implemented using a linked list
Queue = QueueLL()
# enqueue2
Queue.enqueue(2)
# display element at the tail
print(f"Element at the tail: {Queue.peek()}")
# enqueue3
Queue.enqueue(3)
# display the element at the tail
print(f"Element at the tail: {Queue.peek()}")
# enqueue4
Queue.enqueue(4)
# display the element at the tail
print(f"Element at the tail: {Queue.peek()}")
# enqueue 5
Queue.enqueue(5)
# display the element at the tail
print(f"Element at the tail: {Queue.peek()}")
# display the queue
print(f"Current Queue:", end= " ")
Queue.printLL()

print(f"\nElement Dequeued: {Queue.dequeue()}")
print(f"Element Dequeued: {Queue.dequeue()}")

# Display the queue
print(f"Current Queue: ", end = "")
Queue.printLL()