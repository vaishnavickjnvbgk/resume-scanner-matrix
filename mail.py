# Import the following module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

# initialize connection to our
# email server, we will use gmail here
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

# Login with your email and password
smtp.login('matrixresumescanner@gmail.com', 'xnevdqohvmwkeetr')


# send our email message 'msg' to our boss
def message(subject="Python Notification",
			text="", img=None,
			attachment=None):
	
	# build message contents
	msg = MIMEMultipart()
	
	# Add Subject
	msg['Subject'] = subject
	
	# Add text contents
	msg.attach(MIMEText(text))

	
	return msg


# Call the message function
msg = message("Greetings from MATRIX_RESUME_SCANNER!", "MATRIX has shortlisted your resume.Hereby you are informed to be prepared accordingly")
			

# Make a list of emails, where you wanna send mail



# creating an empty list
lst = []
  
# number of elements as input
n = int(input("enter the number of email to send the mail : "))
  
# iterating till the range
for i in range(0, n):
    ele = input()
  
    lst.append(ele)
to = lst


# Provide some data to the sendmail function!
smtp.sendmail(from_addr="matrixresumescanner@gmail.com",
			to_addrs=to, msg=msg.as_string())

# Finally, don't forget to close the connection
smtp.quit()
