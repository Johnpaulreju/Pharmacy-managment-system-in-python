from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import ttk, messagebox
import sqlite3


class RegisterPage:
    def __init__(self, window):
        self.window = window
        width_val=self.window.winfo_screenwidth()
        height_val=self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (width_val,height_val))
        # self.window.geometry("1550x800+0+0")
        self.window.resizable(True, True)
        self.window.iconbitmap(r"F:\pMS\Pharmacy_management-system-master\image\lo.ico")
        self.window.state('zoomed')
        self.window.title('Login Page')
        
        self.desg_variable= IntVar()
        self.name_entry = StringVar()
        self.username_entry = StringVar()
        self.secretans_entry = StringVar()
        self.password_entry = StringVar()
        workID = 2
       

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        
        self.bg_frame = Image.open("F:\pMS\Pharmacy_management-system-master\image\\background12.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        # ====== Login Frame =========================
        
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=290, y=100)

        # ========================================================================
        # ========================================================================
        # ========================================================================
        self.txt = "SIGN UP"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Algerian', 60), bg="#040405",
                             fg='light blue',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=370, height=70)

        # ========================================================================
        # ============ Left Side Image ===========================================
        # ========================================================================
        self.side_image = Image.open("F:\pMS\Pharmacy_management-system-master\image\\vector.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============================Frame====================================
        # ========================================================================        
        
        self.frame1_line = Canvas(self.lgn_frame, width=342, height=3.0, bg="#bdb9b1", highlightthickness=1)
        self.frame1_line.place(x=530, y=20)
        self.frame2_line = Canvas(self.lgn_frame, width=3.0, height=555, highlightthickness=1 )
        self.frame2_line.place(x=530,y=20)
        self.frame3_line = Canvas(self.lgn_frame, width=3.0, height=557, highlightthickness=1)
        self.frame3_line.place(x=870, y=20)
        self.frame4_line = Canvas(self.lgn_frame, width=342, height=3.0, bg="#bdb9b1", highlightthickness=1)
        self.frame4_line.place(x=530, y=575)

        # ========================================================================
        # ============================name====================================
        # ========================================================================
        
        self.name_label = Label(self.lgn_frame, text="Name", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.name_label.place(x=550, y=33)

        self.name_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.name_entry.place(x=580, y=65, width=270)

        self.name_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.name_line.place(x=550, y=89)
        
        # ===== Username icon =========
        
        self.name_icon = Image.open("F:\pMS\Pharmacy_management-system-master\image\\username_icon.png")
        photo = ImageTk.PhotoImage(self.name_icon)
        self.name_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.name_icon_label.image = photo
        self.name_icon_label.place(x=550, y=62)        
        
        # ========================================================================
        # ============================username====================================
        # ========================================================================
        
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=103)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=135, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=159)
        
        # ===== Username icon =========
        
        self.username_icon = Image.open("F:\pMS\Pharmacy_management-system-master\image\\username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=132)
        
        
        # ========================================================================
        # ============================Secret Question====================================
        # ========================================================================
        self.secretq_label = Label(self.lgn_frame, text="Security Question", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.secretq_label.place(x=550, y=170)
        
        self.secret_combo = ttk.Combobox(self.lgn_frame, width=22, font=("times new roman", 12, "bold"), state="readonly")
        self.secret_combo["values"] = ('Select',"What is your mother's maiden name?","What was the name of your first pet?","What was the name of your high school?","What is the city where you grew up?","What was your childhood nickname?","What was the make and model of your first car?")
        self.secret_combo.grid(row=0, column=1)
        self.secret_combo.current(0)
        self.secret_combo.place(x=550, y=200, width=300, height=30)
        
        # ========================================================================
        # ============================Secret Q/A====================================
        # ========================================================================
        
        self.secretans_label = Label(self.lgn_frame, text="Secret Q. Answer", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.secretans_label.place(x=550, y=238)

        self.secretans_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.secretans_entry.place(x=550, y=265, width=300)
        self.secretans_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.secretans_line.place(x=550, y=290)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=300)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=326, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=355)
        # ======== Password icon ================
        self.password_icon = Image.open("F:\pMS\Pharmacy_management-system-master\image\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=328)
                # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file="F:\pMS\Pharmacy_management-system-master\image\\show.png")

        self.hide_image = ImageTk.PhotoImage \
            (file="F:\pMS\Pharmacy_management-system-master\image\\hide.png")

        self.show_button = Button(self.lgn_frame, image=self.show_image,command=self.show , relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=820, y=328)
        

        # ========================================================================
        # ============================branch====================================
        # ========================================================================
        self.branch_label = Label(self.lgn_frame, text="Branch", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.branch_label.place(x=550, y=365)
        
        self.branch_combo = ttk.Combobox(self.lgn_frame, width=22, font=("times new roman", 12, "bold"), state="readonly")
        self.branch_combo["values"] = ('Select',"Kothanur","whitefeild","K Narayanpura","New Aiport","Majestic","Kengeri")
        self.branch_combo.grid(row=0, column=1)
        self.branch_combo.current(0)
        self.branch_combo.place(x=550, y=395, width=300, height=30)
 
        # ========================================================================
        # ============================branch====================================
        # ========================================================================
               
        self.designation_combo = ttk.Combobox(self.lgn_frame, width=22, font=("times new roman", 12, "bold"), state="readonly")
        self.designation_combo["values"] = ('Select Your Designation',"Admin","Employee")
        self.designation_combo.grid(row=0, column=1)
        self.designation_combo.current(0)
        self.designation_combo.place(x=600,y=430)

        # ========================================================================
        # ============================Register button================================
        # ========================================================================
        self.lgn_button = Image.open("F:\pMS\Pharmacy_management-system-master\image\\btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=460)
        self.login = Button(self.lgn_button_label, text='REGISTER',command=self.register, font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open("F:\pMS\Pharmacy_management-system-master\image\\btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=510)
        self.login = Button(self.lgn_button_label, text='CLEAR', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, relief=FLAT,
                                  activebackground="white"
                                  ,command=self.hide, borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=820, y=328)
        self.password_entry.config(show='')
    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=820, y=328)
        self.password_entry.config(show='*')
        
    def register(self):
        conn = sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM login where Username = ?",(self.username_entry.get(),))
        row = my_cursor.fetchall()
        workID=+1
        list1=[rowq for rows in row for rowq in rows]
        print(list1)
        print(len(list1))
        if self.name_entry.get() == "" and self.username_entry.get() == "" and self.secret_combo.get() == "Select " and self.password_entry.get() == "" and self.branch_combo.get() =="Select" and self.designation_combo.get() == "Select Your Designation" :
            messagebox.showerror("Error", "All fields are required")

        elif len(list1) != 0  :
            messagebox.showerror("Error", "Username already exist")
            
        else:
            
            my_cursor.execute("Insert into Login(ID,Name,Username,SecretQ,SecretA,Password,Branch,designation) values("+workID+",?,?,?,?,?,?,?)", (
                self.name_entry.get(),
                self.username_entry.get(),
                self.secret_combo.get(),
                self.secretans_entry.get(),
                self.password_entry.get(),
                self.branch_combo.get(),
                self.designation_combo.get(),))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "USER REGISTERED")

if __name__ == '__main__':
    window = Tk()
    RegisterPage(window)
    window.mainloop()