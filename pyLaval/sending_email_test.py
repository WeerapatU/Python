import smtplib
import os
from os.path import basename
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from time import gmtime, strftime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import Encoders
from email.message import Message
from email.header import Header


def send_mail(send_from, send_to, subject, text, files,
              server):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
        
    msg.attach(MIMEText(text))

    for f in os.listdir(src_dir):
        f = os.path.join(src_dir, files)
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.set_debuglevel(True)
    smtp.ehlo()
    smtp.starttls()
    smtp.login("YOUR-EMAIL-ADDRESS", "YOUR-PASSWORD")   ### <------------------CHANGE HERE
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    smtp.close()

if __name__ == '__main__':
    strftime("%Y-%m-%d")
    src_dir = "/home/joey/research/cronTest/"
    send_mail(send_from='FROM_WHERE', send_to="TO_WHERE", subject=("Cyber Green update "+strftime("%Y-%m-%d")), 
    text=("Hello, \n\nThis test of sending email. "+ strftime("%Y-%m-%d") + "\n\nHave a nice day!\n\nGodzilla"), 
    files="test.txt", server="smtp.gmail.com") ### <-----------------CHANGE HERE

