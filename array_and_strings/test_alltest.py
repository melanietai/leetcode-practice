import unittest
from is_all_chars_unique import is_unique, is_unique_set, is_unique_dict

class Test(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()