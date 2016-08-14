# _*_ coding: utf-8 _*_

import io


from random import choice


def get_text_data(text):
    """Return text from a file as a list"""
    input_file = io.open(text, encoding="utf-8")
    text_data = input_file.read()
    input_file.close()
    return text_data.split()


def make_dict_from_list(word_list):
    """Return a dictionary created from the source text"""
    kata_dict = {}
    for i in range(len(word_list) - 2):
        kata_key = ' '.join(word_list[i:i+2])
        kata_dict.setdefault(kata_key, []).append(word_list[i + 2])
    return kata_dict


def make_text_from_dict(first_word_pair, created_dictionary, new_text_length):
    """Return text created using the created dictionary"""
    created_text = first_word_pair
    for i in range(int(new_text_length) - 2):
        try:
            next_word_list = created_dictionary[first_word_pair]
        except KeyError:
            break
        else:
            created_text = created_text + " " + choice(next_word_list)
            first_word_pair = ' '.join(created_text.split()[-2:])
    return created_text


def main_function(text_path, word_count):
    """Return newly created text based on the source text and word count"""
    first_pair = ' '.join(get_text_data(text_path)[:2])
    created_dictionary = make_dict_from_list(get_text_data(text_path))
    created_text = make_text_from_dict(first_pair, created_dictionary,
                                       word_count)
    print(created_text)
    return created_text


if __name__ == '__main__':
    import sys
    source_path = sys.argv[1]
    word_count = sys.argv[2]
    main_function(source_path, word_count)
