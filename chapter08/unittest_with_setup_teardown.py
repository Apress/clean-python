from unittest import TestCase


class SetupBaseTestCase(TestCase):
    def setUp(self):
        self.sess = CallClassBeforeStartingTest()
 
    def test_simple():
        self.sess.call_function()

    def tearDown(self):
        self.sess.close()
