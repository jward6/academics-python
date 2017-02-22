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
        # Use of a header sentinel
        self._header = self._Node(None, None)
        self._header._next = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        node = self._Node(e, self._header._next)
        self._header._next = node
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._header._next._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._header._next
        self._header._next = answer._next
        self._size -= 1
        return answer._element

class Test(unittest.TestCase):

    def test_len(self):
        s = LinkedStack()
        self.assertEqual(len(s), 0)

    def test_push(self):
        s = LinkedStack()
        s.push(15)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.top(), 15)

    def test_top(self):
        s = LinkedStack()
        s.push(15)
        s.push(20)
        self.assertEqual(s.top(), 20)

    def test_pop(self):
        s = LinkedStack()
        s.push(15)
        s.push(20)
        result = s.pop()
        self.assertEqual(result, 20)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.top(), 15)


if __name__ == '__main__':
    unittest.main()
