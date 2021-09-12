import docx2txt


def docx_to_list():
    text = docx2txt.process('example.docx')
    return text.split()
