
import imaplib
import base64
import os
import email
from decouple import config
import os
import dotenv

def attachment_download(path):

    email_user = 'vaishuck30@gmail.com'
    email_pass = 'snbk zdtc mzhi tuay'
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(email_user, email_pass)
    mail.select('Inbox')
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]# converts byte literal to string removing b''
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)# downloading attachments
        for part in email_message.walk():
            # this part comes from the snipped I don't understand yet... 
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()        
            if bool(fileName):
                filePath = os.path.join(path, fileName)
                if not os.path.isfile(filePath) :   #to check if file already exists #what if the person applies multple times
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()            
                    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                    print('Downloaded "{file}" from email titled "{subject}".'.format(file=fileName, subject=subject))
