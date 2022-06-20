
from mypackage.Library import *
from mypackage.Speak_Hear import *

def whattime():
    now = datetime.now().strftime('%H hour %M minutes')
    speakEn(now)

def today():
    now = datetime.now().strftime('%B %d, %Y')
    speakEn(now)





