def get_word_count(input):
    return len(input.split())

def get_character_count_dict(input):
    letters_dict = {}

    for letter in input:
        lower_letter = letter.lower()
        if lower_letter in letters_dict:
            letters_dict[lower_letter] += 1
        else:
            letters_dict[lower_letter] = 1

    return letters_dict

def get_unsorted_list_of_dict(input_dict):
    unsorted_list = []

    for character in input_dict:
        char_count_dict = { "char": character, "num": input_dict[character] }
        unsorted_list.append(char_count_dict)

    return unsorted_list

def sort_on_num(dict):
    return dict["num"]



def get_sorted_list_of_dict(input_list):
    sorted_list = []

    sorted_list = sorted(input_list, key=sort_on_num)        

    return sorted_list




# def get_sorted_dictionary(dict):
#     sorted_dict = {}
#     sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

#     return sorted_dict

# def get_sorted_dictionaries(dict):
#     report_dict = {}

#     for key, value in dict:
#         report_dict = { "char": key, "num": value }

#     return report_dict