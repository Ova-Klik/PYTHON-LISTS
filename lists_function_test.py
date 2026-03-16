from unittest import TestCase
from list_tasks import *

class TestListFunctions(TestCase):

    def test_that_function_returns_length_of_list(self):
        numbers = [1,2,3,4,5]
        expected =  5
        actual = get_length_of_list(numbers)
        self.assertEqual(actual, 5)

    def test_get_sum_of_element_in_list(self):
        numbers = [1,2,3,4]
        self.assertEqual(get_sum_of_element_in_list(numbers), 10)

    def test_get_sum_of_element_even_positions(self):
        numbers = [1,2,3,4,5,6]
        expected = 12
        actual = get_sum_of_element_even_positions(numbers)
        self.assertEqual(actual, expected)

    def test_get_sum_of_element_odd_positions(self):
        numbers = [1,2,3,4,5,6]
        self.assertEqual(get_sum_of_element_odd_positions(numbers), 9)

    def test_get_product_of_element_at_third_positions(self):
        numbers = [1,2,3,4,5,6,7]
        self.assertEqual(get_product_of_element_at_third_positions(numbers), 12)

    def test_get_average_of_all_elements(self):
        numbers = [2,4,6,8]
        self.assertEqual(get_average_of_all_elements(numbers), 5)

    def test_get_largest_of_all_elements(self):
        numbers = [3,9,1,7]
        self.assertEqual(get_largest_of_all_elements(numbers), 9)

    def test_get_smallest_of_all_elements(self):
        numbers = [3,9,1,7]
        self.assertEqual(get_smallest_of_all_elements(numbers), 1)

    def test_add_every_third_element(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(add_every_third_element(numbers), 18)

    def test_add_first_middle_and_last_element_odd(self):
        numbers = [1,2,3,4,5]
        self.assertEqual(add_first_middle_and_last_element(numbers), 9)

    def test_add_first_middle_and_last_element_even(self):
        numbers = [1,2,3,4]
        self.assertEqual(add_first_middle_and_last_element(numbers), 7.5)


