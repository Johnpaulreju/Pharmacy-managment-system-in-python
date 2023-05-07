from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import ttk, messagebox
import sqlite3


class resetpage:
    def __init__(self, window):
        self.window = window
        width_val=self.window.winfo_screenwidth()
        height_val=self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (width_val,height_val))
        # self.window.geometry("1550x800+0+0")
        self.window.resizable(True, True)
        self.window.iconbitmap(r"F:\pMS\Pharmacy_management-system-master\image\lo.ico")
        self.window.state('zoomed')
        self.window.title('Reset Password Page')
        
        self.username_entry= StringVar()
        self.secretQA_entry= StringVar()
        self.password_entry= StringVar()
        self.confirmpassword_entry= StringVar()
        
        

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
        self.txt = "RESET PASSWORD"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Algerian', 30), bg="#040405",
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
        
        self.frame1_line = Canvas(self.lgn_frame, width=410, height=3.0, bg="#bdb9b1", highlightthickness=1)
        self.frame1_line.place(x=500, y=20)
        self.frame2_line = Canvas(self.lgn_frame, width=3.0, height=555, highlightthickness=1 )
        self.frame2_line.place(x=500,y=20)
        self.frame3_line = Canvas(self.lgn_frame, width=3.0, height=557, highlightthickness=1)
        self.frame3_line.place(x=910, y=20)
        self.frame4_line = Canvas(self.lgn_frame, width=412, height=3.0, bg="#bdb9b1", highlightthickness=1)
        self.frame4_line.place(x=500, y=575)
    
        
        # ========================================================================
        # ============================username====================================
        # ========================================================================
        
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=523, y=33)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=550, y=65, width=330)

        self.username_line = Canvas(self.lgn_frame, width=350, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=523, y=89)
        
        # ===== Username icon =========
        
        self.username_icon = Image.open("F:\pMS\Pharmacy_management-system-master\image\\username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=523, y=62)
        
        
        # ========================================================================
        # ============================Secret Question====================================
        # ========================================================================
        self.secretq_label = Label(self.lgn_frame, text="Security Question", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.secretq_label.place(x=523, y=110)
        
        self.secretQ_combo = ttk.Combobox(self.lgn_frame, width=22, font=("times new roman", 12, "bold"), state="readonly")
        self.secretQ_combo["values"] = ('Select',"What is your mother's maiden name?","What was the name of your first pet?","What was the name of your high school?","What is the city where you grew up?","What was your childhood nickname?","What was the make and model of your first car?")
        self.secretQ_combo.grid(row=0, column=1)
        self.secretQ_combo.current(0)
        self.secretQ_combo.place(x=523, y=140, width=360, height=33)
        
        # ========================================================================
        # ============================Secret Q/A====================================
        # ========================================================================
        
        self.secretQA_label = Label(self.lgn_frame, text="Secret Q. Answer", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.secretQA_label.place(x=523, y=185)

        self.secretQA_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.secretQA_entry.place(x=523, y=212, width=350)

        self.secretQA_line = Canvas(self.lgn_frame, width=350, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.secretQA_line.place(x=523, y=235)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=523, y=250)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=550, y=275 , width=285)

        self.password_line = Canvas(self.lgn_frame, width=350, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=523, y=305)
        # ======== Password icon ================
        self.password_icon = Image.open("F:\pMS\Pharmacy_management-system-master\image\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=523, y=275)
                # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file="F:\pMS\Pharmacy_management-system-master\image\\show.png")

        self.hide_image = ImageTk.PhotoImage \
            (file="F:\pMS\Pharmacy_management-system-master\image\\hide.png")

        self.show_button = Button(self.lgn_frame, image=self.show_image ,command=self.show , relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=850, y=275)
        
        
        # ========================================================================
        # ============================confirm password=============================
        # ========================================================================
        self.confirmpassword_label = Label(self.lgn_frame, text="Confirm Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.confirmpassword_label.place(x=523, y=320)

        self.confirmpassword_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.confirmpassword_entry.place(x=550, y=346, width=285)

        self.confirmpassword_line = Canvas(self.lgn_frame, width=350, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.confirmpassword_line.place(x=523, y=375)
        # ======== Password icon ================
        self.confirmpassword_icon = Image.open("F:\pMS\Pharmacy_management-system-master\image\\password_icon.png")
        photo = ImageTk.PhotoImage(self.confirmpassword_icon)
        self.confirmpassword_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.confirmpassword_icon_label.image = photo
        self.confirmpassword_icon_label.place(x=523, y=344)
                # ========= show/hide password ==================================================================
        self.confirmshow_image = ImageTk.PhotoImage \
            (file="F:\pMS\Pharmacy_management-system-master\image\\show.png")

        self.confirmhide_image = ImageTk.PhotoImage \
            (file="F:\pMS\Pharmacy_management-system-master\image\\hide.png")

        self.show_button = Button(self.lgn_frame, image=self.confirmshow_image,command=self.confirmshow , relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=850, y=348)

        # ========================================================================
        # ============================Register button================================
        # ========================================================================
        self.lgn_button = Image.open("F:\pMS\Pharmacy_management-system-master\image\\btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=460)
        self.login = Button(self.lgn_button_label, text='RESET PASSWORD', command=self.resetpass,font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        
        
        self.passwordvalidation_label = Label(self.lgn_frame, bg="#040405", fg="green",
                                    font=("yu gothic ui", 13, "bold"))
        self.passwordvalidation_label.place(x=680, y=385)
        

    def confirmshow(self):
        self.hide_button = Button(self.lgn_frame, image=self.confirmhide_image, relief=FLAT,command=self.confirmhide,activebackground="white",borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=850, y=348)
        self.confirmpassword_entry.config(show='')
    def confirmhide(self):
        self.show_button = Button(self.lgn_frame, image=self.confirmshow_image, command=self.confirmshow, relief=FLAT, activebackground="white",borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=850, y=348)
        self.confirmpassword_entry.config(show='*')
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, relief=FLAT,
                                  activebackground="white",command=self.hide,
                                  borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=850, y=275)
        self.password_entry.config(show='')
    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=850, y=275)
        self.password_entry.config(show='*')
        
    def resetpass(self):
        conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        if self.password_entry.get() == self.confirmpassword_entry.get() :
            self.passwordvalidation_label.config(text = "Password Matched")
            self.secretA = StringVar()
            self.secretQ = StringVar()
            new_cursor.execute("SELECT * FROM login where Username = ?",(self.username_entry.get(),))
            row = new_cursor.fetchall()
            list1=[rowq for rows in row for rowq in rows]
            self.secretQ = list1[3]
            self.secretA = list1[4]
            if self.secretQ ==self.secretQ_combo.get() and self.secretA== self.secretQA_entry.get():
                new_cursor.execute("UPDATE login SET Password = ? where Username = ?",(self.password_entry.get(),self.username_entry.get(),))
                messagebox.showinfo("Success","Successfully Password reset!!")
                conn.commit()
                window.quit
            else:
                messagebox.showinfo("Failure","Secret Question and Answer is Wrong!!")
                self.password_entry.set(" ")
                self.confirmpassword_entry.set(" ")
                self.secretQA_entry.set(" ")
                conn.commit()
        else:
            self.passwordvalidation_label.config(text = "Password is Not Matching ")
 
if __name__ == '__main__':
    window = Tk()
    resetpage(window)
    window.mainloop()