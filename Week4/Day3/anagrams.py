from anagram_checker import AnagramChecker

file_path = "/Users/saulerub/DI_Bootcamp/Week4/Day3/sowpods.txt"
checker = AnagramChecker(file_path)

def main():
    print("Welcome to the Anagram Checker!")

    while True:
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")
        user_choice = input("Please choose an option (1 or 2): ").strip()

        if user_choice == "2":
            print("Goodbye!")
            break
        elif user_choice == "1":
            user_input = input("Enter a word: ").strip()

            print(f"User input: {user_input}")  

            if len(user_input.split()) > 1:
                print("Please enter only one word.")
                continue

            if not user_input.isalpha():
                print("Invalid input! Please enter only alphabetic characters.")
                continue

            if not checker.is_valid_word(user_input):
                print(f"'{user_input}' is not a valid English word.")
                continue

            print(f"\nYOUR WORD: '{user_input.upper()}' is a valid English word!")
            anagrams = checker.get_anagrams(user_input)

            if anagrams:
                print("Anagrams for your word: " + ", ".join(anagrams))
            else:
                print("No anagrams found.")
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()