import re
from itertools import islice

class WordAnalyzer:
    def __init__(self, file_string):
        self.words = self.__clean_string(file_string.lower())

    def create_word_frequencies(self):
        """
        Description: Analyze a list of words, split them on special characters (except hyphens and apostrophes),
        and calculate the frequency of each unique word.
        :return: dict{str, int}: A dictionary containing words as keys and their frequencies as values. {str: int, ...}
        """
        word_frequencies = {}
        
        for word in self.words:
            if word:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1
        
        return word_frequencies

    def sort_word_frequencies(self, word_frequencies, descending=True):
        """
        Description: Sort a dictionary of word frequencies either in ascending or descending order based on the values.
        :param descending: bool - True to sort in descending order, False to sort in ascending order.
        :param word_frequencies: dict{str: int} Key-value pairs representing words and their frequencies.
        :return: dict{str, int}: A sorted dictionary.
        """
        sorted_words = dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=descending))
        return sorted_words

    def get_top_words(self, num_words, word_frequencies):
        """
        Description: Retrieve the top 'n' words (key-value pairs) from a dictionary.
        If the total number of words is less than 'num_words', return the entire dictionary.
        :param num_words: int - The number of elements to retrieve from the dictionary.
        :param word_frequencies: dict{str, int} - A dictionary to extract key-value pairs from.
        :return: dict{str, int} - The top 'n' values from the dictionary.
        """
        return word_frequencies if len(word_frequencies) <= num_words else self.__take(num_words, word_frequencies.items())

    @staticmethod
    def __clean_string(string):
        """
        Description: Split a string on special characters (excluding hyphens and apostrophes).
        :param string: str - The input string to be split.
        :return: list[str] - A list of strings after splitting the original string.
        """
        return re.split(r'(?:[^-\'a-zA-Z0-9]|[.]\s)+', string)

    @staticmethod
    def __take(num_items, iterable):
        """
        Description: Return the first 'n' items from an iterable as a dictionary.
        :param num_items: int - The number of items to take.
        :param iterable: iterable - The iterable to extract items from.
        :return: dict - A dictionary containing the first 'n' items from the iterable.
        """
        return dict(islice(iterable, num_items))
