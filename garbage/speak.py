
# module Ai speak
# Chuyen text thanh giong noi


import pyttsx3

robot_mount = pyttsx3.init()                          # Khoi tao doi tuong robot_mount

"""VOICE"""
voices = robot_mount.getProperty('voices')            #getting details of current voice
robot_mount.setProperty('voice', voices[1].id)        #changing index, changes voices. 1 for female
# robot_mount.setProperty('voice', voices[0].id)      #changing index, changes voices. o for male

def speak(text):
    print(text)
    robot_mount.say(text)
    robot_mount.runAndWait()                 # Cai nay bat buoc phai co
    robot_mount.stop()


# speak("can i help you")
# speak("i dont understand")

