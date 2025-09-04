stack = []

def push(item):
    stack.append(item)

def pop():
    if not is_empty():
        return stack.pop()
    else:
        return "Stack is empty!"

def peek():
    if not is_empty():
        return stack[-1]
    else:
        return "Stack is empty!"

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

push()
push()
push()
print("Top of stack:", peek())
print("Stack size:", size())
print("Popped:", pop())
print("Popped:", pop())
print("Is stack empty?", is_empty())
print("Popped:", pop())
print("Popped:", pop())