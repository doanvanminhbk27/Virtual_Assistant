
from mypackage.Speak_Hear import *
from mypackage.Myfuntion import *
from mypackage.Library import *
from mypackage.Seach_Open import *


speakEn("Can i help you")

while(True):
    h = hearEn()

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
        break

    else:
        speakEn("i dont understand, you can speak again")