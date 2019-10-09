import imaplib
import base64
import os
import email

from mailvars import *

# Change server address here if not using GMAIL
mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login(email_user, email_pass)

mail.select('Inbox')

#Define senders email and part of subject here
type, data = mail.search(None,'(FROM "somesender@example.com" SUBJECT "JPG")' )

mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]

    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/tmp/', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
