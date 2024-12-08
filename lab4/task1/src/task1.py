def process_stack(commands):
    stack = []
    result = []

    for command in commands:
        if command.startswith('+'):
            _, num = command.split()
            stack.append(int(num))
        elif command == '-':
            result.append(stack.pop())

    return result


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as infile:
        lines = infile.readlines()

    num_commands = int(lines[0].strip())
    commands = [line.strip() for line in lines[1:num_commands + 1]]


    results = process_stack(commands)


    with open("../txtf/output.txt", "w") as outfile:
        for result in results:
            outfile.write(f"{result}\n")
