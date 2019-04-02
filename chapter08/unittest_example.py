from unittest import TestCase

class SimpleTest(TestCase):
    def test_simple(self):
        self.assertTrue(True)

    def test_tuple(self):
        self.assertEqual((1, 3, 4), (1, 3, 4))

    def test_str(self):
        self.assertEqual('This is unit test', 'this is')
