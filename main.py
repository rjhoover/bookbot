
def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents

def count_words(input):
    return len(input.split())


def main():
    file_name = "./books/frankenstein.txt"
    book_text = read_file(file_name)
    num_words = count_words(book_text)

    print(f"{num_words} words found in the document")



main()
