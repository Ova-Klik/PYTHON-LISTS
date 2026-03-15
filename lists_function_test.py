from unittest import TestCase
import list_tasks


class TestClass(TestCase):
    
    def test_that_function_returns_accurate_length_of_a_list(self):
        
        numbers=[1,2,3,45,6,6,5,4,4,33,33]
        expected= get_length_of_list(numbers)
        actual=11
        
        self.assertEqual(actual,expected)
