from empty import Empty
from doublyLinkedBase import _DoublyLinkedBase
import unittest

class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)

class Test(unittest.TestCase):

    def test_insert_first(self):
        d = LinkedDeque()
        d.insert_first(20)
        d.insert_first(15)
        self.assertTrue(len(d) == 2)
        self.assertTrue(d.first() == 15)

    def test_insert_last(self):
        d = LinkedDeque()
        d.insert_last(15)
        d.insert_last(20)
        self.assertTrue(len(d) == 2)
        self.assertTrue(d.last() == 20)

    def test_delete_first(self):
        d = LinkedDeque()
        d.insert_first(20)
        d.insert_first(15)
        result = d.delete_first()
        self.assertTrue(len(d) == 1)
        self.assertTrue(result == 15)
        self.assertTrue(d.first() == 20)

    def test_delete_last(self):
        d = LinkedDeque()
        d.insert_last(15)
        d.insert_last(20)
        result = d.delete_last()
        self.assertTrue(len(d) == 1)
        self.assertTrue(result == 20)
        self.assertTrue(d.last() == 15)

if __name__ == '__main__':
    unittest.main()
