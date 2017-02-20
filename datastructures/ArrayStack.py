import unittest

class Empty(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()

class Test(unittest.TestCase):

    def test_push_error(self):
        arr = ArrayStack()
        try:
            arr.top()
        except Empty as ex:
            self.assertIsInstance(ex, Empty)

    def test_push(self):
        arr = ArrayStack()
        arr.push(15)
        self.assertTrue(len(arr) == 1)

    def test_pop(self):
        arr = ArrayStack()
        arr.push(15)
        arr.push(20)
        result = arr.pop()
        self.assertTrue(result == 20)

    def test_top(self):
        arr = ArrayStack()
        arr.push(15)
        arr.push(20)
        arr.push(25)
        self.assertTrue(arr.top() == 25)

if __name__ == '__main__':
    unittest.main()
