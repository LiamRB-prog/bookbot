def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_letter_frequency(text):
    letter_dict = {}
    for letter in text:
        if letter.lower() not in letter_dict:
            letter_dict[letter.lower()] = 1
        else:
            letter_dict[letter.lower()] += 1
    return letter_dict

def sort_on(items):
    return items['num']

def sort_dict(my_dict):
    sorted_dict = dict(sorted(my_dict.items()))
    return sorted_dict
