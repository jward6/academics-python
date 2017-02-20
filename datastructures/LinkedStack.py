import unittest

class Empty(Exception):
    pass

class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

class Test(unittest.TestCase):

    def test_len(self):
        s = LinkedStack()
        self.assertTrue(len(s) == 0)

    def test_push(self):
        s = LinkedStack()
        s.push(15)
        self.assertTrue(len(s) == 1)
        self.assertTrue(s.top() == 15)

    def test_pop(self):
        s = LinkedStack()
        s.push(15)
        s.push(20)
        result = s.pop()
        self.assertTrue(result == 20)
        self.assertTrue(len(s) == 1)
        self.assertTrue(s.top() == 15)


if __name__ == '__main__':
    unittest.main()
