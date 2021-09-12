## pip install guess_language-spirit

"""
it needs >= 20 characters to make a language determination
"""
from guess_language import guess_language
from _0_read_docx import docx_to_list

word_list = docx_to_list()

for el in word_list:
    print(el, guess_language(el))