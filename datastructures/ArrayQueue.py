import unittest

class Empty(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self, cap=DEFAULT_CAPACITY):
        self._data = [None] * cap
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

class Test(unittest.TestCase):

    def test_enqueue(self):
        q = ArrayQueue()
        q.enqueue(10)
        self.assertTrue(len(q) == 1)

    def test_dequeue(self):
        q = ArrayQueue()
        q.enqueue(10)
        q.enqueue(15)
        result = q.dequeue()
        self.assertTrue(len(q) == 1)
        self.assertTrue(result == 10)

    def test_enqueue_resize(self):
        q = ArrayQueue(2)
        q.enqueue(10)
        q.enqueue(15)
        q.enqueue(20)
        self.assertTrue(len(q) == 3)
        self.assertTrue(q.dequeue() == 10)
        self.assertTrue(q.dequeue() == 15)

if __name__ == '__main__':
    unittest.main()
