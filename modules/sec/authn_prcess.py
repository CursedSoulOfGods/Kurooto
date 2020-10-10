from encrypt_decrypt import load_key_pass_id 
from encrypt_decrypt import decrypt_file
import pickle
from cv2 import cv2
import time
import os
import pyttsx3


base_dir = os.path.dirname(__file__)
req_dir = os.path.dirname(__file__) + "/req/"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getCurrentLock():
    sec_type = "sec_type.KRT"
    file_name = req_dir + sec_type
    get_lock = open(file_name, "r")
    lock_type = get_lock.read()
    lock_type = lock_type.lower()
    get_lock.close()

    if 'face id and pin' in lock_type:
        speak("Please look at, the connected camera, at a suitable angle")
        face_id()
    if 'none' in lock_type:
        speak("No authentication method set, set one in order to prevent anyone from acceessing, would continue without authentication now!")


def password_authn():
    pin = input("Please enter the PIN\n")

    # getting the encryption keys
    key_pin = load_key_pass_id()

    # decryption
    file_name = req_dir + "pin.EKRT"
    actual_password = decrypt_file(file_name, key_pin)
    pin = pin.encode()
    if actual_password == pin:
        speak("Unlock Successful")
        pass
    if actual_password != pin:
        speak('Wrong Passcode, terminating process')
        exit()


def face_id():
    training_data = req_dir + "trainer.yml"
    labels_path = training_data.replace("trainer.yml", "labels.pickle")
    face_cascade = cv2.CascadeClassifier(req_dir + "haarcascade_frontalface_alt2.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(training_data)

    with open(labels_path, "rb") as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)

        # getting cord
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            id_, conf = recognizer.predict(roi_gray)

            if 50 <= conf <= 90:
                cv2.destroyAllWindows()
                speak(f"Recognized person as {labels[id_]}")
                return None

            else:
                speak("Couldn't Recognize your face")
                password_authn()
                quit()
            cv2.imwrite("roi.png", roi_gray)


































'''
if 'password' in lock_type:
    speak("Please input the pin in the provided field")
    password_authn()

'''