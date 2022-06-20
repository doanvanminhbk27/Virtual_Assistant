
# module Ai speak
# Chuyen text thanh giong noi tieng anh


import pyttsx3

robot_mount = pyttsx3.init()                          # Khoi tao doi tuong robot_mount

"""VOICE"""
voices = robot_mount.getProperty('voices')            #getting details of current voice
robot_mount.setProperty('voice', voices[1].id)        #changing index, changes voices. 1 for female
# robot_mount.setProperty('voice', voices[0].id)      #changing index, changes voices. o for male

def speakEn(text):
    print(text)
    robot_mount.say(text)
    robot_mount.runAndWait()                 # Cai nay bat buoc phai co
    robot_mount.stop()


# speak("can i help you")
# speak("i dont understand")


'''================================================================================================================='''

# module Ai speak
# Chuyen text thanh giong noi tieng viet

# module speak 

from gtts import gTTS                # Bien text thanh am thanh
import playsound                     # Phat am thanh
import os


def speakVn(text):
    print("..." + text)
    tts = gTTS(text = text, lang= "vi", slow=False)         # Bien tts luu Class gtts.......chuyen text thanh am thanh qua API google
    tts.save("sound.mp3")                                   # sau khi gg gui am thanh ve se luu duoi ten sound.mp3
    playsound.playsound("sound.mp3", True)                  # phat file sound.mp3...true: se khong chay chuong trinh cho den khi am thanh chay xong
    os.remove("sound.mp3")                                  # xoa file sound.mp3 de tranh xay ra loi...



# speak("Xin chào tôi tên là john")
# speak("Lần sau mấy cái dễ dễ này tự đi mà làm, đừng có mà nhờ tao...")
# speak("i'm fine thanks")


'''================================================================================================================='''


#module AL hear
#Chuyen giọng nói thành text tiếng anh.

import speech_recognition as sr

def hearEn():
    robot_ear = sr.Recognizer()                      # luu class Reognizer voi ten robot_ear de nhan giong nói
    print("Listening:...")
    with sr.Microphone() as source:                  # mo mic luu voi ten source, sau khi thoat with as thi tat mic
        #robot_ear.pause_threshold = 2                          
        audio = robot_ear.listen(source, timeout = 5, phrase_time_limit = 3)     # Thoi gian mo mic toi da
        try:
            text = robot_ear.recognize_google(audio, language="en-IN")        # Chuyen text tieng viet sang tieng anh.
            print(text)
            return(str(text).lower())
        except:
            return None
    



'''================================================================================================================='''

#module AL hear
#Chuyen giọng nói thành text tiếng việt
def hearVn():
    robot_ear = sr.Recognizer()                                     # luu class Reognizer voi ten robot_ear
    print("Search Video:...")
    with sr.Microphone() as source:                                 # mo mix luu voi ten source, sau khi thoat with as thi tat mic
        audio = robot_ear.listen(source, timeout = 5, phrase_time_limit = 3)       #luu lai am thanh duoi dang mp3
        try:
            text = robot_ear.recognize_google(audio, language="vi-VN")
            print(text)
            return(str(text).lower())
        except:
            return None

