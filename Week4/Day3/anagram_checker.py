class AnagramChecker:
    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.word_list = {word.strip().upper() for word in file}
                print(f"Loaded {len(self.word_list)} words.")  
        except FileNotFoundError:
            print("Error: Word list file not found!")
            self.word_list = set()

    def is_valid_word(self, word):
        return word.upper() in self.word_list

    def is_anagram(self, word1, word2):
        word1 = word1.upper()
        word2 = word2.upper()

        if word1 == word2:
            return False
        return sorted(word1) == sorted(word2)

    def get_anagrams(self, word):
        word = word.upper()
        anagrams = []

        for w in self.word_list:
            if self.is_anagram(word, w):
                anagrams.append(w)

        print(f"Anagrams found for '{word}': {anagrams}")  
        return anagrams








     
