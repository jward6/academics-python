from empty import Empty
from priorityQueueBase import PriorityQueueBase
from positionalList import PositionalList

import unittest

class SortedPriorityQueue(PriorityQueueBase):
    """A min oriented priority queue implemented with a sorted list."""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)

        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

    class Test(unittest.TestCase):
        def test_add(self):
            q = SortedPriorityQueue()
            q.add(1, 10)
            self.assertEqual(len(q), 1)

        def test_add_order(self):
            q = SortedPriorityQueue()
            q.add(5, 50)
            q.add(1, 10)
            q.add(2, 20)
            result = q.min()

            self.assertEqual(result, (1, 10))

        def test_remove_min(self):
            q = SortedPriorityQueue()
            q.add(3, 30)
            q.add(2, 20)
            q.add(1, 10)

            result = q.remove_min()
            self.assertEqual(result, (1, 10))
            self.assertEqual(len(q), 2)

if __name__ == '__main__':
    unittest.main()
