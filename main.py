
def main():
	file_name = "./books/frankenstein.txt"
	book_text = read_file(file_name)
	word_count = count_words(book_text)
	letters_dict = count_letter_quantity(book_text)
	sorted_dict = sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)


	print(f"--- Begin report of {file_name} ---")
	print(f"{word_count} words found in the document")
	
	for letter, count in sorted_dict:
		if letter.isalpha():
			print(f"The '{letter}' character was found {count} times")
	
	print("--- End report ---")


# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list

def read_file(file_name):
	with open(file_name) as f:
		file_contents = f.read()
	return file_contents

def count_words(input):
	words = input.split()
	return len(words)

def count_letter_quantity(input):
	letters = {}
	for letter in input:
		lower_letter = letter.lower()
		if lower_letter in letters:
			letters[lower_letter] += 1
		else:
			letters[lower_letter] = 1
	return letters



main()
