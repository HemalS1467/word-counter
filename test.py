import unittest
from app import WordCounter

class TestWordCounter(unittest.TestCase):
    def test_count_repetition(self):
        word_counter = WordCounter("foo foo bar baz")

        result = word_counter.count_repetition()
        self.assertEqual(result, [("bar", 1), ("baz", 1), ("foo", 2)])

        word_counter = WordCounter("hello world ,, 11 9 zzz zzz")
        result = word_counter.count_repetition()
        self.assertEqual(result, [(9, 1), (11, 1), ("hello", 1),("world",1),("zzz",2)])


    def test_count_total_words(self):
        word_counter = WordCounter("foo foo bar baz")
        word_counter.count_repetition()
        result = word_counter.count_total_words()
        self.assertEqual(result, 4)

        word_counter = WordCounter("hello world ,, 11 9 zzz zzz")
        word_counter.count_repetition()
        result = word_counter.count_total_words()
        self.assertEqual(result, 6)


    def test_count_total_characters_with_spaces(self):
        word_counter = WordCounter("foo foo bar baz")
        result = word_counter.count_total_characters()
        self.assertEqual(result, 15)

        word_counter = WordCounter("hello world ,, 11 9 zzz zzz")
        result = word_counter.count_total_characters()
        self.assertEqual(result, 27)

    def test_count_total_characters_without_spaces(self):
        word_counter = WordCounter("foo foo bar baz")
        result = word_counter.count_total_characters(with_spaces=False)
        self.assertEqual(result, 12)

        word_counter = WordCounter("hello world ,, 11 9 zzz zzz")
        result = word_counter.count_total_characters(with_spaces=False)
        self.assertEqual(result, 21)

if __name__ == '__main__':
    unittest.main()
