# _*_ coding: utf-8 _*_

import io


def get_text_data(text):
    """Return text from a file as a list"""
    input_file = io.open(text, encoding="utf-8")
    text_data = input_file.read()
    input_file.close()
    text_data_as_list = text_data.split()
    return text_data_as_list


def make_dict_from_list(word_list):
    """Return a dictionary created from the source text"""
    kata_dict = {}
    for i in range(len(word_list) - 2):
        kata_key = word_list[i] + ' ' + word_list[i + 1]
        if kata_key in kata_dict.keys():
            kata_value = kata_dict.get(kata_key)
        else:
            kata_value = []
        kata_value.append(word_list[i + 2])
        kata_dict[kata_key] = kata_value
    return kata_dict


def make_text_from_dict(first_word_pair, created_dictionary, new_text_length):
    """Return text created using the created dictionary"""
    import random
    created_text = first_word_pair
    for i in range(int(new_text_length) - 2):
        next_word_list = created_dictionary.get(first_word_pair)
        if next_word_list:
            next_word = random.choice(next_word_list)
            created_text = created_text + " " + next_word
            created_text_to_list = created_text.split()
            first_word_pair = str(created_text_to_list[-2]) + \
                ' ' + str(created_text_to_list[-1])
        else:
            break
    return created_text


def main_function(source_path, word_count):
    """Return newly created text based on the source text and word count"""
    text = source_path
    text_data_as_list = get_text_data(text)
    first_pair = get_text_data(text)[0] + ' ' + get_text_data(text)[1]
    created_dictionary = make_dict_from_list(text_data_as_list)
    created_text = make_text_from_dict(first_pair, created_dictionary,
                                       word_count)
    print(created_text)
    return created_text


if __name__ == '__main__':
    import sys
    source_path = sys.argv[1]
    word_count = sys.argv[2]
    main_function(source_path, word_count)
