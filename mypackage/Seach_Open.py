
#module Search_YouTube

from youtube_search import YoutubeSearch
from mypackage.Speak_Hear import *
import webbrowser           # module nay dung de mo web
import time


def Search_YouTube():
    text = hearVn()
    while True:                                                               # su dung vong while tim kiem cho den khi nao co ket qua
        result = YoutubeSearch(text, max_results=10).to_dict()                 # result luu kp duoi dang dic
        if result:
            break

    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    time.sleep(2)
    speakEn("The video you requested has been found")
    
# Search_YouTube("Tom and jerry")

'''================================================================================================================='''

#module Search_Google

def search_google(text):
    url = "https://www.google.com.vn/search?q=" + text
    webbrowser.open(url)
    time.sleep(2)
    speakEn('Your request is done')
    

# search_google("esp8266,gps neo 6m, blynk")

'''================================================================================================================='''


#module open facebook

def open_web(text):
    if "facebook" in text:
        webbrowser.open("https://www.facebook.com/")
        time.sleep(2)
        speakEn("facebook has been opened")
    if "zalo" in text:
        webbrowser.open("https://chat.zalo.me/")
        time.sleep(2)
        speakEn("zalo has been opened")
    if "youtube" in text:
        webbrowser.open("https://www.youtube.com/")
        time.sleep(2)
        speakEn("youtube has been opened")

'''================================================================================================================='''