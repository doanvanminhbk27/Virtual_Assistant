
import numpy
# import speak


f = open("database\\question.txt", mode="r")
ques = f.read().split("\n")                  # mo file question.txt va doc file luu cac cau hoi o dang list()


def handle_data(text):                       # ham xu li du lieu
    text = text.split(" ")                   # chia cau hoi nguoi dung thanh cac tu rieng biet, ngan cach boi dau cach.
    ans = []                                 # list rong de luu ti le % giong nhau giua cau hoi nguoi dung va cau hoi trong question.txt


    for s in ques:                           # tinh toan ti le % tung cau hoi trong database bang for
        count = 0                            # bien dem
        for i in text:
            if i in s:                       # tinh toan so tu trung lap 
                count += 1                   # neu trung thi tang count len 1
    
        ratio = (count * 100) / len(s)           # sau khi tinh duoc so tu trung lap thi se chia cho len(s) de ra %
        ans.append(ratio)                        #append() ti le % vao list ans
    return numpy.argmax(ans)                 # numpy.argmax() tra ve vi tri (index) cua phan tu co gtri lon nhat trong list ans


# doc va ghi lai cac cau tra loi answer.txt o dang list
a = open("database\\answer.txt", mode = "r", encoding="utf8")
answer = a.read().split("\n")


# ind = handle_data("hello")
# speak.speak(answer[ind])

      
