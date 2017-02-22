import unittest
from empty import Empty

class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_link'

        def __init__(self, e, l):
            self._element = e
            self._link = l

    def __init__(self):
        self._head = self._Node(None, None)
        self._tail = self._head

        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        head = self._head._link
        return head._element

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        # Pull the current node from the head
        old_head = self._head._link

        # Set the new head to the old heads link
        self._head._link = old_head._link

        self._size -= 1

        return old_head._element

    def enqueue(self, e):
        newest = self._Node(e, None)

        # Set the current tail link to the new Node
        self._tail._link = newest

        # set the tail to the new Node 
        self._tail = newest

        self._size += 1

    def rotate(self, k):
        # For each count of k, remove the head and add to back    
        for n in range(k):
            head = self.dequeue()
            self.enqueue(head)

    def concatenate(self, q):
        if not isinstance(q, LinkedQueue):
            raise ValueError('q is not of type LinkedQueue')
        if q.is_empty():
            raise ValueError('q is empty')

        # Input queue is latched onto the end of the current queue
        old_tail = self._tail
        self._tail = q._tail
        old_tail._link = self._head._link

        self._size += q._size

        # Reset the input queue
        q._head = self._Node(None, None)
        q._tail = q._head
        q._size = 0

class Test(unittest.TestCase):

    def test_enqueue(self):
        q = LinkedQueue()
        q.enqueue(15)
        q.enqueue(20)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.first(), 15)

    def test_dequeue(self):
        q = LinkedQueue()
        q.enqueue(15)
        q.enqueue(20)
        q.enqueue(25)
        result = q.dequeue()
        self.assertEqual(len(q), 2)
        self.assertEqual(result, 15)
        self.assertEqual(q.first(), 20)

    def test_rotate(self):
        q = LinkedQueue()
        q.enqueue(15)
        q.enqueue(20)
        q.enqueue(25)
        q.rotate(2)
        self.assertEqual(q.first(), 25)

    def test_concatenate(self):
        first = LinkedQueue()
        first.enqueue(15)
        first.enqueue(20)
        first.enqueue(25)

        second = LinkedQueue()
        second.enqueue(30)
        second.enqueue(35)

        first.concatenate(second)

        self.assertEqual(len(first), 5)
        self.assertEqual(first.first(), 15)
        self.assertEqual(first.last(), 35)
        self.assertTrue(second.is_empty())


if __name__ == '__main__':
    unittest.main()
