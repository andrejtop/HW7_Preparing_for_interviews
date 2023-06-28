from prep_interviews import Stack


def balanced(string: str) -> str:
    stack = Stack()

    open_brackets = "([{"
    close_brackets = ")]}"

    for char in string:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return "Несбалансированно"
            else:
                top_char = stack.pop()
                if open_brackets.index(top_char) != close_brackets.index(char):
                    return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


print(balanced("(((([{}]))))"))