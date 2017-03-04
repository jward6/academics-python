from empty import Empty
from priorityQueueBase import PriorityQueueBase
from positionalList import PositionalList
import unittest

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):
        """Returns Position of item with minumum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

class Tests(unittest.TestCase):
    
    def test_length(self):
        q = UnsortedPriorityQueue()
        empty = len(q)

        q.add(1, 10)

        one = len(q)

        self.assertEqual(empty, 0)
        self.assertEqual(one, 1)

    def test_add(self):
        q = UnsortedPriorityQueue()
        q.add(1, 10)
        q.add(2, 15)

        self.assertEqual(len(q), 2)

    def test_min(self):
        q = UnsortedPriorityQueue()
        q.add(1, 10)
        q.add(2, 15)
        q.add(3, 20)

        result = q.min()

        self.assertEqual(result, (1, 10))

    def test_remove_min(self):
        q = UnsortedPriorityQueue()
        q.add(2, 10)
        q.add(5, 50)
        q.add(1, 100)

        result = q.remove_min()
        self.assertEqual(result, (1, 100))
        self.assertEqual(len(q), 2)

if __name__ == '__main__':
    unittest.main()
