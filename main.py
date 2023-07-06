from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class qr_generator():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1000x800+200+50')
        self.root.title("Student QR Code Generator")
        self.root.resizable(False,False)

        header_lbl=Label(self.root,text="QR Code Generator",font=("times new roman",40,'bold'),bg='#3B2F2F',fg='white').place(x=0,y=0,relwidth=1,height=100)

        #-------student details-------
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_college=StringVar()
        self.var_branch=StringVar()
        self.var_sec=StringVar()
        self.var_add=StringVar()
        self.var_aadhar=StringVar()

        #--------creating the first frame-------
        stu_frame=Frame(self.root,bd=3,relief=GROOVE,bg="#3D3635")
        stu_frame.place(x=40,y=120,height=650,width=480)
        block_head=Label(stu_frame,text="Enter the details",font=("times new roman",25,'bold'),bg='#3B2F2F',fg='white').place(x=0,y=0,relwidth=1,height=50)

        #--------creating the fields--------
        stu_id=Label(stu_frame,text="College Id:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=60,height=30)
        stu_name=Label(stu_frame,text="Name:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=100,height=30)
        stu_roll=Label(stu_frame,text="Roll no.:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=140,height=30)
        stu_college=Label(stu_frame,text="College Name:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=180,height=30)
        stu_branch=Label(stu_frame,text="Branch:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=220,height=30)
        stu_sec=Label(stu_frame,text="Section:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=260,height=30)
        stu_add=Label(stu_frame,text="Address:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=300,height=30)
        stu_aadhar=Label(stu_frame,text="Aadhar Card:",font=("times new roman",15),bg='#3B2F2F',fg='white').place(x=5,y=360,height=30)

        #---------creating the entry-fields---------
        txt_id=Entry(stu_frame,textvariable=self.var_id,font=('times new roman',15),bg='#CECECE').place(x=200,y=60,height=30,width=200)
        txt_name=Entry(stu_frame,textvariable=self.var_name,font=('times new roman',15),bg='#CECECE').place(x=200,y=100,height=30,width=200)
        txt_roll=Entry(stu_frame,textvariable=self.var_roll,font=('times new roman',15),bg='#CECECE').place(x=200,y=140,height=30,width=200)
        txt_college=Entry(stu_frame,textvariable=self.var_college,font=('times new roman',15),bg='#CECECE').place(x=200,y=180,height=30,width=200)
        txt_branch=Entry(stu_frame,textvariable=self.var_branch,font=('times new roman',15),bg='#CECECE').place(x=200,y=220,height=30,width=200)
        txt_sec=Entry(stu_frame,textvariable=self.var_sec,font=('times new roman',15),bg='#CECECE').place(x=200,y=260,height=30,width=200)
        txt_add=Entry(stu_frame,textvariable=self.var_add,font=('times new roman',15),bg='#CECECE').place(x=200,y=300,height=50,width=200)
        txt_aadhar=Entry(stu_frame,textvariable=self.var_aadhar,font=('times new roman',15),bg='#CECECE').place(x=200,y=360,height=30,width=200)

        #-------------button------------
        btn_generate=Button(stu_frame,text="Generate",font=("times new roman",18,'bold'),bg='black',fg='white',command=self.generate).place(x=20,y=420,height=50,width=150)
        btn_clear=Button(stu_frame,text="Clear",font=("times new roman",18,'bold'),bg='black',fg='white',command=self.clear).place(x=220,y=420,height=50,width=150)

        #-------------message------------
        self.msg=""
        self.msg_lbl=Label(stu_frame,text=self.msg,font=('times new roman',30,'bold'),bg='#3B2F2F',fg="green")
        self.msg_lbl.place(x=5,y=500)

        #-------------Qr frame------------
        qr_frame=Frame(self.root,bd=3,relief=GROOVE,bg="#3D3635")
        qr_frame.place(x=540,y=120,height=650,width=420)
        qr_head=Label(qr_frame,text="Qr Code",font=("times new roman",25,'bold'),bg='#3B2F2F',fg='white').place(x=0,y=0,relwidth=1,height=50)
        #---------qr image---------
        self.qr_code=Label(qr_frame,text="No Qr Available",font=("times new roman",25,'bold'),bg='black',fg='white')
        self.qr_code.place(x=30,y=100,width=350,height=500)


        #-------------function call---------
    def generate(self):
        if (self.var_id.get()=='' or self.var_name.get()=='' or self.var_roll.get()=='' or self.var_college.get()=='' or self.var_branch.get()=='' or self.var_sec.get()=='' or self.var_add.get()=='' or self.var_aadhar.get()==''):
            self.msg="All Fields are required!!!!!"
            self.msg_lbl.config(text=self.msg,fg='red')
        else:
            qr_data=(f'Student ID:{self.var_id.get()}\nName:{self.var_name.get()}\nRoll no. :{self.var_roll.get()}\nCollege:{self.var_college.get()}\nBranch:{self.var_branch.get()}\nSection:{self.var_sec.get()}\nAddress:{self.var_add.get()}\nAadhar Card No:{self.var_aadhar.get()}')
            qr_code=qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=5
            )
            qr_code=qrcode.make(qr_data)

            #resizing the image
            qr_code=resizeimage.resize_cover(qr_code,[300,300])
            #saving th image
            qr_code.save("student/id-"+str(self.var_id.get())+'.png')
            self.img=ImageTk.PhotoImage(file="student/id-"+str(self.var_id.get())+'.png')
            self.qr_code.config(image=self.img)


            self.msg="Qr Code generated!!!!"
            self.msg_lbl.config(text=self.msg,fg='green')


    def clear(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_roll.set('')
        self.var_college.set('')
        self.var_branch.set('')
        self.var_sec.set('')
        self.var_add.set('')
        self.var_aadhar.set('')
        self.msg='All cleared'
        self.msg_lbl.config(text=self.msg,fg="black")
        self.qr_code.config(image='')


root=Tk()
obj=qr_generator(root)
root.mainloop()