def is_correct_sequence(sequence):
    stack = []
    matching_brackets = {')': '(', ']': '['}

    for char in sequence:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return "NO"

    return "YES" if not stack else "NO"


def process_sequences(sequences):
    return [is_correct_sequence(seq) for seq in sequences]


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as infile:
        lines = infile.readlines()

    n = int(lines[0].strip())  # Число строк
    sequences = [line.strip() for line in lines[1:n + 1]]

    results = process_sequences(sequences)

    with open("../txtf/output.txt", "w") as outfile:
        outfile.write("\n".join(results) + "\n")