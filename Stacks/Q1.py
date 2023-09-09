# Parenthesis Matching
from data_structures import Stack


def parenthesis_checker(expr: str) -> bool:
    stack = Stack()

    for char in expr:
        # if bracket is opening bracket,
        # then push it to the stack
        if char in ['(', '[', '{']:
            stack.push(char)
        else:
            # if current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if stack.isempty():
                return False
            current_char = stack.pop().value
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack.isempty():
        return True
    return False


if __name__ == '__main__':
    exp = input('Enter bracket expression: ')
    print(parenthesis_checker(exp))
