from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        filepath = "./files/hello.txt"
        res = solution(filepath)

        self.assertEqual('Hello World!\n', res)
        self.assertIsInstance(res, str)