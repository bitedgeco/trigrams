# _*_ coding: utf-8 _*_

import io


def get_text_data(text):
    """Return text from a file as a string"""
    input_file = io.open(text, encoding="utf-8")
    text_data = input_file.read()
    input_file.close()
    return text_data


def split_string_into_words(text_string):
    split_string = text_string.split()
    return split_string


def make_dict_from_list(word_list):
    kata_dict = {}
    kata_value_array = []
    for i in range(0,len(word_list) - 2, 3):
        kata_key = word_list[i] + ' ' + word_list[i + 1]
        kata_value = kata_value_array.append(word_list[i + 2])
        kata_dict[kata_key] = 
        if kata_key in kata_dict.keys:
            kata_dict[kata_key].append(word_list[i + 2])
        else:
            kata_value = kata_value.append(word_list[i + 2])
            kata_dict[kata_key] = kata_value
    return kata_dict
