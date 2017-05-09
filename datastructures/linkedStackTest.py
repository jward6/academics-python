import unittest

class Empty(Exception):
    pass

class Stack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, e, n):
            self._element = e
            self._next = n

    def __init__(self):
        self._head = self._Node(None, None)
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._head._next._element

    def push(self, e):
        n = self._Node(e, self._head._next)
        self._head._next = n
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        n = self._head._next
        self._head._next = n._next

        self._length -= 1
        return n._element

    def __iter__(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        n = self._head._next
        while(n != None):
            yield n._element
            n = n._next

class StackTests(unittest.TestCase):

    def test_push(self):
        s = Stack()
        s.push(15)
        s.push(20)

        self.assertEqual(len(s), 2)

    def test_top(self):
        s = Stack()

        s.push(15)
        s.push(20)

        self.assertEqual(s.top(), 20)

    def test_pop(self):
        s = Stack()

        s.push(15)
        s.push(20)

        self.assertEqual(s.pop(), 20)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.pop(), 15) 

    def test_iter(self):
        s = Stack()

        s.push(15)
        s.push(20)
        s.push(25)

        val = 25
        for e in s:
            self.assertEqual(e, val)
            val -= 5


if __name__ == '__main__':
    unittest.main()
