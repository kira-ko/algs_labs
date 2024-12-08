class MaxStack:
    """Класс для реализации стека с поддержкой операций Push(), Pop() и Max()."""

    def __init__(self):
        self.stack = []  # Основной стек
        self.max_stack = []  # Дополнительный стек для отслеживания максимумов

    def push(self, value):
        """Добавляет элемент в стек"""
        self.stack.append(value)
        # Если стек максимумов пуст или новый элемент больше/равен текущему максимуму, добавляем его
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        """Удаляет элемент из стека"""
        if not self.stack:
            raise IndexError("Pop from empty stack")
        value = self.stack.pop()
        # Если удаляемый элемент равен текущему максимуму, удаляем его из max_stack
        if value == self.max_stack[-1]:
            self.max_stack.pop()

    def max(self):
        """Возвращает текущий максимум стека"""
        if not self.max_stack:
            raise IndexError("Max from empty stack")
        return self.max_stack[-1]


def process_commands(commands):
    """
    Обрабатывает команды для стека с максимумом.

    :param commands: список команд
    :return: список результатов для команды max
    """
    stack = MaxStack()
    results = []

    for command in commands:
        parts = command.split()
        if parts[0] == "push":
            stack.push(int(parts[1]))
        elif parts[0] == "pop":
            stack.pop()
        elif parts[0] == "max":
            results.append(stack.max())
        else:
            raise ValueError(f"Unknown command: {parts[0]}")

    return results


if __name__ == "__main__":
    with open('../txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())
        commands = [f.readline().strip() for _ in range(n)]


    results = process_commands(commands)

    with open('../txtf/output.txt', 'w') as f:
        f.write('\n'.join(map(str, results)) + '\n')