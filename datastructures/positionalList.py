from empty import Empty
from doublyLinkedBase import _DoublyLinkedBase
import unittest

class PositionalList(_DoublyLinkedBase):

    class Position:
        __slots__ = '_container', '_node'
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element 
        original._element = e
        return old_value



class Tests(unittest.TestCase):

    def test_validate(self):
        p = PositionalList()
        try:
            p._validate(15)
        except TypeError:
            self.assertTrue(True)

    def test_add_first(self):
        p = PositionalList()
        p.add_first(20)
        p.add_first(15)
        self.assertEqual(p.first().element(), 15)

    def test_add_last(self):
        p = PositionalList()
        p.add_last(15)
        p.add_last(20)
        self.assertEqual(p.last().element(), 20)

    def test_add_before(self):
        p = PositionalList()
        second = p.add_first(25)
        p.add_before(second, 20)
        self.assertEqual(p.first().element(), 20) 

    def test_add_after(self):
        p = PositionalList()
        first = p.add_first(15)
        p.add_after(first, 20)
        self.assertEqual(p.last().element(), 20)

    def test_delete(self):
        p = PositionalList()
        first = p.add_first(15)
        second = p.add_last(20)
        p.delete(first)
        self.assertEqual(p.first().element(), 20)

    def test_replace(self):
        p = PositionalList()
        p.add_first(15)
        t = p.add_last(25)
        p.replace(t, 20)
        self.assertEqual(p.last().element(), 20)

if __name__ == '__main__':
    unittest.main()
