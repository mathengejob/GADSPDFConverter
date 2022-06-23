from pdf2docx import Converter

pdf_file = 'input/_1.pdf'
docx_file = 'output/_1.docx'


def main():
    convt(pdf_file, docx_file)


# convert pdf to docx
def convt(myinput, myoutput):
    cv = Converter(myinput)
    cv.convert(myoutput)  # all pages by default
    cv.close()


if __name__ == '__main__': main()
