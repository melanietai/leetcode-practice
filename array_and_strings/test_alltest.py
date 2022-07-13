import unittest
from is_all_chars_unique import is_unique, is_unique_set, is_unique_dict
from is_permutation import is_permutation_counter, is_permutation_sort, is_permutation_bytearray

class Test1(unittest.TestCase):
    test_cases_is_unique = [
        ("abcde", True),
        ("", True),
        ("2sde2", False),
        ("".join([chr(val) for val in range(128)]), True),
        ("".join([chr(val // 2) for val in range(129)]), False),
    ]
    
    def test_is_unique(self):

        for test, expected in self.test_cases_is_unique:
            result = is_unique(test)
            self.assertEqual(result, expected)
    
    def test_is_unique_set(self):

        for test, expected in self.test_cases_is_unique:
            result = is_unique_set(test)
            self.assertEqual(result, expected)
    
    def test_is_unique_dict(self):

        for test, expected in self.test_cases_is_unique:
            result = is_unique_dict(test)
            self.assertEqual(result, expected)

class Test2(unittest.TestCase):
    test_cases_is_permutation = [
        ("abc", "cba", True),
        ("catz", "cats", False),
        ("cat ", "cat", False),
        ("12345", "4321", False),
        ("aa123", "a1a23", True),
        ("", "", True),
    ]

    def test_is_permutation_counter(self):
        for s1, s2, expected in self.test_cases_is_permutation:
            result = is_permutation_counter(s1, s2)
            self.assertEqual(result, expected)

    def test_is_permutation_sort(self):
        for s1, s2, expected in self.test_cases_is_permutation:
            result = is_permutation_sort(s1, s2)
            self.assertEqual(result, expected)
    
    def test_is_permutation_bytearray(self):
        for s1, s2, expected in self.test_cases_is_permutation:
            result = is_permutation_bytearray(s1, s2)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()