import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


username = "sarooshtahir22@gmail.com"
password = "090078601"


def send_mail(text = "Email Body", subject = "This subject of Email",
              from_email = "IAS BOT <sarooshtahir22@gmail.com>",to_emails = None):

    # if isinstance(to_emails, list):
    assert isinstance (to_emails, list)

    msg = MIMEMultipart('alternative')
    msg["From"] = from_email
    msg["To"] = ','.join(to_emails)  #to_email is a list but we neec comma seprated value
    msg["Subject"] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    msg_str = msg.as_string()
    #login to my smtp server

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  #starts the server
    server.ehlo() #by default
    server.starttls()  #for secure connection
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


    # with smtplib.SMTP() as server:
    #     server.login()

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # environment variables
# username = 'bot.ias921@gmail.com'
# password = '24iNso001'

# def send_mail(text='Email Body', subject='Hello World', from_email='Hungry Py <hungrypy@gmail.com>', to_emails=None, html=None):
#     assert isinstance(to_emails, list)
#     msg = MIMEMultipart('alternative')
#     msg['From'] = from_email
#     msg['To'] = ", ".join(to_emails)
#     msg['Subject'] = subject
#     txt_part = MIMEText(text, 'plain')
#     msg.attach(txt_part)
#     # if html != None:
#     #     html_part = MIMEText(html, 'html')
#     #     msg.attach(html_part)
#     msg_str = msg.as_string()
#     # login to my smtp server
#     server = smtplib.SMTP(host='smtp.gmail.com', port=587)
#     server.ehlo()
#     server.starttls()
#     server.login(username, password)
#     server.sendmail(from_email, to_emails, msg_str)
#     server.quit()
