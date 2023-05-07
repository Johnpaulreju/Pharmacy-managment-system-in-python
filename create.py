from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import sqlite3

with sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db') as db:
    cursor = db.cursor()
cursor.execute("SELECT * From login")
db.commit()
db.close()



class create:
    def __init__(self, root):
        self.root=root
        self.idfield = StringVar()
        self.namefield= StringVar()
        self.desgfield = StringVar()
        self.usernamefield= StringVar()
        self.passwordfield = StringVar()
        self.root.title("Pharmacy Management System")
        self.root.geometry("520x550+0+0")
        self.root.resizable(False, False)
        self.root.iconbitmap(r"F:\pMS\Pharmacy_management-system-master\image\lo.ico")
        topframe = Frame(self.root, bg='grey', bd=5, relief=RIDGE, padx=0)
        topframe.place(x=0, y=0, width=700, height=700)
        self.bg = Image.open("F:\pMS\Pharmacy_management-system-master\image\p1.png")
        resized = self.bg.resize((700, 600),Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(resized)
        lbl_bg = Label(topframe, image=self.bg)
        lbl_bg.pack()
        self.logframe = Frame(topframe, bg='#7FFFD4', bd=5 ,relief=RIDGE)
        self.logframe.place(x=20, y=25, width=470, height=500)
        self.original = Image.open("F:\pMS\Pharmacy_management-system-master\image\sign.png")
        resized = self.original.resize((350, 90),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        lbl_bg = Label(self.logframe, image=self.image)
        lbl_bg.place(x=50, y=20, width=350, height=100)
        
        
        self.id=Label(self.logframe, text="ID -: ", padx=2, pady=4, font=(
            "Garamond", 18, "bold"), bg="#7FFFD4")
        self.id.place(x=65, y=135, width=100, height=40)
        self.idfield=Entry(self.logframe,textvariable='id',font=("Garamond", 15, "bold"),width=2)
        self.idfield.place(x=201, y=141, width=225, height=30)
        
        
        self.name=Label(self.logframe, text="Name -: ", padx=2, pady=4, font=(
            "Garamond", 18, "bold"), bg="#7FFFD4")
        self.name.place(x=15, y=185, width=162, height=40)
        self.namefield=Entry(self.logframe,textvariable='name',font=(
            "Garamond", 15, "bold"),width=2)
        self.namefield.place(x=201, y=189, width=225, height=30)
        
        
        self.username=Label(self.logframe, text="Username -: ", padx=2, pady=4, font=(
            "Garamond", 18, "bold"), bg="#7FFFD4")
        self.username.place(x=15, y=245, width=162, height=40)
        self.usernamefield=Entry(self.logframe,textvariable='user',font=(
            "Garamond", 15, "bold"),width=2)
        self.usernamefield.place(x=201, y=249, width=225, height=30)
        
        
        self.desg=Label(self.logframe, text="Designation -: ", padx=2, pady=4, font=(
            "Garamond", 18, "bold"), bg="#7FFFD4")
        self.desg.place(x=15, y=305, width=162, height=40)
        # self.desgfield=Entry(self.logframe,textvariable='designation',font=(
            # "Garamond", 15, "bold"),width=2)
        self.ref_combo = ttk.Combobox(self.logframe, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.ref_combo["values"] = ('Select',"Emp","Admin")
        self.ref_combo.grid(row=0, column=1)
        self.ref_combo.current(0)
        self.ref_combo.place(x=201, y=309, width=225, height=30)
        
        self.password=Label(self.logframe, text="Password -: ", padx=2, pady=4, font=(
            "Garamond", 18, "bold"), bg="#7FFFD4")
        self.password.place(x=15, y=365, width=162, height=40)
        self.passwordfield=Entry(self.logframe,textvariable='pass',show="*",font=(
            "Garamond", 15, "bold"),width=2)
        self.passwordfield.place(x=201, y=369, width=225, height=30)
        
        
        self.login=Button(self.logframe,text="Sign Up",cursor="hand2",command=lambda:signup() ,bd=5 ,bg="white", fg="black", font=("Garamond", 18,"bold"), highlightcolor="#7FFFD4", padx=5,pady=5, relief="groove")
        self.login.place(x=45, y=435, width=152, height=40)
        self.login=Button(self.logframe,text="Clear",cursor="hand2",bd=5,bg="white",fg="black",
                   command=lambda:my_reset() , font=("Garamond", 18,"bold"),padx=5,pady=5,highlightcolor="#7FFFD4",relief="groove")
        self.login.place(x=255, y=435, width=152, height=40)
   
   
   
        def my_reset():
            self.idfield.delete(0,"end")
            self.desgfield.delete(0,"end")
            self.namefield.delete(0,"end")
            self.usernamefield.delete(0,"end")
            self.passwordfield.delete(0,"end")
            

        
        def signup():
            
            with sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db') as db:
                cursor = db.cursor()
            find_user = ("SELECT * FROM login WHERE Username = ? ")
            cursor.execute(find_user,[(self.usernamefield.get())])
            results = cursor.fetchall()
            if results:
                messagebox.showerror("Opps!!","Username Taken! ")
            else:
                messagebox.showinfo("Success!!","Account has been created")
            insert= "INSERT INTO login(ID,Name,Username,desgination,Password) VALUES(?,?,?,?,?)"
            cursor.execute(insert,[(self.idfield.get()),(self.namefield.get()),(self.usernamefield.get()),(self.desgfield.get()),(self.passwordfield.get())])
            messagebox.showinfo("Successfull ! ! !","REGISTERED SUCCESSFULLY")
            db.commit()    
        

 


if __name__ == '__main__':

    root=Tk()
    obj=create(root)
    root.mainloop()
