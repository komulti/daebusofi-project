# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)

# file = drive.CreateFile({'title' : 'test.txt',
#             'parents' : [{'id' : '755019657138-edrdeiofdsfu5am4e6evrf9f6n22up2a'}]})
# file.SetContentString("Hello World !\n")
# file.Upload()

# import multiprocessing
# import time

# #시작시간
# start_time = time.time()

# 멀티쓰레드 사용 하는 경우 (20만 카운트)
# Pool 사용해서 함수 실행을 병렬
# def count(name):
#     for i in range(1,50001):
#         print(name," : ",i)

# num_list = ['p1', 'p2', 'p3', 'p4']

# if __name__ == '__main__':
#     #멀티 쓰레딩 Pool 사용
#     pool = multiprocessing.Pool(processes=2) # 현재 시스템에서 사용 할 프로세스 개수
#     pool.map(count, num_list)
#     pool.close()
#     pool.join()

# print("--- %s seconds ---" % (time.time() - start_time))


# import re

# 전용면적 = '조 1,901.7235'
# 전용면적 = re.sub(r'[^0-9.,]', '', 전용면적)
# print('전용면적: ', 전용면적)


def check_number(text):
    import re
    regex = re.compile(r'((-)?\d{1,3}(,\d{3})*(\.\d+)?)')
    search = regex.search(text)   
    print(search.group(1))
    
# check_number('조 101.7235')

전체주소 = '경기도 평택시 비전동 236-22외 1필지 동아목련아파트 제101동 제16층 제1610호'
동호수여부 = False
주소list = 전체주소.split(' ')
if '동' in 주소list[-3] and '층' in 주소list[-2] and '호' in 주소list[-1]:
    동호수여부 = True
    주소_호 = 주소list[-1].replace('제','').replace('호','')
    주소_층 = 주소list[-2].replace('제','').replace('층','')
    주소_동 = 주소list[-3].replace('제','').replace('동','')
    print('주소_동:',주소_동,'주소_층:',주소_층,'주소_호:',주소_호)

# import tkinter
# import customtkinter

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
# root_tk.geometry("400x240")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=root_tk, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# root_tk.mainloop()

# import pyautogui

# pyautogui.sleep(1)
# pyautogui.scroll(-1000)
# pyautogui.sleep(2)
# pyautogui.scroll(1000)
# pyautogui.sleep(2)
# pyautogui.hotkey('command','t')

# px=list(range(0,10))
# px[0] = 'A'
# px.append('X')
# px.insert(0,'Y')
# del px[0]
# print(px)

def zip_function():
    words = ['as', 'you', 'wish']
    counts = [3,2,5]
    for word,count in zip(words,counts):
        print(word,count)
        x =[]
        x.append(word)
        x.append(count)
        print(x)
# zip_function()

def convert(price):
    price = price
    if "억" in price:
        a = price.split('억')[0].strip()
        b = price.split('억')[1].replace('만', "").zfill(4).strip()
        return a + b
    else:
        c = price.replace('만', "").zfill(4)
        return c
# print(convert('5억100'))
