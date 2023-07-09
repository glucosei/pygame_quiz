# -*- coding: utf-8 -*-
import os
import random
from PIL import ImageTk
from tkinter import *
import tkinter.font
import threading
import time
import sys
import os




def init():
    global q1
    global q2
    global a1
    global a2
    global atmosphere
    atmosphere=['대류권','성층권','중간권','열권','우주공간','달']
    q1=[ ]
    q2=[ ]
    a1=[ ]
    a2=[ ]
    file1=open(os.getcwd()+'\\q1.txt',"rt", encoding='UTF8')
    i=0
    while True:
        read=file1.readline().strip()
        if read=='':
            break
        if i%2==0:
            #print(read+'\n'+str(len(read))+'\n')
            if len(read)>=20:
                r=list(read)
                for j in range(20,len(read)):
                    if r[j]==' ':
                        r[j]='\n'
                        read=''.join(r)
                        break
            #print(read)
            q1.append(read)
        else:
            a1.append(read)
        i+=1
    file1.close()

    file2=open(os.getcwd()+'\\q2.txt','rt', encoding='UTF8')
    i=0
    while True:
        read=file2.readline().strip()
        if read=='':
            break
        if i%2==0:
            #print(read+'\n'+str(len(read))+'\n')
            if len(read)>=20:
                r=list(read)
                for j in range(20,len(read)):
                    if r[j]==' ':
                        r[j]='\n'
                        read=''.join(r)
                        break
            #print(read)
            q2.append(read)
        else:
            a2.append(read)
        i+=1
    file2.close()

    #print(q1,q2,a1,a2,sep='\n')

def cmp(k,pAnswer,grade):
    if grade==1:
        #print(k,a1[k],pAnswer)
        if a1[k]==pAnswer:
            return True
        else:
            return False
    else:
        #print(a2[k],pAnswer)
        if a2[k]==pAnswer:
            return True
        else:
            return False

def randQ(grade):
    if grade==1:
        rnum=random.randint(0,len(q1)-1)
        return rnum, q1[rnum]
    else:
        rnum=random.randint(0,len(q2)-1)
        return rnum, q2[rnum]


def destroy(root):
    root.destroy()

def start():
    #win창 생성
    main=Tk()
    main.title("select")
    main.geometry("1000x600+200+100")
    main.configure(bg='#12fb0c')
    main.option_add("*Font","궁서 30")
    #lab레이블 생성
    lab=Label(main,text="로켓 발사 퀴즈 게임!",width='20',height='3')
    lab.pack(pady=30)
    #선택지
    #1: 게임시작
    btn1=Button(main)
    btn1.config(text='게임 시작')
    btn1.config(command=lambda:[fir_sel(main)])
    btn1.pack(pady=30)

    #2: 설명
    btn2=Button(main)
    btn2.config(text='게임 설명')
    btn2.config(command=lambda:[manual(main)])
    btn2.pack(pady=30)
    main.mainloop()

def manual(bef):
    def home(cur_path):
        def DnC():
            cur_path.destroy()
            start()
        btn=Button(cur_path,text="Home",command=DnC,width='5',height='1')
        btn.pack(anchor='nw')
    destroy(bef)
    main=Tk()
    main.title("select")
    main.geometry("1000x600+200+100")
    main.configure(bg='#12fb0c')
    main.option_add("*Font","맑은고딕 25")
    #lab레이블 생성
    home(main)
    label=Label(main,text='게임 설명',width=30,height=4)
    font=tkinter.font.Font(family="맑은 고딕", size=13)
    lab=Label(main,text="-지구와 달까지 거리:384000km\n-대기권에서의 시간은 리얼타임(100초)\n-로켓은 대기권에서 0km/s~20km/s까지 증가하지만 실제와 다르게 등가속도직선 운동함.(고도 1000km까지 대기권)\n-우주에서 시간은 실제보다 957.5배 빠르게 흐름(20초)\n-로켓은 우주에서 20km/s로 등속 직선 운동함.\n-플레이 타임은 약 2분\n-대기해주는 시간은 6.5초\n-문제는 8초마다 나옴\n-처음 문제를 맞춰야 발사가 되는데 이때는 left,right 키로 정답을 맞힘\n-다음 문제 부터는 로켓을 좌우로 움직여서 왼쪽에 있는지 오른쪽에 있는지로 정답을 맞힘\n-총 17문제",width='20',height='3')
    lab.config(width=95,height=15,font=font)
    label.pack(pady=(0,30))
    lab.pack()

def fir_sel(bef):
    #win창 생성
    destroy(bef)
    main=Tk()
    main.title("select")
    main.geometry("1000x600+200+100")
    main.configure(bg='#12fb0c')
    main.option_add("*Font","궁서 30")
    #lab레이블 생성
    lab=Label(main,text="당신은 몇학년인가요?",width='20',height='3')
    lab.pack(pady=30)
    #선택지
    #1: 1학년
    btn1=Button(main)
    btn1.config(text='1학년')
    btn1.config(command=lambda:[game(main,1)])
    btn1.pack(pady=30)

    #2: 2학년
    btn2=Button(main)
    btn2.config(text='2학년')
    btn2.config(command=lambda:[game(main,2)])
    btn2.pack(pady=30)
    main.mainloop()


    

#본게임
def game(main,grade):
    destroy(main)
    global x
    global bgnum
    global speed
    global vartime
    global height
    global q
    global gy
    global mh
    global Img
    global FlipImg
    global cur_atmo
    cur_atmo=1
    mh=0
    q=[ ]
    vartime=0
    speed=0
    bgnum=0
    height=0
    x=0.4
    gy=0.71
    sel1=Tk()
    sel1.title("game")
    sel1.geometry("700x700+400+50")
    sel1.option_add("*Font","굴림 15")
    FlipImg=ImageTk.PhotoImage(file=os.getcwd()+'\\FlipRocket.png')
    Img=ImageTk.PhotoImage(file=os.getcwd()+'\\rocket.png')
    canvas = Canvas(sel1, width = 700, height = 700,bg="#00ffff")
    canvas.place(relwidth=1,relheight=1)
    label=Label(sel1)
    label.config(image=Img,bg='#00ffff')
    label.place(relx=x,rely=0.55,relwidth=0.2,relheight=0.2)
    notlab=Label(sel1, width=50,height=50,bg="#ffffff",text='<info>\n게임시간:0초\n현재속력:0km/s\n현재고도:0km\n현재위치:지구 표면\n0/17')
    notlab.place(relx=0.7,rely=0.01,relwidth=0.3,relheight=0.2)
    line=Label(sel1,bg='#000000')
    line.place(relx=0.5,rely=0,relwidth=0.001,relheight=1)
    xlab=Label(sel1,bg='#ff0000',text='x')
    xlab.place(relx=0.7,rely=0.9,relwidth=0.1,relheight=0.1)
    olab=Label(sel1,bg='#0000ff',text='o')
    olab.place(relx=0.2,rely=0.9,relwidth=0.1,relheight=0.1)
    font=tkinter.font.Font(family="맑은 고딕", size=12)
    qlab=Label(sel1,bg='#ffffff',font=font)
    qlab.place(relx=0.1,rely=0.01,relwidth=0.55,relheight=0.1)
    glab=Label(sel1,bg='#12fb0c')
    glab.place(relx=0,rely=gy,relwidth=1,relheight=0.29)
    mlab=Label(sel1,bg="#FFD400")
    mlab.place(relx=0,rely=0,relwidth=1,relheight=0)
    Lcolor=[ ]
    color="ffff"
    Lcolor.append("#00"+color)
    for i in range(509):
        if int(color,16)-256>255:
            color=hex(int(color,16)-256)
            if int(color,16)>=4096:
                Lcolor.append("#00"+color[-4:])
            else:
                Lcolor.append("#000"+color[-3:])
        else:
            color=hex(int(color,16)-1)
            if int(color,16)-1>16:
                Lcolor.append("#0000"+color[-2:])
            else:
                Lcolor.append("#00000"+color[-1:])
    
    def bgMover():
        global bgnum
        global gy
        global vartime
        global mh
        if gy<1:
            gy+=0.05
            glab.place_forget()
            glab.place(relx=0,rely=gy,relwidth=1,relheight=0.29)
        elif gy==1:
            gy+=0.05
            glab.place_forget()
        if bgnum<510:
            color=Lcolor[bgnum]
            canvas.config(bg=Lcolor[bgnum])
            label.config(bg=Lcolor[bgnum])
            bgnum+=1
        
        elif vartime>=115 and mh<0.55:
            mh+=0.022
            mlab.place_forget()
            mlab.place(relx=0,rely=0,relwidth=1,relheight=mh)
            line.place_forget()
        sel1.after(200,bgMover)
    
    def obsMover():
        global height
        global cur_atmo
        if height<=11:
            cur_atmo=0
        elif height<=50:
            cur_atmo=1
        elif height<=80:
            cur_atmo=2
        elif height<=1000:
            cur_atmo=3
        elif height<=380000:
            cur_atmo=4
        else:
            cur_atmo=5
        sel1.after(100,obsMover)
    def TS():
        global speed
        global vartime
        global height
        global cur_atmo
        global atmosphere
        if vartime<100:
            vartime+=0.1
            height+=0.1*speed
            speed+=0.02
        elif vartime<120:
            vartime+=0.1
            height+=95.75*speed
        elif vartime>=120:
            success(sel1)
        if 114<=vartime<=114.5:
            #print('1')
            label.config(image=FlipImg)
        notlab.config(text="<info>\n게임시간:%.1f초\n현재속력:%.1fkm/s\n현재고도:%.1fkm\n현재위치:%s\n%d/17"%(vartime,speed,height,atmosphere[cur_atmo],len(q)))
        sel1.after(100,TS)
    
    def questioner(grade):
        
        #debugpy.debug_this_thread()
        global q
        if len(q)>=17:
            return
        qnum,msg=randQ(grade)
        if qnum in q:
            sel1.after(10,lambda:[questioner(grade)])
            return
        #print(qnum)
        qlab.config(text=msg+'\nO는 <-, X는 ->')
        qlab.place(relx=0.1,rely=0.01,relwidth=0.55,relheight=0.1)
        sel1.after(6500,lambda:[check(grade)])
        def check(grade):
            bool=False
            if x>=0.4:
                #print('x')
                bool=cmp(qnum,'x',grade)
            else:
                #print('o')
                bool=cmp(qnum,'o',grade)

        
            if bool==False:
                gameover(sel1)
                return
            else:
                #print('app')
                q.append(qnum)
                qlab.place_forget()
            sel1.after(1500,lambda:[questioner(grade)])
 

    def up():
        sel1.update()
        sel1.after(100,up)

    def keyPressHandler(event):
        global x
        key=event.keycode
        #print("Press: ",event.keycode)
        if key==39:
             #print('r')
             x+=0.01
        elif key==37:
            #print('l')
            x-=0.01
        label.place_forget()
        label.place(relx=x,rely=0.55,relwidth=0.2,relheight=0.2)


    qnum,msg=randQ(grade)
    qlab.config(text=msg+'\nO는 <-키, X는 ->키')
    t1=threading.Thread(target=bgMover,daemon=True)
    t2=threading.Thread(target=TS,daemon=True)
    t3=threading.Thread(target=up,daemon=True)
    t4=threading.Thread(target=lambda:[questioner(grade)],daemon=True)
    t5=threading.Thread(target=obsMover,daemon=True)
    def firQ(event):
        key=event.keycode
        bool=False
        if key==39:
            bool=cmp(qnum,'x',grade)
        elif key==37:
            bool=cmp(qnum,'o',grade)
        if bool==False:
            gameover(sel1)
            return
        else:
            global q
            q.append(qnum)
            qlab.place_forget()
            sel1.unbind("<KeyPress>")
            sel1.bind("<KeyPress>",keyPressHandler)
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
    sel1.bind("<KeyPress>",firQ)
    
    sel1.mainloop()
    



        
#게임오버
def retry(bef):
        destroy(bef)
        mh=0
        gy=0.75
        x=0.55
        bgnum=0
        speed=0
        vartime=0
        height=0 
        q.clear()
        start()




def gameover(bef):
    destroy(bef)
    over=Tk()
    over.title("over")
    over.geometry("600x600+400+50")
    over.configure(bg='#ff0000')
    over.option_add("*Font","궁서 30")
    lab=Label(over,text='게임오버\n\n'+str(len(q))+'개의 문제를 맞힘',bg="#ff0000")
    lab.pack(pady=(200,0))
    btn=Button(over,text="다시 플레이 하기",command=lambda:[retry(over)],width='15',height='10',bg='#ffffff')
    btn.pack(pady=100)
    over.mainloop()



def success(bef):
    destroy(bef)
    success=Tk()
    success.title("success")
    success.geometry("600x600+400+50")
    success.configure(bg='#12fb0c')
    success.option_add("*Font","궁서 30")
    lab=Label(success,text='게임 클리어를 축하합니다!!!',bg="#12fb0c")
    lab.pack(pady=(200,0))
    btn=Button(success,text="다시 플레이 하기",command=lambda:[retry(success)],width='15',height='10',bg='#ffffff')
    btn.pack(pady=100)
    success.mainloop()



sys.setrecursionlimit(10000)
init()
start()
