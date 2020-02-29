from tkinter import *
from tkinter import Label,Button,messagebox
#import sendsms
from tkinter import ttk
import re, os, webbrowser
from math import ceil
from tkinter.ttk import Style
import tkinter as tk
from tkinter import filedialog
import zipfile
from PIL import ImageTk, Image, ImageEnhance
from tkcalendar import DateEntry, Calendar
import mysql.connector as mysql
import time
from datetime import datetime

class Student:
    
    def __init__(self,root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1350x700+0+0')
        
        title=Label(self.root,text="Room Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg='white',fg='blue')
#        title.place(x=0,width=1300)
        title.pack(side=tk.TOP,fill=X)
        
        homebttn = Button(self.root,text='Home',command=self.Home)
        homebttn.place(relx=0.98,rely=0.022,relwidth=0.05,anchor='ne')
        
        exitbttn = Button(self.root,text='Quit',command=lambda: Student.ExitApplication(self))
        exitbttn.place(relx=0.98,rely=0.058,relwidth=0.05,anchor='ne')
        
    #=======Variables=============
        v_rent = IntVar()
        v_maint = IntVar()
        v_cook = IntVar()        
        v_maid = IntVar()
        v_internet = IntVar()
        v_ebill = IntVar()
        common_share = IntVar()
        
    #=======Fixed Vaues======================
        self.rentamt = 10500
        self.maintamt = 100
        self.cookamt = 3500
        self.maidamt=1500
        self.internetamt = 800
        self.ebillamt = 700
        
        self.common_share = round((self.rentamt+self.maintamt+self.cookamt+self.maidamt+self.internetamt+self.ebillamt)/3)
    #=======Common Share Frame=========    
        self.Common_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        self.Common_Frame.place(x=20,y=100,width=400,height=580)
        
        m_title = Label(self.Common_Frame,text="Common Share",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        m_title.grid(row=0,columnspan=2,pady=20,padx=100)
        
        lbl_Rent = Label(self.Common_Frame,text="Room Rent",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        lbl_Rent.grid(row=1,column=0,sticky="w",pady=10)
        
        txt_Rent = Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,text=v_rent)
        v_rent.set(self.rentamt)
        txt_Rent.grid(row=1,column=1,sticky='w',pady=10,padx=10)
        
        lbl_Maint = Label(self.Common_Frame,text="Maintenance",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        lbl_Maint.grid(row=2,column=0,sticky="w",pady=10)
        
        txt_Maint = Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,text=v_maint)
        v_maint.set(self.maintamt)
        txt_Maint.grid(row=2,column=1,sticky='w',pady=10,padx=10)
        
        lbl_Cook = Label(self.Common_Frame,text="Cook",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        lbl_Cook.grid(row=3,column=0,sticky="w",pady=10)
        
        txt_Cook = Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,text=v_cook)
        v_cook.set(self.cookamt)
        txt_Cook.grid(row=3,column=1,sticky='w',pady=10,padx=10)

        lbl_Maid = Label(self.Common_Frame,text="Maid",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        lbl_Maid.grid(row=4,column=0,sticky="w",pady=10)
        
        txt_Maid = Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,text=v_maid)
        v_maid.set(self.maidamt)
        txt_Maid.grid(row=4,column=1,sticky='w',pady=10,padx=10)
        
        lbl_Internet = Label(self.Common_Frame,text="Internet",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        lbl_Internet.grid(row=5,column=0,sticky="w",pady=10)
        
        txt_Internet = Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,text=v_internet)
        v_internet.set(self.internetamt)
        txt_Internet.grid(row=5,column=1,sticky='w',pady=10,padx=10)
        
        lbl_Ele = Label(self.Common_Frame,text="Electricity",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        lbl_Ele.grid(row=6,column=0,sticky="w",pady=10)
        
        txt_Ele = Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,text=v_ebill)
        v_ebill.set(self.ebillamt)
        txt_Ele.grid(row=6,column=1,sticky='w',pady=10,padx=10)
        
        combttn = Button(self.Common_Frame,text='Calculate Common Share',width=25,command=lambda: Student.common_share(self))
        combttn.place(x=100,y=450)


        
    #=======Individual Share Frame=========    
        Individual_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Individual_Frame.place(x=450,y=100,width=410,height=580)
        
        i_title = Label(Individual_Frame,text="Individual Share",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        i_title.grid(row=0,columnspan=2,pady=20,padx=100)

        self.lbl_Vinesh_i = Label(Individual_Frame,text="Vinesh",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Vinesh_i.place(x=0,y=75)
        
        self.txt_Vinesh_i = Entry(Individual_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Vinesh_i.place(x=100,y=75,width=250)
        
        self.vinbtn_i = Button(Individual_Frame,text='C',width=4,height=1,command=lambda: Student.add_vinesh(self))
        self.vinbtn_i.place(x=355,y=78)
        
        self.lbl_Viswa_i = Label(Individual_Frame,text="Viswa",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Viswa_i.place(x=0,y=125)
        
        self.txt_Viswa_i = Entry(Individual_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Viswa_i.place(x=100,y=125,width=250)
        
        self.visbtn_i = Button(Individual_Frame,text='C',width=4,height=1,command=lambda: Student.add_viswa(self))
        self.visbtn_i.place(x=355,y=128)
        
        self.lbl_Srujan_i = Label(Individual_Frame,text="Srujan",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Srujan_i.place(x=0,y=175)
        
        self.txt_Srujan_i = Entry(Individual_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Srujan_i.place(x=100,y=175,width=250)
        
        self.srubtn_i = Button(Individual_Frame,text='C',width=4,height=1,command=lambda: Student.add_srujan(self))
        self.srubtn_i.place(x=355,y=178)


    #=======Clothes Share Frame=========    
        self.Clothes_Frame = Frame(self.root,bg="crimson")
        self.Clothes_Frame.place(x=450,y=350,width=410,height=280)
#        
 
        c_title = Label(self.Clothes_Frame,text="Clothes Share",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        c_title.grid(row=0,columnspan=2,pady=20,padx=100)

        self.lbl_Vinesh_c = Label(self.Clothes_Frame,text="Vinesh",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Vinesh_c.place(x=0,y=75)
        
        self.txt_Vinesh_c = Entry(self.Clothes_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Vinesh_c.place(x=100,y=75,width=250)
        
        self.vinbtn_c = Button(self.Clothes_Frame,text='C',width=4,height=1,command=lambda: Student.clothes_vinesh(self))
        self.vinbtn_c.place(x=355,y=78)
        
        self.lbl_Viswa_c = Label(self.Clothes_Frame,text="Viswa",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Viswa_c.place(x=0,y=125)
        
        self.txt_Viswa_c = Entry(self.Clothes_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Viswa_c.place(x=100,y=125,width=250)
        
        self.visbtn_c = Button(self.Clothes_Frame,text='C',width=4,height=1,command=lambda: Student.clothes_viswa(self))
        self.visbtn_c.place(x=355,y=128)
        
        self.lbl_Srujan_c = Label(self.Clothes_Frame,text="Srujan",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Srujan_c.place(x=0,y=175)
        
        self.txt_Srujan_c = Entry(self.Clothes_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Srujan_c.place(x=100,y=175,width=250)
        
        self.srubtn_c = Button(self.Clothes_Frame,text='C',width=4,height=1,command=lambda: Student.clothes_srujan(self))
        self.srubtn_c.place(x=355,y=178)
        
    
    #=========Calculate Summary================
    
#        self.srubtn_s = Button(root,text='Summary Share',width=4,height=1,command=lambda: Student.summary_frame(self))
#        self.srubtn_s.place(x=880,y=100,width=200)    
        
        self.style = Style()
        self.style.configure('TButton',font=('calibri',20,'bold'),borderwidth=4)
#        self.style.map('TButton', foreground = [('active', '! disabled', 'green')], background = [('active', 'black')])
        
        
        
        self.srubtn_s = Button(root,text='Summary Share',command=lambda: Student.summary_frame(self))
        self.srubtn_s.place(x=880,y=100,width=200)    
       
    #=======Summary Share Frame=========    
    def summary_frame(self):

        Summary_Frame = Frame(self.root,bg="crimson")
        Summary_Frame.place(x=880,y=150,width=350,height=300)
#        
 
        s_title = Label(Summary_Frame,text="Summary Share",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        s_title.grid(row=0,columnspan=2,pady=20,padx=80)

        self.lbl_Vinesh_s = Label(Summary_Frame,text="Vinesh",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Vinesh_s.place(x=0,y=75)
        
        self.txt_Vinesh_s = Entry(Summary_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Vinesh_sum = self.common_share + (((self.price_vinesh + self.price_viswa + self.price_srujan)/3)-self.price_vinesh)+ self.price_vinesh_c
        self.txt_Vinesh_sum=ceil(self.txt_Vinesh_sum/10.0) * 10
        self.txt_Vinesh_s.delete(0,"end")
        self.txt_Vinesh_s.insert(0,self.txt_Vinesh_sum)
        self.txt_Vinesh_s.place(x=100,y=75,width=150)
        smscon = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
        cursor = smscon.cursor()
        cursor.execute("update room_management set summary_share = %s where name='vinesh'"%(self.txt_Vinesh_sum))
        cursor.execute("COMMIT")
        smscon.close()
        
        self.lbl_Viswa_s = Label(Summary_Frame,text="Viswa",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Viswa_s.place(x=0,y=125)
        
        self.txt_Viswa_s = Entry(Summary_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Viswa_sum = self.common_share + (((self.price_vinesh + self.price_viswa + self.price_srujan)/3)-self.price_viswa)+ self.price_vinesh_c
        self.txt_Viswa_sum=ceil(self.txt_Viswa_sum/10.0) * 10
        self.txt_Viswa_s.delete(0,"end")
        self.txt_Viswa_s.insert(0,self.txt_Viswa_sum)
        self.txt_Viswa_s.place(x=100,y=125,width=150)
        smscon = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
        cursor = smscon.cursor()
        cursor.execute("update room_management set summary_share = %s where name='viswa'"%(self.txt_Viswa_sum))
        cursor.execute("COMMIT")
        smscon.close()
        
        self.lbl_Srujan_s = Label(Summary_Frame,text="Srujan",font=("times new roman",20,"bold"),bg='crimson',fg='white')
        self.lbl_Srujan_s.place(x=0,y=175)
        
        self.txt_Srujan_s = Entry(Summary_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Srujan_sum = self.common_share + (((self.price_vinesh + self.price_viswa + self.price_srujan)/3)-self.price_srujan)+ self.price_vinesh_c
        self.txt_Srujan_sum=ceil(self.txt_Srujan_sum/10.0) * 10
        self.txt_Srujan_s.delete(0,"end")
        self.txt_Srujan_s.insert(0,self.txt_Srujan_sum)
        self.txt_Srujan_s.place(x=100,y=175,width=150)
        smscon = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
        cursor = smscon.cursor()
        cursor.execute("update room_management set summary_share = %s where name='srujan'"%(self.txt_Srujan_sum))
        cursor.execute("COMMIT")
        smscon.close()
        
        self.send_sms = Button(Summary_Frame,text='Send SMS',command=lambda: Student.send_sms(self))
        self.send_sms.place(x=100,y=250)    
        
    def send_sms(self):
        print(self.txt_Viswa_sum)
        print(self.txt_Vinesh_sum)
        print(self.txt_Srujan_sum)
        import sendsms
        
    def add_vinesh(self):
        
        self.price_vinesh = self.txt_Vinesh_i.get()
        self.price_vinesh = sum(map(int,re.findall('\d+',self.price_vinesh)))
        self.txt_Vinesh_i.delete(0,self.price_vinesh)
        self.txt_Vinesh_i.insert(0,self.price_vinesh)

    def add_viswa(self):
        
        self.price_viswa = self.txt_Viswa_i.get()
        self.price_viswa = sum(map(int,re.findall('\d+',self.price_viswa)))
        self.txt_Viswa_i.delete(0,self.price_viswa)
        self.txt_Viswa_i.insert(0,self.price_viswa)

    def add_srujan(self):
        
        self.price_srujan = self.txt_Srujan_i.get()
        self.price_srujan = sum(map(int,re.findall('\d+',self.price_srujan)))
        self.txt_Srujan_i.delete(0,self.price_srujan)
        self.txt_Srujan_i.insert(0,self.price_srujan)
    
    def clothes_vinesh(self):
        
        self.clothes_vinesh = self.txt_Vinesh_c.get()
        self.clothes_vinesh = sum(map(int,re.findall('\d+',self.clothes_vinesh)))
        pairs_vinesh = self.clothes_vinesh/2
        self.price_vinesh_c = round(pairs_vinesh * 15)
        self.txt_Vinesh_c.delete(0,self.price_vinesh_c)
        self.txt_Vinesh_c.insert(0,self.price_vinesh_c)

    def clothes_viswa(self):
        
        self.clothes_viswa = self.txt_Viswa_c.get()
        self.clothes_viswa = sum(map(int,re.findall('\d+',self.clothes_viswa)))
        pairs_viswa = self.clothes_viswa/2
        self.price_viswa_c = round(pairs_viswa*15)
        self.txt_Viswa_c.delete(0,self.price_viswa_c)
        self.txt_Viswa_c.insert(0,self.price_viswa_c)

    def clothes_srujan(self):
        
        self.clothes_srujan = self.txt_Srujan_c.get()
        self.clothes_srujan = sum(map(int,re.findall('\d+',self.clothes_srujan)))
        pairs_srujan = self.clothes_srujan/2
        self.price_srujan_c = round(pairs_srujan*15)
        self.txt_Srujan_c.delete(0,self.price_srujan_c)
        self.txt_Srujan_c.insert(0,self.price_srujan_c)
        
    def common_share(self):
            
        self.common_share = round((self.rentamt+self.maintamt+self.cookamt+self.maidamt+self.internetamt+self.ebillamt)/3)
        self.txt_cs = tk.Entry(self.Common_Frame,font=("times new roman",15,"bold"),bd=0,text=self.common_share,bg='crimson',fg='white')
        self.txt_cs.place(x=10,y=500,width=370)
        self.txt_cs.delete(0,"end")
        self.txt_cs.insert(0,"Common Share: "+ str(self.common_share))
        
    def ExitApplication(self):
        Msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit application',icon='warning')
        if Msgbox == 'yes':
            self.root.destroy()
            
    def Home(self):
        self.root.destroy()
        self.root=Tk()
        Interframe(self.root)
        
    def Logout(self):
        Msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to Logout from application',icon='warning')
        if Msgbox == 'yes':
            self.root.destroy()
            self.root=Tk()
            Login(self.root)
        
class Zipper:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x500+0+0")
        
        self.zip_bg = ImageEnhance.Brightness(Image.open("zip.png"))
        self.zip_bg = self.zip_bg.enhance(1)
        
        self.zip_background_label = ImageTk.PhotoImage(self.zip_bg, master=self.root)
        self.zip_bgimg= tk.Label(self.root,image=self.zip_background_label)
        self.zip_bgimg.place(relwidth=1,relheight=1)
        self.title=tk.Label(self.root,text="Zipper",font=('calibri',25,'bold'),fg="black")  
        self.title.pack(side=tk.TOP)
        
        self.button = tk.Button(self.root, text='Select File', bg='khaki',fg='black',command=lambda: self.UploadAction())
        self.button.place(x=220,y=75)
        
        homebttn = tk.Button(self.root,text='Home',command=self.home)
        homebttn.place(relx=0.98,rely=0.022,relwidth=0.1,anchor='ne')
        
    def UploadAction(self):
        self.filename = filedialog.askopenfilenames()
        
        if self.filename != '':
            self.var = tk.StringVar()
            self.zip_name=tk.Label(self.root,text="Select zip filename",font=('calibri',14),fg="Black")
            self.zip_name.place(x=20,y=180)
            self.zip_dir=tk.Label(self.root,text="Folder to place file",font=('calibri',14),fg="Black")
            self.zip_dir.place(x=20,y=120)
            self.zip_dirt=tk.Entry(self.root,font=('calibri',14),fg="Black",textvariable=self.var)
            self.zip_dirt.place(x=200,y=120)
            self.zip_dirbttn = tk.Button(self.root, text='Dir',command=lambda: self.directory())
            self.zip_dirbttn.place(x=420,y=120)
            self.zip_text=tk.Entry(self.root,font=('calibri',14),fg="Black")
            self.zip_text.place(x=200,y=180)
            self.zip_text != self.zip_text.get()
            self.zip_button = tk.Button(self.root, text='Zip',command=lambda: self.zip())
            self.zip_button.place(x=420,y=180)
            
            
    def directory(self):
        self.dirname = filedialog.askdirectory()
        self.var.set(self.dirname)
        
    def zip(self):
        self.zip_text = self.zip_text.get()
        if self.zip_text != '':
            try:
                self.newZip = zipfile.ZipFile(self.dirname+'/'+self.zip_text+'.zip', 'w')
            except AttributeError or PermissionError:
                self.dirname = os.getcwd()
                self.newZip = zipfile.ZipFile(self.dirname+'/'+self.zip_text+'.zip', 'w')
        else:
            try:
                self.newZip = zipfile.ZipFile(self.dirname+'/'+datetime.now().strftime('%Y-%m-%d-%H%M%S')+'.zip', 'w')
            except AttributeError or PermissionError:
                self.dirname = os.getcwd()
                self.newZip = zipfile.ZipFile(self.dirname+'/'+datetime.now().strftime('%Y-%m-%d-%H%M%S')+'.zip', 'w')
            
        for f in self.filename:
            self.newZip.write(f,compress_type=zipfile.ZIP_DEFLATED)
        self.newZip.close()
        self.zip_msg=tk.Label(self.root,text="Files Zip Success, click here to view \nselect file to continue further",font=('calibri',14),fg="Green")
        self.zip_msg.place(x=120,y=240)
        self.zip_msg.bind("<Button-1>", lambda e: self.openlocation('"'+self.dirname+'/'+self.zip_text+'"'))        
    
    
    def openlocation(self,url):
        webbrowser.open_new(url)
        
    def home(self):
        self.root.destroy()
        self.root=tk.Tk()
        Interframe(self.root)
        
class Interframe:
    
    def __init__(self,root):
        
        self.root = root
        self.root.geometry("1350x750")
        
        self.img_zip = Image.open("zip.png")
        self.img_zip = self.img_zip.resize((100,100))
        self.img_zip = ImageTk.PhotoImage(self.img_zip, master=self.root )
        
        self.img_rms = Image.open("room.png")
        self.img_rms = self.img_rms.resize((100,100))
        self.img_rms = ImageTk.PhotoImage(self.img_rms, master=self.root )
        
        self.bg = ImageEnhance.Brightness(Image.open("landscape (1).png"))
        self.bg = self.bg.enhance(0.3)
        
        self.background_label = ImageTk.PhotoImage(self.bg, master=self.root )
        self.bgimg = tk.Label(self.root,image=self.background_label)
        self.bgimg.place(relwidth=1,relheight=1)
        
        self.label_zip = tk.Label(self.root, text='Zip convertor',bg=None,font=('calibri',13,'bold'))
        self.label_zip.place(x=100,y=220,width=104)
        
        self.label_rms = tk.Label(self.root, text='Room \nMgmt System',bg=None,font=('calibri',13,'bold'))
        self.label_rms.place(x=250,y=200,width=104,height=47)
        
        self.button_zip = tk.Button(self.root, image=self.img_zip,command=self.zipper)
        self.button_zip.place(x=100,y=250)
        
        self.button_rms = tk.Button(self.root, image=self.img_rms,command=self.RMS)
        self.button_rms.place(x=250,y=250)
        
        self.exitbttn_q = tk.Button(self.root,text='Logout',command=lambda: Student.Logout(self),bg='yellow')
        self.exitbttn_q.place(x=1250,y=15,width=50)
    
    def zipper(self):
        self.root.destroy()
        self.root=tk.Tk()
        Zipper(self.root)

    def RMS(self):
        self.root.destroy()
        self.root=tk.Tk()
        Student(self.root)
        
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        
        self.uname = StringVar()
        self.pwd = StringVar()
        self.time()
        
        self.bg = ImageEnhance.Brightness(Image.open("landscape (1).png"))
        self.bg = self.bg.enhance(0.3)
        
        self.background_label = ImageTk.PhotoImage(self.bg, master=self.root )
        self.bgimg = tk.Label(self.root,image=self.background_label)
        self.bgimg.place(relwidth=1,y=50,relheight=1)
        
        self.title=Label(self.root,text="Login System",font=('calibri',25,'bold'),fg="black")
        self.title.pack(side=TOP)
        
        
        self.Login_frame = Frame(self.root,bg="white",bd=5,relief=GROOVE)
        self.Login_frame.place(x=300,y=200,width=400,height=350)
        
        lbluser = Label(self.Login_frame,text="Username",font=('calibri',20,'bold'),bg="white")
        lbluser.place(x=30,y=80)
        
        entuser = Entry(self.Login_frame,textvariable=self.uname,font=('calibri',14,'bold'),bg="white")
        entuser.place(x=155,y=87)
        
        lblpwd = Label(self.Login_frame,text="Password",font=('calibri',20,'bold'),bg="white")
        lblpwd.place(x=30,y=140)
        
        entpwd = Entry(self.Login_frame,textvariable=self.pwd,font=('calibri',14,'bold'),bg="white", show='*')
        entpwd.place(x=155,y=146)
        
        loginbttn = Button(self.Login_frame,text="Login",font=('calibri',14,'bold'),bg="white",command=lambda: Login.login(self))
        loginbttn.place(x=100,y=210,width=75)
        
        signupbttn = Button(self.Login_frame,text="Signup",font=('calibri',14,'bold'),bg="white",command=lambda: Login.signup(self))
        signupbttn.place(x=200,y=210,width=75)

    def login(self):
        
        con = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
        cursor = con.cursor()
        cursor.execute("select username,password from customer")
        result = cursor.fetchall()
        login= [result[i][0] for i in range(len(result))]
        con.close()

        if self.uname.get() == "" or self.pwd.get()=="":
            messagebox.showerror("Error","All the fields are required!!")
            
        elif (self.uname.get() in login):
            con = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
            cursor = con.cursor()
            cursor.execute('SELECT password FROM customer WHERE username = %(username)s', { 'username' : self.uname.get()})
            result = cursor.fetchone()
            if self.pwd.get() == result[0]:
                con.close()  
                a = messagebox.showinfo("Success",f"welcome {self.uname.get()}")
                if a=='ok':                
                    self.root.destroy()                
                    self.root=tk.Tk()
                    Interframe(self.root)
            else:
                flashlbl= tk.Label(self.Login_frame,text="Invalid Username or Password",font=('calibri',15,'bold'),bg="white",fg="red")
                flashlbl.place(x=75,y=290)
                
        else:
        
            flashlbl= tk.Label(self.Login_frame,text="Invalid Username or Password",font=('calibri',15,'bold'),bg="white",fg="red")
            flashlbl.place(x=75,y=290)
            
    def signup(self):
        
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.cnfpassword = tk.StringVar()
        self.email = tk.StringVar()
        self.mobile = tk.StringVar()
        self.dob = tk.StringVar()
        
        self.signup_frame = tk.Frame(self.root,bg="white",bd=5,relief=GROOVE)
        self.signup_frame.place(x=750,y=100,width=500,height=530)
        
        lblfirst = tk.Label(self.signup_frame,text="Firstname",font=('calibri',15,'bold'),bg="white")
        lblfirst.place(x=30,y=40)
        
        lbllast = tk.Label(self.signup_frame,text="Lastname",font=('calibri',15,'bold'),bg="white")
        lbllast.place(x=30,y=90)
        
        lbluser = tk.Label(self.signup_frame,text="Username",font=('calibri',15,'bold'),bg="white")
        lbluser.place(x=30,y=140)
        
        lblpwd = tk.Label(self.signup_frame,text="Password",font=('calibri',15,'bold'),bg="white")
        lblpwd.place(x=30,y=190)
        
        lblcnfpwd = tk.Label(self.signup_frame,text="Confirm Password",font=('calibri',15,'bold'),bg="white")
        lblcnfpwd.place(x=30,y=240)
        
        lblemail = tk.Label(self.signup_frame,text="Email",font=('calibri',15,'bold'),bg="white")
        lblemail.place(x=30,y=290)
        
        lblmobile = tk.Label(self.signup_frame,text="mobile",font=('calibri',15,'bold'),bg="white")
        lblmobile.place(x=30,y=340)
        
        lbldob = tk.Label(self.signup_frame,text="Date of Birth",font=('calibri',15,'bold'),bg="white")
        lbldob.place(x=30,y=390)
        
        self.entfirst = tk.Entry(self.signup_frame,textvariable=self.firstname,font=('calibri',14,'bold'),bg="white")
        self.entfirst.place(x=200,y=47)
        
        self.entlast = tk.Entry(self.signup_frame,textvariable=self.lastname,font=('calibri',14,'bold'),bg="white")
        self.entlast.place(x=200,y=95)
        
        self.entuser = tk.Entry(self.signup_frame,textvariable=self.username,font=('calibri',14,'bold'),bg="white")
        self.entuser.place(x=200,y=145)
        
        self.entpwd = tk.Entry(self.signup_frame,textvariable=self.password,font=('calibri',14,'bold'),bg="white", show='*')
        self.entpwd.place(x=200,y=195)
        
        self.entcnfpwd = tk.Entry(self.signup_frame,textvariable=self.cnfpassword,font=('calibri',14,'bold'),bg="white", show='*')
        self.entcnfpwd.place(x=200,y=245)
        
        self.entemail = tk.Entry(self.signup_frame,textvariable=self.email,font=('calibri',14,'bold'),bg="white")
        self.entemail.place(x=200,y=295)
        
        self.entmobile = tk.Entry(self.signup_frame,textvariable=self.mobile,font=('calibri',14,'bold'),bg="white")
        self.entmobile.place(x=200,y=345)
         
        self.createbttn = Button(self.signup_frame,text="Create a new account",font=('calibri',14,'bold'),command=lambda: self.signupupdatedb())
        self.createbttn.place(x=170,y=450,width=185)
        
        closebttn = Button(self.signup_frame,text="X",font=('calibri',14,'bold'),command=lambda: self.close())
        closebttn.place(x=440,y=10,height=35,width=30)
            
        self.cal = DateEntry(self.signup_frame, width=30, height=10,year=1900,textvariable=self.dob, month=1, day=1, background='darkblue', foreground='white')
        self.cal.place(x=200,y=395)
        
        
    def close(self):
        self.signup_frame.destroy()
        
    def signupupdatedb(self):
        
        self.first = self.entfirst.get()
        self.last = self.entlast.get()
        self.user = self.entuser.get()
        self.pwd = self.entpwd.get()
        self.cnfpwd = self.entcnfpwd.get()
        self.email = self.entemail.get()
        self.mbl = self.entmobile.get()
        self.calc = self.cal.get()
        
        print(self.first)
        print(self.last)
        print("user",self.user)
        
        if self.user == None:
            print("yea")
            
        email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
        if (self.pwd != self.cnfpwd):
            messagebox.showerror("Error","Passwords should match")
        
        #=================Password validation to be added later========================#
        #=================Birthday remainders to be added later========================#
        
        
        if (re.search(email_regex,self.email)):
            pass
        else:
            messagebox.showerror("Error","Enter a valid email address")
        
        con = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
        cursor = con.cursor()
        cursor.execute('SELECT username FROM customer WHERE username = %(username)s', { 'username' : self.user})
        unameresult=cursor.fetchone()

        if unameresult != None:
            messagebox.showerror("Error","Please enter different userid as the userid with same name alreadt exists")
        con.close()   
        
        if (self.first != "" or self.last != "" or self.user != "" or self.pwd != "" or self.email != "" or self.mbl != "" or self.calc!= ""):
            
            con = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
            cursor = con.cursor()
            cursor.execute("insert into customer values('"+self.first+"','"+self.last+"','"+self.email+"','"+self.calc+"','"+self.mbl+"','"+self.pwd+"','"+self.user+"')")
            cursor.execute("commit");
            con.close()
            self.createbttn.destroy()
            flashlbl= tk.Label(self.signup_frame,text="User Created Successfully",font=('calibri',15,'bold'),bg="white",fg="green")
            flashlbl.place(x=150,y=450,width=220)
            
        else:
            messagebox.showerror("Error","Please take care of blank fields")
            
            
    def time(self):
        
        self.now = tk.StringVar()
        self.time = Label(self.root,font=('Helvetica', 20))
        self.time.place(x=1440,rely=0.005,relwidth=0.25,anchor='ne')
        
        self.time["textvariable"] = self.now
        
        self.onUpdate()
        
    def current_iso8601(self):
        return time.strftime("%H:%M:%S", time.localtime())
    
    def onUpdate(self):
        self.now.set(self.current_iso8601())
        self.time.after(1000, self.onUpdate)
        

root = tk.Tk()
ob = Login(root)
root.mainloop()
