from stats import get_word_count
from stats import get_character_count_dict


"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
ô: 1
============= END ===============
"""


def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents


def get_sorted_dictionaries(dict):
    report_dict = {}

    for key, value in dict:
        report_dict = { "char": key, "num": value }

    return report_dict


def main():
    file_name = "./books/frankenstein.txt"
    book_text = read_file(file_name)

    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")

    num_chars_dict = get_character_count_dict(book_text)
    print(num_chars_dict)

    # report_dict = {}
    # for key, value in num_chars_dict:
    #     report_dict = { "char": key, "num": value }

    # print(report_dict)


main()
