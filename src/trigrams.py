# _*_ coding: utf-8 _*_

import io


def get_text_data(text):
    """Return text from a file as a string"""
    input_file = io.open(text, encoding="utf-8")
    text_data = input_file.read()
    input_file.close()
    text_data_as_list =text_data.split()
    return text_data_as_list


def make_dict_from_list(word_list):
    kata_dict = {}
    for i in range(len(word_list) - 2):
        kata_key = word_list[i] + ' ' + word_list[i + 1]
        if kata_key in kata_dict.keys():
             kata_value = kata_dict.get(kata_key)
        else:
             kata_value = []
        #import pdb; pdb.set_trace()
        kata_value.append(word_list[i + 2])
        kata_dict[kata_key] = kata_value
    return kata_dict

def make_text_from_dict(first_word_pair, created_dictionary, new_text_length):
    created_text = first_word_pair
    for i in range (new_text_length - 2):
        next_word_list = created_dictionary.get(first_word_pair)
        if next_word_list:
            next_word = next_word_list[0]
            created_text = created_text + " " + next_word
            created_text_to_list = created_text.split()
            first_word_pair = str(created_text_to_list[-2]) + ' ' + str(created_text_to_list[-1])
        else:
            print('stopped')
    return created_text


def main_function(source_path, word_count):
    text = source_path
    text_data_as_list = get_text_data(text)
    first_pair = get_text_data(text)[0] + ' ' + get_text_data(text)[1]
    created_dictionary = make_dict_from_list(text_data_as_list)
    created_text = make_text_from_dict(first_pair, created_dictionary, word_count)
    print(created_text)
    return created_text
