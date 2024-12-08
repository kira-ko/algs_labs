from collections import deque

class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()

    def push(self, value):
        self.queue.append(value)
        while self.min_queue and self.min_queue[-1] > value:
            self.min_queue.pop()
        self.min_queue.append(value)

    def pop(self):
        if self.queue:
            value = self.queue.popleft()
            if value == self.min_queue[0]:
                self.min_queue.popleft()

    def get_min(self):
        if self.min_queue:
            return self.min_queue[0]


def process_commands(commands):
    queue = MinQueue()
    results = []

    for command in commands:
        if command.startswith("+"):
            _, value = command.split()
            queue.push(int(value))
        elif command == "-":
            queue.pop()
        elif command == "?":
            results.append(queue.get_min())

    return results


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as infile:
        lines = infile.readlines()

    m = int(lines[0].strip())
    commands = [line.strip() for line in lines[1:m + 1]]

    results = process_commands(commands)

    with open("../txtf/output.txt", "w") as outfile:
        outfile.write("\n".join(map(str, results)) + "\n")
