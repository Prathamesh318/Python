class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}.")

    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            print(f"Dequeued {item}.")
            return item
        else:
            print("Queue is empty.")
            return None

    def display(self):
        print("Queue elements:", self.queue)

# Example Usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.display()
