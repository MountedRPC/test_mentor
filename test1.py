class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def is_valid_brackets(string):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            if opening_brackets.index(stack.peek()) != closing_brackets.index(char):
                return False
            stack.pop()

    return stack.is_empty()


if __name__ == "__main__":
    test1 = "({[()()]})"
    test2 = "({[()]})"
    test3 = "({[()()]}"
    
    print(is_valid_brackets(test1))
    print(is_valid_brackets(test2))
    print(is_valid_brackets(test3)) 
