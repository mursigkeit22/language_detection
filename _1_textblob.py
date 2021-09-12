""" textblob uses google API, so makes an API call for every word and has rate limits.
Also it needs pauses between API calls, so is very slow.
SUITABLE ONLY FOR VERY SHORT DOCUMENTS ~ 2500 CHARACTERS


2553645dsg EN
sfDFGdf4245 EN
253536588 EN
DHGFHJGKR GD
3454DD AR
"""
import urllib
from time import sleep

from textblob import TextBlob
import docx2txt

text = docx2txt.process('example.docx')
print(len(text))
# print(text)
split_text = text.split()
# print(splited_text)
for el in split_text:
    try:
        if len(el) >= 3:
            b = TextBlob(el)
            print(el, b.detect_language().upper())
        else:
            print(el, "too short")
    except urllib.error.HTTPError as ex:
        sleep(1)
        try:
            b = TextBlob(el)
            print(el, b.detect_language().upper())
        except urllib.error.HTTPError as ex:
            print(el, ex)

    sleep(0.5)
