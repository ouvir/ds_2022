from LinkedStack import LinkedStack

def parenBalance(s)->bool:
    stack = []
    for word in s:
        if word=="(":
            stack.append(word)
        elif word==")":
            stack.pop() 
    return not bool(stack)


a = "(())"
b = "((())"
print(parenBalance(a))
print(parenBalance(b))