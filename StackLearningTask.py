"""
Part 1: PythonProgram File

Design a Python program that will implement a Stack Abstract Data Structure using Array. You can use one of the sample codes: ­StackArr.py as reference.

The program should determine the height of each stack and at which height the three stacks are equal.

Ask the user for the elements of each stack. The inputs are separated by space. Once enter key is pressed, the next prompt will be displayed accordingly.

If the stacks are not equal at a given height, prompt a message “Stack heights will never be equal”.

Success and Error messages should be displayed when necessary.

The program loops until user chooses not to continue, or N is pressed."""

def create_stack():
    return []
def push(stack,value):
    return stack.append(value)
def is_empty(stack):
    return stack == 0
def pop(stack):
    return stack.pop() if stack is not is_empty(stack) else "The stack is empty"
def user_input():
    stack_list = input("Enter element of a Stack: ")
    stack_list = stack_list.split(" ")
    return [int(num) for num in stack_list]
def equal_height(stack1,stack2,stack3):
    stack1sum = sum(stack1)
    stack2sum = sum(stack2)
    stack3sum = sum(stack3)
    index1,index2,index3 = 0,0,0
    while index1 < len(stack1) and index2 < len(stack2) and index3 < len(stack3):
        max_sum = max(stack1sum, stack2sum, stack3sum)
        if stack1sum == max_sum:
                stack1sum -= stack1[-1]
                index1 += 1
                pop(stack1)
        elif stack2sum == max_sum:
                stack2sum -= stack2[-1]
                index2 += 1
                pop(stack2)
        else:
                stack3sum -= stack3[-1]
                index3 += 1
                pop(stack3)
        if stack1sum == stack2sum == stack3sum:
            return stack1sum
def main():
    stack = create_stack()
    for i in user_input():
        push(stack,i)
    return stack
print(equal_height(main(),main(),main()))