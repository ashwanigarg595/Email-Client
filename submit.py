import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
import smtplib
import email
from email.header import decode_header
from imapclient import IMAPClient
import pyttsx3
import speech_recognition as sr
import datetime

import imaplib
sender_host = 'smtp.gmail.com'
reciever_host = 'imap.gmail.com'
logintext1="Login to your account."
logintext2="  :(  Enter correct credentials."
logintext3="Logged out, Login to other account."
mainpagetext1='Welcome to Homepage'
mainpagetext2='All unread cleared'
mainpagetext3='Inbox cleared'
intxt='inbox.txt'
sntxt='sent.txt'
inTitle='Inbox'
snTitle='Sentbox'
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voices',voice[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir")
    elif hour>=12 and hour<5:
        speak("Good afternoon sir")
    else:
        speak("good evening sir")

    speak("I am your Email client")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=.5
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio,language='en-in')
    except:
        speak("Say that again please....")
        return "None"
    return query
def main_audio():
    volume = engine.getProperty('volume')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 175)
    speak('what can i do for you sir')
    while True:
        query=takecommand().lower()
        if "compose new" in query or "send an email" in query or "create new " in query:
            speak('opening compose box for you sir')
            compose_new()
        elif "open my inbox" in query or "show inbox" in query or "read my inbox" in query:
            speak('opening inbox for you sir')
            read_inbox()
        elif "delete complete inbox" in query or "delete my complete inbox" in query or "clear my inbox" in query:
            speak('deleting all mails from your inbox sir')
            delete_all_inbox()
        elif "sentbox" in query:
            speak('opening your sent box sir')
            read_sent()
        elif "delete all unseen" in query or "clear all unseen" in query or "remove unseen" in query:
            speak('trying to delete all unseen mails from you inbox sir.')
            delete_unseen()

def show(a,b):
    temp=open(a,'r')
    window=tk.Tk()
    window.geometry("1280x500")
    window.title('Inbox')
    sb=Scrollbar(window)
    sb.pack(side=RIGHT,fill=Y)
    def g():
        window.destroy()
    mylist=Listbox(window,yscrollcommand=sb.set,width=140,font=(None,12),height=50)
    back_button = tk.Button(text="Go Back",bd='5', foreground='Yellow', background='Red',font=(None,15),height=2,command=lambda: [g(),main_page(mainpagetext1)])
    greeting = tk.Label(text=b,bd='8', foreground='Green', background='Black',font=(None,17),width=80,height=2)
    greeting.pack()
    back_button.place(x=0.0)
    for i in temp:
        mylist.insert(END,i)
    mylist.pack(pady=2.0,side=LEFT)
    sb.config(command=mylist.yview)
    window.mainloop()


def  sent_successfully():
    myfont = font.Font(family='Helvetica')
    window4=tk.Tk()
    window4.title("Mail sent")
    label4=tk.Label(text='Your mail has been sent sucessfully',fg='Green',bg='Black',font=(None,15),width=50,height=10)
    label4.pack()
    def e():
        window4.destroy()
    back_button = tk.Button(text="Go Back",bd='5', foreground='Yellow', background='Red',command=lambda: [e(), main_page(mainpagetext1)])
    back_button['font'] = myfont
    back_button.pack()


def error1():
    myfont = font.Font(family='Helvetica')
    window3=tk.Tk()
    window3.title("Error")
    label3=tk.Label(text='Sorry :(   Try again.',fg='Green',bg='Black',font=(None, 15),width=40,height=10)
    label3.pack()
    def e():
        window3.destroy()
    back_button = tk.Button(text="Go Back",bd='5', foreground='Yellow', background='Red',command=lambda: [e(), main_page(mainpagetext1)])
    back_button['font'] = myfont
    back_button.pack()


def compose_new():
    window = tk.Tk()
    window.title('Compose')
    greeting = tk.Label(text="Create new mail", foreground='Green', background='Black', width=60)
    myfont = font.Font(family='Helvetica')
    label5 = tk.Label(text="To")
    label6 = tk.Label(text="Subject")
    label7 = tk.Label(text="Body")
    reciever_id = tk.Entry(bg='pink', fg='green',width=40)
    entrysub = tk.Entry(bg='black', fg='green', width=50)
    entrymain = tk.Text(bg='black', fg='green', width=50, height=10)
    greeting['font'] = myfont
    reciever_id['font'] = myfont
    entrysub['font'] = myfont
    entrymain['font'] = myfont
    def d(reciever_id, entrymain):
        global reciever
        reciever = reciever_id.get()
        global msg1
        msg1 = entrymain.get("1.0", 'end-1c')
        window.destroy()
    sendmail = tk.Button(text="Send",bd='5', foreground='Yellow', background='Red',command=lambda: [d(reciever_id, entrymain), compose2()])
    sendmail['font'] = myfont
    greeting.pack()
    label5.pack()
    reciever_id.pack()
    label6.pack()
    entrysub.pack()
    label7.pack()
    entrymain.pack()
    sendmail.pack()
    def g():
        window.destroy()
    back_button = tk.Button(text="Go Back",bd='5', foreground='Yellow', background='Red',command=lambda: [g(),main_page(mainpagetext1)])
    back_button['font']=myfont
    back_button.pack()
    window.mainloop()


def main_page(mainpagetext1):
    root = tk.Tk()
    root.title('Homepage')
    n=tk.StringVar()
    num=ttk.Combobox(root,width = 5, textvariable = n)
    num['values'] = ('1','2','3','4','5','6','7','8','9','10')
    def a():
        speak('opening compose box sir')
    def b():
        root.destroy()
    greeting = tk.Label(text=mainpagetext1, foreground='Green', background='Black', width=60, height=2,font=(None,15))
    greeting.pack()
    topFrame = Frame(root)
    topFrame.pack()
    myfont = font.Font(family='Helvetica')
    create = tk.Button(topFrame, text='Compose',bd='5', bg='Red', fg='Yellow', width=50, command=lambda: [b(),a(), compose_new()])
    inbox = tk.Button(topFrame, text='Inbox',bd='5', bg='Red', fg='Yellow', width=50, command=lambda:[b(),read_inbox()])
    sent = tk.Button(topFrame, text='Sent',bd='5', bg='Red', fg='Yellow', width=50, command=lambda :[b(),read_sent()])
    delete_all_read = tk.Button(topFrame, text='Delete unseen from Inbox',bd='5', bg='Red', fg='Yellow', width=50,command=lambda:[b(),delete_unseen()])
    delete_all = tk.Button(topFrame, text='Delete complete Inbox',bd='5', bg='Red', fg='Yellow', width=50, command=lambda:[b(),delete_all_inbox()])
    logout = tk.Button(text="Logout", foreground='Green',bd='5', background='Red', command=lambda:[b(),logout_account()])
    control_with_audio = tk.Button(text="Control with audio.", foreground='Green',bd='5', background='Red', command=lambda:[b(),main_audio()])
    create['font'] = myfont
    inbox['font'] = myfont
    sent['font'] = myfont
    delete_all['font'] = myfont
    delete_all_read['font'] = myfont
    logout['font'] = myfont
    control_with_audio['font'] = myfont
    create.pack()
    inbox.pack()
    sent.pack()
    delete_all.pack()
    delete_all_read.pack()
    logout.pack()
    control_with_audio.pack()
    root.configure(bg='#003feb')
    root.mainloop()


def login1(logintext1):
    window1 = tk.Tk()
    window1.title('Login')
    myfont = font.Font(family='Helvetica')
    greeting = tk.Label(text=logintext1, foreground='Green', background='Black',font=(None,15),width=40,height=2)
    label1 = tk.Label(text="Email-Id",bg='#0377fc',font=(None,15),width=40,height=2)
    label2 = tk.Label(text="Password",bg='#0377fc',font=(None,15),width=40,height=2)
    user1 = tk.Entry(text='Username', bg='Black', fg='Green',width=35)
    user1['font'] = myfont
    password1 = tk.Entry(text='Password',show="*", bg='black', fg='Green',width=35)
    password1['font'] = myfont
    def c(user1, password1):
        global user
        global password
        user = user1.get()
        password = password1.get()
        session2 = imaplib.IMAP4_SSL(reciever_host)
        try:
            k=session2.login(user, password)[0]
            speak('you have logged in sir')
            window1.destroy()
            main_page(mainpagetext1)
        except:
            window1.destroy()
            speak('Sir ,maybe credentials were wrong')
            login1(logintext2)
    button = tk.Button(text="Login",bd='5', foreground='Yellow', background='Red',width=10,command=lambda: [c(user1, password1), main_page(mainpagetext1)])
    button['font'] = myfont
    greeting.pack()
    label1.pack(ipady=3)
    user1.pack(ipady=3)
    label2.pack(ipady=3)
    password1.pack(ipady=3)
    button.pack(ipady=3)
    window1.configure(bg='#0377fc')
    window1.mainloop()


def compose2():
    try:
        session = smtplib.SMTP(sender_host, 587)
        session.starttls()
        session.login(user, password)
        session.sendmail(user, reciever, msg1)
        speak('Mail has been sent sucessfully sir')
        compose_new()
        session.quit()
    except:
        error1()


def read_inbox():
    try:
        speak('opening inbox for you')
        session2 = imaplib.IMAP4_SSL(reciever_host)
        session2.login(user, password)
        status, message = session2.select('Inbox')
        message = int(message[0])
        temp=open('inbox.txt','w')
        N=5
        for i in range(message, message - N, -1):
            res, msg2 = session2.fetch(str(i), "(RFC822)")
            for response in msg2:
                if isinstance(response, tuple):
                    msg2 = email.message_from_bytes(response[1])
                    subject = decode_header(msg2["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    from_ = msg2.get("From")
                    temp.write("%s\n" % "  ")
                    temp.write("%s\n" % "From:")
                    temp.write("%s\n" % from_)
                    temp.write("%s\n" % "Subject:")
                    temp.write("%s\n" % subject)
                    temp.write("%s\n" % "*************************************")
        temp.close()
        show(intxt,inTitle)
    except:
        error1()


def logout_account():
    try:
        speak('You have successfully logged out')
        session2 = imaplib.IMAP4_SSL(reciever_host)
        session2.login(user, password)
        login1(logintext3)
    except:
        error1()


def delete_unseen():
    try:
        speak('deleting unseen mails sir')
        session = IMAPClient(reciever_host, ssl=True, port=993)
        session.login(user, password)
        session.select_folder('Inbox')
        delmail = session.search('UNSEEN')
        session.delete_messages(delmail)
        main_page(mainpagetext2)
    except:
        error1()


def delete_all_inbox():
    try:
        speak('deleting all mails sir')
        session = IMAPClient(reciever_host, ssl=True, port=993)
        session.login(user, password)
        session.select_folder('Inbox')
        delmail = session.search('ALL')
        session.delete_messages(delmail)
        main_page(mainpagetext3)
    except:
        error1()


def read_sent():
    try:
        speak('trying to show your sent box sir')
        session2 = imaplib.IMAP4_SSL(reciever_host)
        session2.login(user, password)
        status, message = session2.select('"[Gmail]/Sent Mail"')
        N = 5
        temp=open('sent.txt','w')
        message = int(message[0])
        for i in range(message, message - N, -1):
            res, msg2 = session2.fetch(str(i), "(RFC822)")
            for response in msg2:
                if isinstance(response, tuple):
                    msg2 = email.message_from_bytes(response[1])
                    From = msg2["From"]
                    subject = msg2["Subject"]
                    To = msg2["To"]
                    Bcc = msg2["Bcc"]
                    Body = msg2["Body"]
                    temp.write("%s\n" % "  ")
                    temp.write("%s\n" % "To")
                    temp.write("%s\n" % To)
                    temp.write("%s\n" % "Bcc:")
                    temp.write("%s\n" % Bcc)
                    temp.write("%s\n" % "Subject")
                    temp.write("%s\n" % subject)
                    temp.write("%s\n" % "*************************************")
        temp.close()
        show(sntxt,snTitle)
    except:
        error1()

wishme()
login1(logintext1)

