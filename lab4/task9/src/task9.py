from collections import deque

class PolyclinicQueue:
    def __init__(self):
        self.queue = deque()
        self.middle_index = 0

    def add_end(self, patient_id):
        self.queue.append(patient_id)

    def add_middle(self, patient_id):
        self.middle_index = (len(self.queue) + 1) // 2
        self.queue.insert(self.middle_index, patient_id)

    def serve_patient(self):
        return self.queue.popleft()

def process_requests(commands):
    queue = PolyclinicQueue()
    results = []

    for command in commands:
        if command.startswith("+"):
            _, patient_id = command.split()
            queue.add_end(int(patient_id))
        elif command.startswith("*"):
            _, patient_id = command.split()
            queue.add_middle(int(patient_id))
        elif command == "-":
            results.append(queue.serve_patient())

    return results


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as infile:
        lines = infile.readlines()

    n = int(lines[0].strip())
    commands = [line.strip() for line in lines[1:n + 1]]

    results = process_requests(commands)

    with open("../txtf/output.txt", "w") as outfile:
        outfile.write("\n".join(map(str, results)) + "\n")