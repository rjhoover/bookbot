import sys
from stats import *

def print_report(book_file, num_words, list_of_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for count_dict in list_of_dict:
        if count_dict["char"].isalpha():
            print(f"{count_dict["char"]}: {count_dict["num"]}")

    print("============= END ===============")

def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_name = sys.argv[1] 

    # file_name = "./books/frankenstein.txt"
    book_text = read_file(file_name)
    num_words = get_word_count(book_text)
    num_chars_dict = get_character_count_dict(book_text)
    unsorted_list_of_dict = get_unsorted_list_of_dict(num_chars_dict)
    sorted_list = get_sorted_list_of_dict(unsorted_list_of_dict)

    print_report(file_name, num_words, sorted_list)

main()


