#module searchYouTube

from youtube_search import YoutubeSearch
import webbrowser
import time

def Search_YouTube(text):

    while True:                                                               # su dung vong while tim kiem cho den khi nao co ket qua
        result = YoutubeSearch(text, max_results=10).to_dict()                 # result luu kp duoi dang dic
        if result:
            break

    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    time.sleep(2)
    

# Search_YouTube("Tom and jerry")
