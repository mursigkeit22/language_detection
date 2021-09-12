"""
USELESS FOR WORDS:
determine codes and many other english words as non-english:
2553645dsg da
sfDFGdf4245 da
253536588 No features in text.
DHGFHJGKR de
3454DD de

corresponding it
properties it
file ro
"""
import langdetect
from langdetect import detect

from _0_read_docx import docx_to_list

word_list = docx_to_list()

for el in word_list:
    try:
        lang = detect(el)
        print(el, lang)
    except langdetect.lang_detect_exception.LangDetectException as ex:
        print(el, ex)