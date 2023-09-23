"""JAYSON ASIADO BSCS 2A"""
from os import system as sys
from colorama import Fore,Style
red = Fore.RED
rst = Style.RESET_ALL
grn = Fore.LIGHTGREEN_EX
class Node:
    """Node class
    """
    def __init__(self,data):
        self.data = data
        self.next = None
        
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
    def printLL(self):
        if self.head is None:
            return "Empty"
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return " ".join(map(str, result))

    def sum(self):
        sum = 0
        current = self.head
        while current:
            sum += current.data
            current = current.next
        return sum

def user_input():
    while 1:
        try:
            num = int(input(grn+"Enter Workload: "+rst))
            return num
        except ValueError:
            print(red+"Invalid Input Try Again!!"+rst)
            
def main():
    sys('clear')
    queue_1 = QueueLL()
    queue_2 = QueueLL()
    queue_3 = QueueLL()
    while 1:

        enqueue_min = min(queue_1.sum(), queue_2.sum(), queue_3.sum())
        head_1 = queue_1.head.data if queue_1.head is not None else float('inf')
        head_2 = queue_2.head.data if queue_2.head is not None else float('inf')
        head_3 = queue_3.head.data if queue_3.head is not None else float('inf')
        dequeue_min = min(head_1, head_2, head_3)
        print(f"""________________________________
Queue 1: {queue_1.printLL()}
Queue 2: {queue_2.printLL()}
Queue 3: {queue_3.printLL()}  
________________________________""")
        while 1:
            try:
                choice = int(input("""[0] Exit
[1] Enqueue Workload
[2] Dequeue Worload
Choice: """))
                if choice < 0 or choice > 2:
                    print(red+"\nInvalid Input Try Again!!\n"+rst)
                    continue
                break
            except ValueError:
                print(red+"\nInvalid Input Try Again!!\n"+rst)
        match choice:
            case 0:
                print("Thank you!")
                exit()
            case 1:
                data = user_input()
                if enqueue_min == queue_1.sum():
                    queue_1.enqueue(data)
                elif enqueue_min == queue_2.sum():
                    queue_2.enqueue(data)
                elif enqueue_min == queue_3.sum():
                    queue_3.enqueue(data)
            case 2:
                if dequeue_min == float('inf'):
                    print(red+"\nQueue Underflow\n"+rst)
                elif dequeue_min == head_1:
                    queue_1.dequeue()
                elif dequeue_min == head_2:
                    queue_2.dequeue()
                else:
                    queue_3.dequeue()
            
                
if __name__ == "__main__":
    main()