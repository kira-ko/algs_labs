import unittest
from lab4.task5.src.task5 import MaxStack, process_commands


class TestMaxStack(unittest.TestCase):
    def test_push_and_max(self):
        stack = MaxStack()
        stack.push(1)
        self.assertEqual(stack.max(), 1)
        stack.push(3)
        self.assertEqual(stack.max(), 3)
        stack.push(2)
        self.assertEqual(stack.max(), 3)

    def test_pop_and_max(self):
        stack = MaxStack()
        stack.push(1)
        stack.push(3)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.max(), 3)
        stack.pop()
        self.assertEqual(stack.max(), 1)

    def test_process_commands(self):
        commands = [
            "push 1",
            "push 3",
            "max",
            "pop",
            "max",
        ]
        expected = [3, 1]
        self.assertEqual(process_commands(commands), expected)

    def test_empty_stack_error(self):
        stack = MaxStack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.max()


if __name__ == "__main__":
    unittest.main()
