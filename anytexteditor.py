from tkinter import *   
from tkinter.filedialog import asksaveasfilename ,askopenfilename  
from tkinter.messagebox import showinfo
r=Tk()   
r.geometry('500x500')  
file=None

r.title('Untitled-ANY TEXT EDITOR')

def saveas():  
    global textarea,file
    file=asksaveasfilename(defaultextension='.txt',filetypes=[ ('Text Documents','.txt') ,('All Files','.')])  
    r.title(str(file)+'  ANY TEXT EDITOR')
    try:   
        f=open(file,mode='w')  
        f.write(textarea.get(1.0,END))  
        f.close()
        showinfo('ANY TEXT EDITOR',"FILE SAVED  SUCCESSFULLY")
    except:  
        pass
def openit():  
    global textarea ,file,labelf ,r
    try:
        file=askopenfilename(defaultextension='.txt',filetypes=[ ('Text Documents','.txt'), ('All Files','.')]) 
        f=open(file,mode='r')
        r.title(str(file))
        textarea.delete(1.0,END)  
        cont=f.read()  
        textarea.insert(1.0,cont)  
        f.close()
    except:  
        pass
def deletealltext(): 
    global textarea,file
    textarea.delete(1.0,END)
    file=None
def newfile():
    global file,textarea  
    file=None  
    textarea.delete(1.0,END)  
    r.title('Untitled-ANY TEXT EDITOR')
textarea=Text(r,font='arial 21 bold',width=500,height=400,pady=100,bg='yellow') 
textarea.pack(expand=True,fill=BOTH)
button=Button(r,text='SAVE CURRENT TEXT ',command=saveas,font='arial 13 bold') 
button.place(x=140,y=10)
button2=Button(r,text="OPEN  FILE",command=openit,font='arial 13 bold')  
button2.place(x=20,y=10)
button4=Button(r,text='DELETE ALL TEXT',command=deletealltext,font='arial 13 bold')
button4.place(x=380,y=10)
button5=Button(r,text='NEW FILE',command=newfile,font='arial 13 bold')
button5.place(x=570,y=10)
Scroll = Scrollbar(textarea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=Scroll.set)
label2=Label(r,text='ANY TEXT EDITOR',font='arial  20 bold',bg='yellow')
label2.place(x=600,y=40)
canas=Canvas(r,width=2000,height=10,bg='black') 
canas.place(x=0,y=80)
canas2=Canvas(r,width=2000,height=10,bg='black') 
canas2.place(x=0,y=740)
def make_menu(w):    
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")
def show_menu(e):
    w = e.widget
    global the_menu
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)
make_menu(r)
textarea.bind_class("Text", "<Button-3><ButtonRelease-3>", show_menu)
backgroundcolor=None
backgroundcolor=StringVar()  
fontcolor=None  
fontcolor=StringVar() 
fontsize=None 
fontsize=StringVar()    
ent1=Entry(r,textvariable=backgroundcolor,font='arial 12 bold',bd=6)  
ent1.place(x=100,y=760)
ent1=Entry(r,textvariable=fontcolor,font='arial 12 bold',bd=6)  
ent1.place(x=410,y=760)
ent2=Entry(r,textvariable=fontsize,font='arial 12 bold',bd=6)  
ent2.place(x=670,y=760)
def set_bg_color():   
    try:
        global backgroundcolor  ,textarea
        color=backgroundcolor.get()   
        textarea['bg']=str(color)
    except:   
        pass
def set_fg_color():   
    try:
        global fontolor  ,textarea
        color=fontcolor.get()   
        textarea['fg']=str(color)
    except:   
        pass
def set_font_sz(): 
    try:
        global fontsize ,textarea  
        sz=fontsize.get()   
        textarea['font']='arial '+str(sz)+' bold'
    except:  
        showinfo('ANY TEXT EIDTOR',"MUST BE INTEGER VALUE")
def set_def():
    global textarea
    textarea['font']='arial 21 bold'
def set_f():
    global textarea
    textarea['fg']='black'
def set_b():
    global textarea
    textarea['bg']='yellow'
def set_all():
    global textarea
    textarea['bg']='yellow'
    textarea['fg']='black'
    textarea['font']='arial 21 bold'
button6=Button(r,text='SET BACKGROUND COLOR',font='arial 12 bold',command=set_bg_color)  
button6.place(x=100,y=800)
button7=Button(r,text='SET FONT COLOR',font='arial 12 bold',command=set_fg_color)  
button7.place(x=410,y=800)
button8=Button(r,text='SET FONT SIZE',font='arial 12 bold',command=set_font_sz)
button8.place(x=670,y=800)
button9=Button(r,text='SET DEFAULT FONT SIZE',font='arial 12 bold',command=set_def)
button9.place(x=910,y=800)
button9=Button(r,text='SET DEFAULT FONT COLOR',font='arial 12 bold',command=set_f)
button9.place(x=910,y=760)
button10=Button(r,text='SET DEFAULT BACKGROUND COLOR',font='arial 12 bold',command=set_b)
button10.place(x=1210,y=760)
button10=Button(r,text='SET ALL DEFAULT',font='arial 12 bold',command=set_all)
button10.place(x=1210,y=800)
r.mainloop()
