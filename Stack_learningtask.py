"""
JAYSON ASIADO BSCS 2A
"""
import os
from colorama import Fore,Style
def create_stack(): # I create an empty stack that I can use to push and pop elements   
    return []

def push(stack,value): # this is the push function that I can use to add elements to the stack
    return stack.append(value)  # apped the value to the last index of the stack

def is_empty(stack): # Function for cheking if the stack is empty
    return stack == 0 # return true if the stack is equal to 0

def pop(stack):# pop function is to remove the last element of the stack
    return stack.pop() if stack is not is_empty(stack) else "The stack is empty" # just pop the last element of the stack if the stack is not empty

def user_input(): # this function is for getting the user input
    stack = create_stack() # create a stack
    for i in range(1,4): # loop 3 times to get the elements of the stack
        # I used the map function to convert the input to integer and split the input by space
        # push every element to the stack by using the push function and strip white spaces in the input
        push(stack,(list(map(int,input(f"Enter the elements of the stack {i}: ").strip().split()))))
    print(f"\nStack 1 total height: {sum(stack[0])}\nStack 2 total height: {sum(stack[1])}\nStack 3 total height: {sum(stack[2])}")
    return stack # return the stack

def equal_height(stack1,stack2,stack3): # this function is for checking if the stacks are going to be equal after popping elements
    # I used the sum function to get the sum of the elements of the stack
    stack1sum = sum(stack1)
    stack2sum = sum(stack2)
    stack3sum = sum(stack3)

    while 1: # I used the while loop and pop an item for every iteration in the maximum sum of the stacks
        if stack1sum == 0 or stack2sum == 0 or stack3sum == 0: # if the sum of the stacks is equal to 0 then return the stack willl never be equal
            return print("\nStack heights will never be equal.")
        if stack1sum == stack2sum == stack3sum: # This is to check if the stacks are equal then return any of the sum
            return print(Fore.GREEN+f"""\n All stacks are equal at height: {stack1sum}
        Stack 1: {' '.join(map(str,stack1[::-1]))}
        Stack 2: {' '.join(map(str,stack2[::-1]))}
        Stack 3: {' '.join(map(str,stack3[::-1]))}"""+Style.RESET_ALL)# print the reverse of the remaining stack
        
        max_sum = max(stack1sum,stack2sum,stack3sum) # get the maximum sum of the stacks

        if stack1sum == max_sum: # if the stack1sum is equal to the maximum sum and the index is less than the length of the stack
            stack1sum -= stack1[-1] # subtract the last element of the stack to the stack1sum
            pop(stack1) # pop the last element of the stack
            # JUST LIKE THE STACK1 I DID THE SAME THING TO THE STACK2 AND STACK3
        elif stack2sum == max_sum:
            stack2sum -= stack2[-1]
            pop(stack2)
        else:
            stack3sum -= stack3[-1]
            pop(stack3)
        # if the stacks are not equal after removing elements 1 by 1 then return this message

def main():
    stack_input = user_input() # store the user input to the variable stack
    equal_height(stack_input[0],stack_input[1],stack_input[2]) # call the equal_height function and pass the 3 stacks as arguments
main() # call the main function
while 1: # loop until the user choose not to continue
    choice = input("\nContinue? Y or N?: ").upper() # ask the user if he/she wants to continue
    if choice == "Y": # if the user choose to continue then ask for the user input again
        os.system('clear') # clear the screen
        main() # call the main function again
    elif choice == "N":
        print(Fore.YELLOW+"\nThank you for using the program."+Style.RESET_ALL)# if the user choose not to continue then exit the program
        exit()
    else: # if the user input is not Y or N then ask again
        print(Fore.RED+"\nInvalid input"+Style.RESET_ALL)