# This is a test calculator program ..
# Program written by:  adarsh dash

from tkinter import *
import datetime
import speech_recognition as sr
import pyttsx3



root=Tk()
root.title("Calculator")
root.geometry("350x550")
root.minsize(350,550)
menu=Menu(root)
menu.add_command(label="exit",command=quit)
root.config(menu=menu)
scvalue=StringVar()
scvalue.set("")
# FUNCTIONS
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
# print(voices[-1].id)
    engine.setProperty('voice', voices[-1].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
def click(event):
    text= event.widget.cget("text")
    
    print(text)
    
    

    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
            
        else:
            try:
                value=eval(screen.get())
               
            except Exception as e:
                value="ERROR"
        speak(scvalue.get())
        scvalue.set(value)
        screen.update()
        speak(value)
        
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        strin=scvalue.set(scvalue.get()+text)
        screen.update()
        
speak("28")
speak("welcome to calculator")

def voice(event):
    wishme()    
    speak("I am Marry sir...... Please tell me how may I help you.....")
        
   # if __name__ == "__main__":
    #    wishMe()



mainframe=Frame(root,bg="#c1c9e6")

f1=Frame(mainframe)
screen=Entry(f1,textvariable=scvalue,font="caliberi 25 ",bg="#edf1ff")
screen.pack(fill=X,pady=5)
f1.pack(pady=20,padx=10)

f2=Frame(mainframe,bg="#c1c9e6")
b=Button(f2,text="1",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f2,text="2",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f2,text="3",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
f2.pack(pady=8,padx=10)

f3=Frame(mainframe,bg="#c1c9e6")
b=Button(f3,text="4",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f3,text="5",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f3,text="6",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
f3.pack(pady=8,padx=10)

f4=Frame(mainframe,bg="#c1c9e6")
b=Button(f4,text="7",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f4,text="8",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f4,text="9",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
f4.pack(pady=8,padx=10)

f5=Frame(mainframe,bg="#c1c9e6")
b=Button(f5,text=".",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f5,text="0",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f5,text="=",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
f5.pack(pady=8,padx=10)

f6=Frame(mainframe,bg="#c1c9e6")
b=Button(f6,text="+",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f6,text="-",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f6,text="*",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
f6.pack(pady=8,padx=10)

f7=Frame(mainframe,bg="#c1c9e6")
b=Button(f7,text="/",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f7,text="%",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
b=Button(f7,text="C",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=4)
f7.pack(pady=8,padx=10)

f8=Frame(mainframe,bg="#c1c9e6")
b=Button(f8,text="<<||>>",padx=35,pady=15,bg="#ebe1f2")
b.bind("<Button-1>",voice)
b.pack(side=RIGHT,padx=4)
f8.pack(pady=8,padx=10)



mainframe.pack()

root.mainloop()
