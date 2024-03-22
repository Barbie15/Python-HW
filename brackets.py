def brackets(a):
    stack = []
    for i in a:
        if i == '(':
            stack.append(i)
        elif len(stack) != 0:
            stack.pop()
        else:
            return False

    return True if len(stack) == 0 else False


print(brackets(")"))