import unittest


# Function to test
def check_for_word(string):
     for letter in string:
         if letter.isalpha():
             return True
     return False


# Testing class
class test_check_word_function(unittest.TestCase):
    def test_all_letters(self):
        self.assertEqual(check_for_word("testcase"), True)

    def test_no_letters(self):
        self.assertEqual(check_for_word("$$#@%$$"), False)

    def test_some_letters(self):
        self.assertEqual(check_for_word("te$tc@$e"), True)


# Running tests
if __name__ == '__main__':
    unittest.main()

