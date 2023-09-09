# Reverse word in string
from data_structures import ListStack


def reverse_words(msg: str) -> str:
    stack = ListStack()
    result = ''

    # loop till end of the string
    for letter in msg:
        # push every letter in the stack till space
        if not letter.isspace():
            stack.push(letter)
        else:
            # pop the all letters from stack
            # and add to result when current
            # letter is space
            while not stack.isempty():
                result += stack.pop()
            # add space at every reverse word
            result += ' '

    # add last reversed word to list
    while not stack.isempty():
        result += stack.pop()

    return result


if __name__ == '__main__':
    string = input('Enter the message: ')
    print(reverse_words(string))
