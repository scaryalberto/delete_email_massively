username = #insert personal email to clean
password = #insert email' password to clean
mail_server = #insert email server, for example: 'outlook.office365.com', 'imap.gmail.com'

import imaplib
import time

#list with all email address to dolete
email_spam = []

for from_email in email_spam:
    mail = imaplib.IMAP4_SSL(mail_server)
    mail.login(username, password)
    #chose folder
    mail.select('inbox')

    status, data = mail.search(None, f'FROM "{from_email}"')

    print(from_email, " -> ", (len(data[0].split())))

    mail_ids = []

    for block in data:
        mail_ids += block.split()

    for i in mail_ids:

        try:
            status, data = mail.fetch(i, '(RFC822)')
            resp_code, response = mail.store(i, "+FLAGS", "\Deleted")
            resp_code, response = mail.expunge()
            time.sleep(5)
            print("SPAM deleted")

        except:
            print("ERROR: ")
            continue
    resp_code, response = mail.expunge()

print("#FINISHED MAIL")
