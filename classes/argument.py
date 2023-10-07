import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="A program that counts unique words from an English text file, "
                        "treating hyphens and apostrophes as part of the word. "
                        "The program outputs the ten most frequent words "
                        "and mentions the number of occurrences."
        )
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument(
            '-i',
            '--input',
            help='Path to the file to read from.',
            required=True
        )
        self.parser.add_argument(
            '-o',
            '--output',
            help='Path to the file to save the result. If the file does not exist, it will be created '
                 'at the specified path or in the current directory.',
            required=True
        )

    def parse_arguments(self):
        return self.parser.parse_args()
