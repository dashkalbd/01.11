# 1. Own Stack class
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        print(f"Done: {item}")

    def peek(self):
        if self.is_empty():
            print("History is empty")
            return None
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            print("Nothing to undo, history is empty")
            return None
        item = self.items.pop()
        print(f"Undone: {item}")
        return item

    def show(self):
        if self.is_empty():
            print("History is empty")
            return
        print("History (last to first):")
        for item in reversed(self.items):
            print(item)


history = Stack()

# 2. Add at least five operations
history.push("Added product «Keyboard»")
history.push("Changed price of «Mouse»")
history.push("Changed quantity of «Monitor»")
history.push("Deleted product «Headphones»")
history.push("Added product «Webcam»")

# 3. Show the last operation
print()
print("Last operation:", history.peek())

# 4. Undo the last two operations
print()
history.pop()
history.pop()

# 5. Show the remaining history
print()
history.show()
print("Records in history:", history.size())

# 6. Undo when the stack is empty
print()
history.pop()
history.pop()
history.pop()
history.pop()
history.show()


# Bonus: menu
def menu():
    stack = Stack()

    while True:
        print()
        print("1 - Add operation")
        print("2 - Show last operation")
        print("3 - Undo last operation")
        print("4 - Show number of records")
        print("5 - Show history")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            operation = input("Describe the operation: ")
            stack.push(operation)
        elif choice == "2":
            last = stack.peek()
            if last is not None:
                print("Last operation:", last)
        elif choice == "3":
            stack.pop()
        elif choice == "4":
            print("Records in history:", stack.size())
        elif choice == "5":
            stack.show()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Wrong choice, try again")


print()
print("Menu:")
menu()