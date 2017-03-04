
from empty import Empty

import unittest

class SinglyLinkedList:
    __slots__ = '_element', '_link'

    def __init__(self):
        self._element = None
        self._link = None

    def __str__(self):
        return str(self._element)

    def _last(self, parent):
        if parent._link is None:
            return parent 
        else:
            return self._last(parent._link)

    def __iter__(self):
        return self._iterate(self)

    def _iterate(self, parent):
        yield parent
        if parent._link is not None:
            self._iterate(parent._link)

    def add(self, e):
        if self._element is None and self._link is None:
            self._element = e
        else:
            new_node = SinglyLinkedList()
            new_node._element = e
            new_node._link = None
            last = self._last(self)
            last._link = new_node

    def reverse(self):
        prev = None
        cur = self
        while cur is not None:
            t = cur._link
            cur._link = prev
            prev = cur
            cur = t

        return prev

class Test(unittest.TestCase):
    
    def test_add(self):
        l = SinglyLinkedList()
        l.add(10)
        l.add(15)

        self.assertEqual(l._last(l)._element, 15)

    def test_iter(self):
        l = SinglyLinkedList()
        l.add(0)
        l.add(1)
        l.add(2)

        counter = 0
        for i in l:
            self.assertEqual(i._element, counter)
            counter += 1

    def test_reverse(self):
        l = SinglyLinkedList()
        l.add(0)
        l.add(1)
        l.add(2)
        l.add(3)

        l =  l.reverse()

        counter = 3
        for i in l:
            self.assertEqual(i._element, counter)
            counter -= 1

if __name__ == '__main__':
    unittest.main()

