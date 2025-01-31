import re

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book_as_string= f.read()
    book_as_list = re.split(r'(\s+)', book_as_string)
    book_word_length = len(book_as_list)

    def number_of_characters():
        character_dict = {}
        for word in book_as_list:
            for letter in word:
                letter = letter.lower()
                if letter in character_dict:
                    character_dict[letter] += 1 
                else:
                    character_dict[letter] = 1

        letter_dict = {}
        for character in character_dict:
            if character.isalpha():
                letter_dict[character] = character_dict[character]
                
        for letter in letter_dict:    
            print(f"The '{letter}' character was found {letter_dict[letter]} times")

    number_of_characters()
main()