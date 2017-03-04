from empty import Empty
from priorityQueueBase import PriorityQueueBase

import unittest

class HeapPriorityQueue(PriorityQueueBase):

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""

        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

def pq_sort(C):
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)

class Tests(unittest.TestCase):

    def test_add(self):
        q = HeapPriorityQueue()
        q.add(5, 50)
        q.add(2, 20)
        q.add(1, 10)
        q.add(10, 100)
        q.add(9, 90)

        self.assertEqual(len(q), 5)
        self.assertEqual(q.min(), (1, 10))

    def test_remove_min(self):
        q = HeapPriorityQueue()
        q.add(3, 30)
        q.add(2, 20)
        q.add(4, 40)
        q.add(1, 10)
        q.add(5, 50)

        result = q.remove_min()
        self.assertEqual(len(q), 4)
        self.assertEqual(result, (1, 10))
        self.assertEqual(q.min(), (2, 20))

if __name__ == '__main__':
    unittest.main()
