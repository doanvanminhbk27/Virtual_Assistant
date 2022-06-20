
#module search_google

import webbrowser
import time

def search_google(text):
    url = "https://www.google.com.vn/search?q=" + text
    webbrowser.open(url)
    time.sleep(2)
    

# search_google("esp8266,gps neo 6m, blynk")