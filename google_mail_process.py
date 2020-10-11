import httplib2
import os
import oauth2client
from oauth2client import client, tools, file
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from modules.i_o_engine import *
import time


SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'
email_store_loc = os.path.normpath((os.path.join(os.path.dirname(__file__), "user/mail_service")))
email_store = open(email_store_loc + "\email.KRT", 'r')
SENDER = email_store.read()
email_store.close()

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def SendMessage(sender, to, subject, msg_text):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject, msg_text)
    SendMessageInternal(service, "me", message1)


def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        # print ('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print ('An error occurred: %s' % error)


def CreateMessage(sender, to, subject, msg_text):
    msg = MIMEText(msg_text)
    msg['To'] = to
    msg['From'] = sender
    msg['Subject'] = subject
    return {'raw': base64.urlsafe_b64encode(msg.as_string().encode()).decode()}

def send_email(to):
    speak("What should be the Subject?")
    subject = takeCommand()
    speak("What should I say?")
    msg_text = takeCommand()
    speak("Ok sir, sending mail to " + to + "with the subject being " + subject + ",stating that" + msg_text)
    time.sleep(0.5)
    speak("Are you sure you want to send this mail?")
    choice = takeCommand()
    if 'yes' in choice:
        SendMessage(SENDER, to, subject, msg_text)
        speak("Email has been sent!")
    elif 'no' in choice:
        speak("Ok sir, mail cancelled!")