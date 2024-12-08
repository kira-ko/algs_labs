def evaluate_postfix_expression(expression):
    """Вычисляет значение выражения в постфиксной записи."""
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # Если токен - число
            stack.append(int(token))
        else:  # Если токен - оператор
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                raise ValueError(f"Неизвестный оператор: {token}")

    return stack[0]  # Результат остается единственным элементом в стеке




if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as f:
        n = int(f.readline().strip())
        expression = f.readline().strip()

    result = evaluate_postfix_expression(expression)

    with open("../txtf/output.txt", "w") as f:
        f.write(str(result) + '\n')


