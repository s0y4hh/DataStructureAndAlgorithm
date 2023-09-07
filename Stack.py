def create_stack():
    return []

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(f"Pushed item: {item}")
def pop(stack):
    return stack.pop() if not is_empty(stack) else "Stack is empty"

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print(f"stack after pushing: {str(stack)}")
print(f"Popped item: {pop(stack)}")
print(f"stack after popping: {str(stack)}")

push(stack, str(5))

print(f"stack after pushing: {str(stack)}")
