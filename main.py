#directories shud be empty
import dotenv
import os
import email_extraction
import pdfminer_multiple
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def preprocess(pdf_path,text_path):
    while True:
        

        dotenv.set_key(dotenv_file, "API_PATH_PDF", os.environ["API_PATH_PDF"])
        path=os.environ["API_PATH_PDF"]
       

        if os.path.exists(path+'/'):

            email_extraction.attachment_download(path)
            break

    dotenv.set_key(dotenv_file, "API_PATH_TXT", os.environ["API_PATH_TXT"])
    pdfDir = os.environ["API_PATH_PDF"] + '/'
    txtDir = os.environ["API_PATH_TXT"] +'/'
    pdfminer_multiple.convertMultiple(pdfDir, txtDir)


