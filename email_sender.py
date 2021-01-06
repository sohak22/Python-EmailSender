import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib import Path 

html = Template(Path('index.html').read_text())
email= EmailMessage()
email['from']= '<Name>'
email['to'] = '<to email address>'
email['subject']= 'You are a Python Master!'

email.set_content(html.substitute({'name': 'Harry Potter'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<your email address>', '<your password>')
	smtp.send_message(email)
	print('all good boss!')