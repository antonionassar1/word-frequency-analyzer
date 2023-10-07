class FileHandler:
    def __init__(self, args):
        self.input_path = args.input
        self.output_path = args.output

    def read_input(self):
        """
        Read the contents of a file specified by the input path.
        :return: str - The string read from the file.
        """
        try:
            with open(self.input_path, "r") as file:
                str_file = file.read()
                if not str_file:
                    print(f'Exit, the provided file "{self.input_path}" is empty!')
                    exit()
                return str_file
        except FileNotFoundError as err:
            print(f'Error input file, No such file or directory "{self.input_path}"')
        except PermissionError as err:
            print(f'Error input file, No permissions to read the file "{self.input_path}"')
        except Exception as err:
            print('Something went wrong:', err)
        exit()

    def write_output(self, words_dict):
        """
        Write the list of words and their frequencies to an output file.
        :param words_dict: dict{str: int} - a dictionary representing a list of words and their frequencies.
        :return: None
        """
        try:
            with open(self.output_path, 'w') as file:
                for word, freq in words_dict.items():
                    file.write(f'{word} ({freq})\n')
            if not self.output_path.startswith('./'):
                self.output_path = './' + self.output_path
            print(f'Results saved to: "{self.output_path}"')
        except FileNotFoundError as err:
            print(f'Error output file, No such directory "{self.output_path}"')
        except PermissionError as err:
            print(f'Error output file, No permissions to write to the file "{self.output_path}"')
        except Exception as err:
            print('Error output file, Something went wrong:', err)
        exit()
