import os


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        if self.is_empty():
            return 0
        temp = self.head
        total = 0
        while temp != None:
            temp = temp.next
            total += 1
        return total
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Insert Successfully")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return "Data inserted at head instead"
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return "Data inserted successfully at the tail"

    def insert_at_mid(self, data, position):
        if position == 0:
            return self.insert_at_start(data)
        if position < 0 or position > self.size():
            print("Index out of range")
            return
        new_node = Node(data)
        ptr = None
        temp = self.head
        count = 0
        while count < position - 1:
            ptr = temp
            temp = temp.next
            count += 1
        new_node.next = temp
        ptr.next = new_node
    def delete_at_start(self):
        if self.is_empty():
            return "There's nothing to delete"
        self.head = self.head.next
        return "Delete at start successfully"

    def delete_at_mid(self, position):
        if self.is_empty():
            return "There's Nothing to delete"
        count = 0
        temp = self.head
        while count < position - 1:
            temp = temp.next
            count += 1
        ptr = temp.next
        ptr2 = ptr.next
        temp.next = ptr2

    def delete_at_end(self):
        # Check if the list is empty
        if self.size() == 0:
            print("The list is empty. Nothing to delete.")
            return

        # If there's only one element in the list, delete it directly
        if self.size() == 1:
            self.head = None
            self.tail = None
            print("Deleted the only element in the list.")
            return

        # Traverse the list to find the second-to-last node
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        # Update the tail node to be the second-to-last node, and set its next pointer to None
        self.tail = temp
        self.tail.next = None
        print("Last element deleted successfully!")

    def delete_number(self, value):
        if self.is_empty():
            return "The list is empty"

        if self.head.data == value:
            self.head = self.head.next
            return f"Deleted {value} from the list"
        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next
        if current.next is None:
            return f"{value} not found in the list"

        current.next = current.next.next
        return f"Deleted {value} from the list"

    def display(self):
        if self.is_empty():
            return "The list is empty"
        temp = self.head
        while temp is not None:
            if temp is self.head:
                print(f"[HEAD] --> [{temp.data}]", end=' ==> ')
            elif temp.next is None:
                print(f"[{temp.data}] --> [TAIL]", end = '')
            else:
                print(f"[{temp.data}]",end=' ==> ')
            temp = temp.next
    def search(self, value):
        if self.is_empty():
            return "The list is empty"
        temp = self.head
        count = 0
        while temp.data != value:
            temp = temp.next
            count += 1
            if temp == None:
                return f"There's no {value} in the list"
        return f"Found {value} at index {count}"

    def display_num_position(self, index):
        if self.is_empty():
            return "The list is empty!!"
        temp = self.head
        count = 0
        while temp is not None:
            if count == index:
                return temp.data
            temp = temp.next
            count += 1
        return "Index out of range"


ll = LinkedList()


def input_num():
    return int(input("Enter a number: "))


def main():
    while 1:
        try:
            choice = int(input(""" 
            - - - - - MENU - - - - - 

            [0] EXIT
            [1] INSERT AT START
            [2] INSERT AT END
            [3] INSERT AT POSITION
            [4] DELETE AT START
            [5] DELETE AT END
            [6] DELETE AT POSITION
            [7] DELETE NUMBER
            [8] SEARCH NUMBER
            [9] DISPLAY NUMBER AT POSITION
            [10] DISPLAY LIST: """))
            break
        except ValueError:
            print("\n\t\t\tPlease input integer only")
    match choice:
        case 0:
            while 1:
                yesorno = input("Are you sure you want to exit? y/n").upper()
                if yesorno == "Y":
                    print("THANK YOU FOR USING THIS PROGRAM")
                    os.system(exit())
                elif yesorno == "N":
                    main()
        case 1:
            ll.insert_at_start(input_num())
            print("Insert at start successfully")
            print(ll.size())
        case 2:
            ll.insert_at_end(input_num())
            print("Insert at end successfully")
        case 3:
            ll.insert_at_mid(input_num(), int(input("Enter position: ")))
        case 4:
            ll.delete_at_start()
            print("Delete at start successfully")
        case 5:
            ll.delete_at_end()
        case 6:
            if ll.size() == 0:
                print("The linked list is empty")
                main()
            ll.delete_at_mid(int(input("Enter position: ")))
        case 7:
            ll.delete_number(input_num())
            print("Delete number successfully")
        case 8:
            print(ll.search(input_num()))
        case 9:
            print(ll.display_num_position(int(input("Enter position: "))))
        case 10:
            ll.display()
    main()
main()