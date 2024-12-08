import unittest
from lab4.task8.src.task8 import evaluate_postfix_expression

class TestPostfixEvaluation(unittest.TestCase):
    def test_simple_expression(self):
        self.assertEqual(evaluate_postfix_expression("2 3 +"), 5)
        self.assertEqual(evaluate_postfix_expression("7 3 -"), 4)
        self.assertEqual(evaluate_postfix_expression("4 5 *"), 20)

    def test_complex_expression(self):
        self.assertEqual(evaluate_postfix_expression("2 3 + 4 *"), 20)  # (2 + 3) * 4
        self.assertEqual(evaluate_postfix_expression("5 1 2 + 4 * + 3 -"), 14)  # 5 + (1 + 2) * 4 - 3
        self.assertEqual(evaluate_postfix_expression("8 3 2 * + 5 -"), 9)  # 8 + (3 * 2) - 5

    def test_single_number(self):
        self.assertEqual(evaluate_postfix_expression("7"), 7)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            evaluate_postfix_expression("3 4 %")

if __name__ == "__main__":
    unittest.main()
