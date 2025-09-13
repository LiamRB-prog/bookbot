from stats import get_num_words

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        pass
    return file_contents

def main():
    file = 'books/frankenstein.txt'
    file_string = get_book_text(file)
    num_words = get_num_words(file_string)
    print(str(num_words) + " words found in the document")

main()
