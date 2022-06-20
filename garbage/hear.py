
#module AL hear
#Chuyen giọng nói thành text tiếng anh.

import speech_recognition as sr

def hear():
    robot_ear = sr.Recognizer()                      # luu class Reognizer voi ten robot_ear de nhan giong nói
    print("Listening:...")
    with sr.Microphone() as source:                  # mo mic luu voi ten source, sau khi thoat with as thi tat mic
        #robot_ear.pause_threshold = 2                          
        audio = robot_ear.listen(source, timeout = 10, phrase_time_limit = 3)     # Thoi gian mo mic toi da
        try:
            text = robot_ear.recognize_google(audio, language="en-IN")        # Chuyen text tieng viet sang tieng anh.
            print(text)
            return(str(text).lower())
        except:
            return None
    

# from speak import *
# while(1):
#     you = hear()

#     if you == "how are you":
#         speak('i dont understand')
#     elif "goodbye" in you:
#         speak("goodbye minh doan")
#         break        