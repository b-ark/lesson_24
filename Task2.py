# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."
class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


def balanced(sequence: str):
    counter = {
        '(': 0,
        ')': 0,
        '[': 0,
        ']': 0,
        '{': 0,
        '}': 0,
    }
    temp = Stack()
    for symbol in sequence:
        temp.push(symbol)
    while not temp.is_empty():
        check = temp.pop()
        if check in counter:
            counter[check] += 1
    massage('(', ')', counter)
    massage('{', '}', counter)
    massage('[', ']', counter)


def massage(par1, par2, counter_):
    if counter_[par1] == counter_[par2]:
        print(f'\'{par1}\' and \'{par2}\' are balanced')
    else:
        print(f'\'{par1}\' and \'{par2}\' are not balanced')


if __name__ == "__main__":
    balanced('(([]{{}}')
