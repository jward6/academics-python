import unittest
from empty import Empty

class CircularQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = self._Node(None, None)
        self._tail = self._Node(None, self._head)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail
        self._tail = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, self._tail._next)
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail == self._tail._next

class Test(unittest.TestCase):

    def test_enqueue(self):
        q = CircularQueue()
        q.enqueue(15)
        self.assertEqual(len(q), 1)
        self.assertEqual(q.first(), 15)

    def test_dequeue(self):
        q = CircularQueue()
        q.enqueue(15)
        q.enqueue(20)
        result = q.dequeue()
        self.assertEqual(result, 15)
        self.assertEqual(len(q), 1)

    def test_first(self):
        q = CircularQueue()
        q.enqueue(15)
        q.enqueue(20)
        q.enqueue(25)
        self.assertEqual(q.first(), 15)

    def test_rotate(self):
        q = CircularQueue()
        q.enqueue(15)
        q.enqueue(20)
        q.enqueue(25)

        q.rotate()

        self.assertEqual(len(q), 3)
        self.assertEqual(q.first(), 15)


if __name__ == '__main__':
    unittest.main()
