import pytest
import pyperclip
from unittest.mock import patch
import tkinter as tk
from project import convert_to_uppercase, convert_to_lowercase, \
                                         convert_to_titlecase, convert_to_sentencecase,\
                                         text_info

# Set a custom value in the clipboard for the test
pyperclip.copy('hello world')
pyperclip.paste()

# Defining needed variables

text = ""
text_in_preview = text
preview_out_label = tk.Label()
lenght_label = tk.Label()
word_count_label = tk.Label()


def test_text_info():

    expected_result = ('hello world', 'hello world')
    assert text_info(text, text_in_preview, preview_out_label, lenght_label, word_count_label) == expected_result

def test_convert_to_uppercase():

    expected_result = "HELLO WORLD"
    assert convert_to_uppercase(text, text_in_preview, preview_out_label) == expected_result

def test_convert_to_lowercase():

    expected_result = "hello world"
    assert convert_to_lowercase(text, text_in_preview, preview_out_label) == expected_result

def test_convert_to_titlecase():

    expected_result = "Hello World"
    assert convert_to_titlecase(text, text_in_preview, preview_out_label) == expected_result

def test_convert_to_sentencecase():

    expected_result = "Hello world"
    assert convert_to_sentencecase(text, text_in_preview, preview_out_label) == expected_result
        