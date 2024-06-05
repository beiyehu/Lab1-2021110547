import unittest
from lab1 import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # 设置测试所需的图
        self.graph = {
            'i': {'am': 1, 'have': 1},
            'am': {'a': 1},
            'a': {'student': 1, 'teacher': 1},
            'have': {'a': 1},
            'student': {'of': 1},
            'of': {'computer': 1},
            'computer': {'science': 1}
        }

    def test_bridge_words_exist(self):
        # word1 和 word2 都存在于图中，并且存在桥接词
        result = find_bridge_words(self.graph, 'i', 'a')
        print("Test case 1 - input ('i', 'a'): Expected ['am', 'have'], got", result)
        self.assertEqual(result, ['am', 'have'])

        result = find_bridge_words(self.graph, 'student', 'computer')
        print("Test case 2 - input ('student', 'computer'): Expected ['of'], got", result)
        self.assertEqual(result, ['of'])

    def test_bridge_words_not_exist(self):
        # word1 和 word2 都存在于图中，但不存在桥接词
        result = find_bridge_words(self.graph, 'i', 'student')
        print("Test case 3 - input ('i', 'student'): Expected [], got", result)
        self.assertEqual(result, [])

        result = find_bridge_words(self.graph, 'am', 'teacher')
        print("Test case 4 - input ('am', 'teacher'): Expected [], got", result)
        self.assertEqual(result, [])

    def test_word2_not_exist(self):
        # word1 存在于图中，但 word2 不存在于图中
        result = find_bridge_words(self.graph, 'i', 'nonexistent')
        print("Test case 5 - input ('i', 'nonexistent'): Expected [], got", result)
        self.assertEqual(result, [])

    def test_word1_not_exist(self):
        # word1 不存在于图中，但 word2 存在于图中
        result = find_bridge_words(self.graph, 'nonexistent', 'a')
        print("Test case 6 - input ('nonexistent', 'a'): Expected [], got", result)
        self.assertEqual(result, [])

    def test_both_words_not_exist(self):
        # word1 和 word2 都不存在于图中
        result = find_bridge_words(self.graph, 'nonexistent', 'word')
        print("Test case 7 - input ('nonexistent', 'word'): Expected [], got", result)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
