import unittest

# Function to test
def check_alphanumeric(string):
     for char in string:
         if not (char.isalnum() or char.isspace()):
             return False
     return True


# Test class
class test_check_alnum_function(unittest.TestCase):
    def test_all_alnum(self):
        self.assertEqual(check_alphanumeric("t3stc4s3"), True)
    
    def test_not_alnum(self):
        self.assertEqual(check_alphanumeric("!@#$%$#@!"), False)

    def test_some_alnum(self):
        self.assertEqual(check_alphanumeric("!t3stc4s3!"), False)


# Running tests
if __name__ == '__main__':
    unittest.main()