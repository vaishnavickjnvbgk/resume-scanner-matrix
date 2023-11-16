import pdfminer_single
import os
import sys, getopt
import streamlit as st

x=0
def convertMult(pdfDir, txtDir):
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
            fileExtension = pdf.split(".")[-1]
            if fileExtension == "pdf":
                pdfFilename = pdfDir + pdf
                text = pdfminer_single.convert(pdfFilename) #get string of text content of pdf
                textFilename = txtDir + pdf + ".txt"
                textFile = open(textFilename, "w") #make text file
                textFile.write(text) #write text to text file        
        
                        
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    if os.path.exists(pdfDir) and os.path.exists(txtDir) :
        convertMult(pdfDir, txtDir)
                #textFile.close


