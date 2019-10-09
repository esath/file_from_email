# file_from_email
Download attachments from IMAP-server with Python

In this sample we'll check gmail inbox and download all JPEG-files from defined sender

You can store your credentials to other .py file and compile it to hide username password.
Note: Anyone can anyway dig your credentials if they have that compiled file. Don't share that!

In gmail you have to enable insecure connections!

1. Compile mailvars.py:
    python compile.py
2. Delete original mailvars.py
3. run: readmail.py

Change destination directory inside 'readmail.py'. Default is /tmp/ 

Thanks:
https://medium.com/@sdoshi579/to-read-emails-and-download-attachments-in-python-6d7d6b60269
