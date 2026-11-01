from datetime import datetime


# Node = one version of the document
class VersionNode:
    def __init__(self, version_id, text, description):
        self.version_id = version_id
        self.text = text
        self.changed_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.description = description
        # links to neighbours (required: prev and next)
        self.prev = None
        self.next = None

    def __str__(self):
        return (f"Version {self.version_id} | {self.changed_at} | {self.description}\n"
                f"   Text: {self.text}")


class DocumentHistory:
    def __init__(self):
        # no built-in list: only links to nodes
        self.head = None
        self.tail = None
        self.current = None
        self.next_id = 1

    def is_empty(self):
        return self.head is None

    # 1. Add a new version at the end
    def add_version(self, text, description):
        node = VersionNode(self.next_id, text, description)
        self.next_id = self.next_id + 1

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.current = node
        print(f"Added version {node.version_id}")

    # 2. Show the current version
    def show_current(self):
        if self.current is None:
            print("History is empty")
            return
        print("Current version:")
        print(self.current)

    # 3. Go to the previous version
    def go_back(self):
        if self.current is None:
            print("History is empty")
        elif self.current.prev is None:
            print("This is the first version, can't go back")
        else:
            self.current = self.current.prev
            print(f"Moved back to version {self.current.version_id}")

    # 3. Go to the next version
    def go_forward(self):
        if self.current is None:
            print("History is empty")
        elif self.current.next is None:
            print("This is the last version, can't go forward")
        else:
            self.current = self.current.next
            print(f"Moved forward to version {self.current.version_id}")

    # 4. Find a version by id
    def find(self, version_id):
        node = self.head
        while node is not None:
            if node.version_id == version_id:
                return node
            node = node.next
        return None

    # 5. Delete a version by id
    def delete(self, version_id):
        node = self.find(version_id)
        if node is None:
            print(f"Version {version_id} not found")
            return

        # left neighbour skips the deleted node
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        # right neighbour skips the deleted node
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        # if the current version was deleted, move current
        if self.current is node:
            if node.prev is not None:
                self.current = node.prev
            else:
                self.current = node.next

        # no wrong links left on the deleted node
        node.prev = None
        node.next = None

        print(f"Deleted version {version_id}")

    # 6. History from first to last
    def show_forward(self):
        if self.is_empty():
            print("History is empty")
            return
        print("History (first to last):")
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    # 6. History from last to first
    def show_backward(self):
        if self.is_empty():
            print("History is empty")
            return
        print("History (last to first):")
        node = self.tail
        while node is not None:
            print(node)
            node = node.prev


# Test: empty history
history = DocumentHistory()
print("Empty history:")
history.show_current()
history.go_back()
history.show_forward()
history.delete(1)

# Test 1: add versions
print("\nAdding:")
history.add_version("Hello", "Document created")
history.add_version("Hello, world", "Added a word")
history.add_version("Hello, world!", "Added an exclamation mark")
history.add_version("Hello, world! How are you?", "Added a question")

# Tests 2 and 6
print()
history.show_forward()
print()
history.show_current()

# Test 3: moving between versions
print("\nMoving:")
history.go_forward()
history.go_back()
history.go_back()
history.go_forward()
history.show_current()

# Test 4: search
print("\nSearch:")
print(history.find(2))
print(history.find(10))

# Test 5: delete first, last and current
print("\nDeleting the first:")
history.delete(1)
history.show_forward()

print("\nDeleting the last:")
history.delete(4)
history.show_forward()

print("\nDeleting the current:")
history.show_current()
history.delete(3)
history.show_current()

print()
history.show_forward()
history.show_backward()

# delete the rest -> empty again
print("\nDeleting everything:")
history.delete(2)
history.show_forward()
history.show_current()