## pip install googletrans==4.0.0-rc1
""" ограничений по количеству запросов вроде бы нет,
но буквенно-цифровые коды распознает не как англ:
DHGFHJGKR gd
3454DD ar
"""
from googletrans import Translator

from _0_read_docx import docx_to_list

word_list = docx_to_list()

for el in word_list:
    t = Translator().detect(el)
    if t.lang != "en":
        print(el, t.lang)
