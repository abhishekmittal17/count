from unittest import TestCase
from unittest import expectedFailure

from run import possible_decodes

class TestPossibleDecodesMethod(TestCase):

    def test_for_empty_expected_count_1(self):
        message = ''
        expected_count = 1

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)

    def test_for_5_expected_count_1(self):
        message = '5'
        expected_count = 1

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)

    def test_for_111_expected_count_3(self):
        message = '111'
        expected_count = 3

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)

    def test_for_121_expected_count_3(self):
        message = '121'
        expected_count = 3

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)

    def test_for_11111_expected_count_8(self):
        message = '11111'
        expected_count = 8

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)

    @expectedFailure
    def test_for_11111_expected_count_3(self):
        message = '11111'
        expected_count = 3

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)

    @expectedFailure
    def test_for_5_expected_count_2(self):
        message = '5'
        expected_count = 2

        actual_count = possible_decodes(message)
        self.assertEqual(actual_count, expected_count)
