from classes.argument import ArgumentParser
from classes.file import FileHandler
from classes.word import WordAnalyzer

__author__ = "Your Name"
__license__ = "Your License"

def main():
    args_parser = ArgumentParser()
    args = args_parser.parse_arguments()

    file_handler = FileHandler(args)
    file_contents = file_handler.read_input()

    word_analyzer = WordAnalyzer(file_contents)
    word_frequencies = word_analyzer.create_word_frequencies()
    sorted_word_frequencies = word_analyzer.sort_word_frequencies(word_frequencies)
    top_10_words = word_analyzer.get_top_words(10, sorted_word_frequencies)

    print_to_console(top_10_words)
    file_handler.write_output(top_10_words)

def print_to_console(words_dict):
    """
    Description: Print a dictionary of key-value pairs.
    :param words_dict: dict{str, int} A dictionary of key/value pairs containing words and their frequencies.
    :return: None
    """
    print('Most frequent words list:')
    for word, freq in words_dict.items():
        print(f'{word} ({freq})')
    print('')

if __name__ == '__main__':
    main()
