import unittest

def quick_sort(S, a, b):
    if a >= b:
        return

    pivot = S[b]
    left = a
    right = b - 1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]

    quick_sort(S, a, left - 1)
    quick_sort(S, left + 1, b)

class TestCases(unittest.TestCase):

    def test_sort(self):
        import random
        S = [random.randint(1, 20) for x in range(20)]
        quick_sort(S, 0, len(S) - 1)

        prev = S[0]
        for x in S[1:]:
            self.assertTrue(prev <= x)
            prev = x

if __name__ == '__main__':
    unittest.main()
