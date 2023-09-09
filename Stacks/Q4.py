# Reverse a string
from data_structures import ListStack


def reverse_words(msg: str) -> str:
    stack = ListStack()
    result = ''

    # loop till end of the string
    for letter in msg:
        # push every letter in the stack
        stack.push(letter)

    # pop the all letters from stack
    # and add to result till stack empty
    while not stack.isempty():
        result += stack.pop()

    return result


if __name__ == '__main__':
    string = input('Enter the message: ')
    print(reverse_words(string))
