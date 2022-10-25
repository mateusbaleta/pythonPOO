import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'BraiNiac'
email['to'] = 'mateusbalabenute2@gmail.com'
email['subject'] = 'Gotcha!'

email.set_content(html.substitute({'name': 'BraiNiac'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mateusbalabenute@gmail.com', 'kpwnbyofkdvweicd')
    smtp.send_message(email)
    print('all good boss.')
