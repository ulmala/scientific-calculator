import unittest
from entities.output_queue import OutputQueue


class TestOutputQueue(unittest.TestCase):
    def setUp(self):
        self.output_queue = OutputQueue()

    def test_str_repr_returns_list_as_string(self):
        self.output_queue.put("+")
        self.output_queue.put("-")
        self.assertEqual(str(["+", "-"]), str(self.output_queue))