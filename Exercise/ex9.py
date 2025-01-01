class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty.")
            return None

    def display(self):
        print("Stack elements:", self.stack)


s = Stack()
s.push(1)
s.push(2)
s.pop()
s.display()
