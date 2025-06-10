import os

class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.lower().split()
        frequency = words.count(word.lower())
        if frequency == 0:
            return f"The word '{word}' does not appear in the text."
        return frequency
    
    def most_common_word(self):
        words = self.text.lower().split()
        word_count = {word: words.count(word) for word in words}
        most_common = max(word_count, key=word_count.get)
        return most_common
    
    def unique_words(self):
        words = set(self.text.lower().split())
        return list(words)

    @classmethod
    def from_file(cls, filename):
        print(f"Looking for file: {filename}")
        print(f"Current working directory: {os.getcwd()}")
        abs_path = os.path.abspath(filename)
        print(f"Absolute path: {abs_path}")
        try:
            with open(filename, 'r') as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please check the path.")
            return None

text_file_instance = Text.from_file('Week3/Day5/the_stranger.txt')
if text_file_instance:
    print(text_file_instance.word_frequency("the"))