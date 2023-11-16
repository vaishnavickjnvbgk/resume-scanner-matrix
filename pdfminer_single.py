from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import PyPDF2
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    myFile = open(fname, "rb")
    pdfReader = PyPDF2.PdfFileReader(myFile)
    numOfPages = pdfReader.numPages
    for i in range(numOfPages):
        page = pdfReader.getPage(i)
        text = page.extractText()
        
    
    myFile.close()
    return text