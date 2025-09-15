from stats import get_num_words
from stats import get_letter_frequency
from stats import sort_dict

import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        pass
    return file_contents

def book_report(file):
    file_string = get_book_text(file)
    num_words = get_num_words(file_string)
    letter_frequency = get_letter_frequency(file_string)
    sorted_dict = sort_dict(letter_frequency)

    print("========== BOOKBOT ==========")
    print("Analyzing book found at " + file + "...")
    print("---------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("---------- Character Count ----------")
    for letter, val in sorted_dict.items():
        if letter.isalpha():
            print(str(letter) + ": " + str(val))
    print("========== END ==========")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_report(sys.argv[1])

main()
