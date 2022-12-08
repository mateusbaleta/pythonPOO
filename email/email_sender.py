import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'email'
email['subject'] = 'Gotcha!'

email.set_content(html.substitute({'name': 'yourName'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'pass')
    smtp.send_message(email)
    print('all good boss.')
