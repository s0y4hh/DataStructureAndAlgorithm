"""
Part 1: PythonProgram File

Design a Python program that will implement a Stack Abstract Data Structure using Array. You can use one of the sample codes: ­StackArr.py as reference.

The program should determine the height of each stack and at which height the three stacks are equal.

Ask the user for the elements of each stack. The inputs are separated by space. Once enter key is pressed, the next prompt will be displayed accordingly.

If the stacks are not equal at a given height, prompt a message “Stack heights will never be equal”.

Success and Error messages should be displayed when necessary.

The program loops until user chooses not to continue, or N is pressed."""

"""
JAYSON ASIADO BSCS 2A
"""
def create_stack(): # I create an empty stack that I can use to push and pop elements   
    return []

def push(stack,value): # this is the push function that I can use to add elements to the stack
    return stack.append(value)  # apped the value to the last index of the stack

def is_empty(stack): # Function for cheking if the stack is empty
    return stack == 0 # return true if the stack is equal to 0

def pop(stack):# pop function is to remove the last element of the stack
    return stack.pop() if stack is not is_empty(stack) else "The stack is empty" # just pop the last element of the stack if the stack is not empty


def user_input(): # this function is for the user to input the elements of the stack and return the stack
    stack_list = input("Enter element of a Stack: ").strip() # ask the user to input the elements of the stack 
                                                            #and remove whitespaces from left and right to reduce errors
    stack_list = stack_list.split(" ")
    return [int(num) for num in stack_list] # return the stack after converting each element to integer

stack = create_stack() # create a stack by storing an empty list to the variable stack

def equal_height(stack1,stack2,stack3): # this function is for checking if the stacks are going to be equal after popping elements
    # I used the sum function to get the sum of the elements of the stack
    stack1sum = sum(stack1)
    stack2sum = sum(stack2)
    stack3sum = sum(stack3)
    # I used the index to keep track of the elements that I popped
    index1,index2,index3 = 0,0,0

    while 1: # I used the while loop and pop an item for every iteration in the maximum sum of the stacks
        if stack1sum == stack2sum == stack3sum: # This is to check if the stacks are equal then return any of the sum
            return stack1sum
        max_sum = max(stack1sum,stack2sum,stack3sum) # get the maximum sum of the stacks

        if stack1sum == max_sum and index1 < len(stack1): # if the stack1sum is equal to the maximum sum and the index is less than the length of the stack
            stack1sum -= stack1[-1] # subtract the last element of the stack to the stack1sum
            index1 += 1 # increment the index
            pop(stack1) # pop the last element of the stack
            # JUST LIKE THE STACK1 I DID THE SAME THING TO THE STACK2 AND STACK3
        elif stack2sum == max_sum and index2 < len(stack2):
            stack2sum -= stack2[-1]
            index2 += 1
            pop(stack2)
        elif stack3sum == max_sum and index3 < len(stack3):
            stack3sum -= stack3[-1]
            index3 += 1
            pop(stack3)
        else:
            return "Stack heights will never be equal" # if the stacks are not equal after removing elements 1 by 1 then return this message
print(equal_height(user_input(),user_input(),user_input())) # print the result of the function equal_height with the user_input as the arguments