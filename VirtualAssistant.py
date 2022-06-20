
from mypackage.Speak_Hear import *
from mypackage.Myfuntion import *
from mypackage.Library import *
from mypackage.Seach_Open import *

def Virtual(h):
    global end_out  # global variable
    if "open" in h:
        open_web(h)
        
    elif "for me video" in h:      
        Search_YouTube()
    
    elif "what time" in h:
        whattime()
    
    elif "today" in h:
        today()

    elif "goodbye" in h or "thank you" in h:
        speakEn("goodbye minh doan, see you again")
        end_out = 1

    else:
        speakEn("i dont understand, you can speak again")


if __name__ == '__main__':
    speakEn("Can i help you")
    count_out = 0

    while(True):
        h = hearEn()
        if(h):
            Virtual(h)
            count_out = 0
            if(end_out == 1):
                break
            continue

        else:
            count_out += 1
            if(count_out == 3):
                time.sleep(2)
                speakEn("Not request, good bye")
                break
            continue
            

