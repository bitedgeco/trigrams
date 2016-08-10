# _*_ coding: utf-8 _*_

import io


def get_text_data(text):
    input_file = io.open(text, encoding="utf-8")
    text_data = input_file.read()
    input_file.close()
    return text_data
