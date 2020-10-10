import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sumangalamavtarsharma@gmail.com', 'idontknowthepassword')
    server.sendmail('sumangalamavtarsharma@gmail.com', to, content)
    server.close()
