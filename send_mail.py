#!/usr/bin/env python3
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from datetime import date

def send(dog_problems, interventions, new_wave):
    fromEmail = 'matthewevansterbeek@gmail.com'
    toEmail = 'matthewevansterbeek@gmail.com'
    subject = "Vinyl Stock Update - " + str(date.today())

    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = subject

    body = "<p>" + dog_problems + "</p><p>" + interventions + "</p><p>" + new_wave + "</p>"
    msg.attach(MIMEText(body, 'html'))

    # my_file = open(filename, 'rb')
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((my_file).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', 'attachment; filename= '+ filename)
    # msg.attach(part)

    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromEmail,'psomorpbcrbfirsc')

    server.sendmail(fromEmail, toEmail, message)
    server.quit()