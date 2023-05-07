from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import sqlite3
from tkcalendar import DateEntry
from  datetime import date
import datetime
from reportlab.pdfgen import canvas
from tkinter import filedialog
import os


class AdminPage:
    def __init__(self, root,username):
        self.root = root
        self.root.title("Pharmacy Management System")
        width_val=self.root.winfo_screenwidth()
        height_val=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_val,height_val))
        # self.root.geometry("1550x800+0+0")
        self.root.resizable(True, True)
        self.root.iconbitmap(r"F:\pMS\Pharmacy_management-system-master\image\lo.ico")
        img2 = Image.open(r"F:\pMS\Pharmacy_management-system-master\image\logo1.png")
        img2 = img2.resize((70, 45), Image.ANTIALIAS)
        self.file_name = ImageTk.PhotoImage(img2)

        ##### Requ
        
        
        ##### ADDMED VARIABLE ######
        self.ref_variable = StringVar()
        self.addmed_variable = StringVar()
        self.Issue_data = StringVar()
        self.Expiry_data = StringVar()
        self.sideeffect = StringVar()
        self.warning = StringVar()
        self.TabletPrice = StringVar()


        ########## MEDICINE DEPARTMENT VARIABLE #######
        self.patientid = IntVar()
        self.patientid.set("0")
        self.companyname_var = StringVar()
        self.Mobileno = StringVar()
        self.patientname = StringVar()
        self.hospital = StringVar()
        self.refno_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedt_var = StringVar()
        self.expdt_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        self.totalp = StringVar()
        self.discount=StringVar()
        self.tnp=StringVar()
        self.amtp=StringVar()
        self.balance=StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        va = StringVar()
        
        self.tol= StringVar()
        self.idno = StringVar()
        
        
        ######## menu bar ########
        self.menubar = Menu(self.root , background='#283e4a', foreground='black', activebackground='white', activeforeground='black')  
        self.reportmenu = Menu(self.menubar, tearoff=0, background='#283e4a', foreground='white')
        self.reportmenu.add_command(label="Mobile No. Wise")
        self.reportmenu.add_command(label="Date Wise Sales")
        self.reportmenu.add_command(label="Customer Wise")
        self.reportmenu.add_command(label="Product Wise")

        self.file = Menu(self.menubar, tearoff=1, background='#283e4a', foreground='white')  
        # self.file.add_command(label="Report") 
        self.file.add_cascade(label="Report",menu=self.reportmenu) 
        self.file.add_separator()  
        self.file.add_command(label="Exit", command=root.quit)  
        self.menubar.add_cascade(label="File", menu=self.file) 
        self.edit = Menu(self.menubar, tearoff=0, background='#283e4a', foreground='white')  
        self.edit.add_command(label="Undo")  
        self.edit.add_separator()     
        # self.edit.add_command(label="Cut")  
        # self.edit.add_command(label="Copy")  
        # self.edit.add_command(label="Paste")  
        # self.menubar.add_cascade(label="Edit", menu=self.edit)  

        self.help = Menu(self.menubar, tearoff=0, background='#283e4a', foreground='white')  
        self.help.add_command(label="About")  
        self.menubar.add_cascade(label="Help", menu=self.help)  
        self.root.config(menu=self.menubar)

        ######## title animation #########
        self.txt = "PHARMACY MANAGEMENT SYSTEM"
        self.count = 0
        self.text = " "
        self.color = ["red"]
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 30, "bold"), background="#283e4a", fg="blue", bd=9, relief=RIDGE)
        self.heading.pack(side=TOP, fill=X)
        self.slider()
        self.heading_color()

        ######### pharmacy logo label #######
        img1 = Image.open(r"F:\pMS\Pharmacy_management-system-master\image\logo1.png")
        img1 = img1.resize((70, 45), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1,
                    borderwidth=0, bg='grey')
        b1.place(x=15, y=8)
        self.avatar = Label(self.root,font=(
            "times new roman", 15, "bold"), bg='#7FFFD4', fg="blue", relief=RIDGE)
        self.avatar.place(x=1320,y=15,height=35,width=195)
        self.username = Label(self.root,image=self.photoimg1, bg='#7FFFD4', fg="blue", relief=RIDGE)
        self.username.place(x=1250,y=10,height=45,width=50)
        self.avatar.config(text = "Welcome "+username)

        ###### Top Frame #####
        
        self.bg_frame = Image.open(r"F:\pMS\Pharmacy_management-system-master\image\background1.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        
        topframe = Frame(self.root,bg="#283e4a", bd=10, relief=RIDGE, padx=20)
        topframe.place(x=0, y=62, width=1535, height=450)

        ########  down button frame #######
        down_buttonframe = Frame(
            self.root, bg='#283e4a', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=0, y=512, width=1535, height=60)

            ###### all buttons ######
        add_button = Button(down_buttonframe, text="Store Information", command=self.addmedicine, font=(
            "arial", 12, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.place(x=0,y=3)

        update_button = Button(down_buttonframe, command=self.update_new, text="Update", font=(
            "arial", 13, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        update_button.place(x=160,y=3)

        delete_button = Button(down_buttonframe, text="Delete", command = self.deleteinfo ,font=("arial", 13, "bold"), width=13,
                               fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        delete_button.place(x=320,y=3)

        reset_button = Button(down_buttonframe, text="Reset", command=self.clear_new, font=("arial", 13, "bold"), width=12,
                              fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        reset_button.place(x=470,y=3)

        exit_button = Button(down_buttonframe, command=self.root.quit, text="Exit", font=(
            "arial", 13, "bold"), width=10, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        exit_button.place(x=620,y=3)

        search_by = Label(down_buttonframe, text="Search By -: ", font=(
            "times new roman", 20, "bold"), fg="white", bg="#283e4a", bd=3, padx=3)
        search_by.place(x=735,y=0)

        self.search_combo = ttk.Combobox(down_buttonframe, width=14, font=(
            "arial", 13, "bold"), state="readonly", textvariable=self.search_by)
        self.search_combo["values"] = ("Select Options", "Mobile No.","Patient Name")
        self.search_combo.place(x=885,y=8)
        self.search_combo.current(0)

        entry_button = Entry(down_buttonframe, font=("arial", 15, "bold"), fg="black",
                             bg="grey", bd=3, width=15, relief=RIDGE, textvariable=self.search_txt)
        entry_button.place(x=1040,y=3)

        search_button = Button(down_buttonframe, text="Search", font=("arial", 13, "bold"), width=10, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.search_data)
        search_button.place(x=1220,y=3)

        show_button = Button(down_buttonframe, text="Show All", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=10, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.fetch_new)
        show_button.place(x=1370,y=3)

        ######## left small frame #######
        left_smallframe = LabelFrame(topframe, bg='grey', bd=10, relief=RIDGE,
                                     padx=20, text="Patient Information", font=("arial", 13, "bold"), fg="white")
        left_smallframe.place(x=0, y=3, width=820, height=415)
        
        ############Button inside the left label
        fetchdebutton = Button(left_smallframe, text="Fetch", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=12, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.fetd)
        # fetchbutton.place(x=5,y=400)
        fetchdebutton.place(x=20,y=344)
        
        ############Button inside the left label
        tpbutton = Button(left_smallframe, text="Total Price", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=12, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.bill)
        tpbutton.place(x=170,y=344)
        
############Button inside the left label
        tnpbutton = Button(left_smallframe, text="Total Net Price", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=12, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.disc)
        tnpbutton.place(x=320,y=344)
        
        ############Button inside the left label
        blncebutton = Button(left_smallframe, text="Balance", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=12, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.balan)
        blncebutton.place(x=470,y=344)
        
    ############Button inside the left label
        printbutton = Button(left_smallframe, text="Print Bill" , command = self.generate_receipt , font=("arial", 13, "bold"), fg="white", bg="black",
                             width=12, bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        printbutton.place(x=620,y=344)
        #### labeling & entry box #########
        # 2
        Mobile_label = Label(left_smallframe, text="Mobile No.  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Mobile_label.grid(row=0, column=0)
        self.Mobileno_entry = Entry(left_smallframe, textvariable=self.Mobileno, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Mobileno_entry.grid(row=0, column=1)
        
                # 2
        PatientName_label = Label(left_smallframe, text="Patient Name  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        PatientName_label.grid(row=1, column=0)
        self.PatientName_entry = Entry(left_smallframe, textvariable=self.patientname, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.PatientName_entry.grid(row=1, column=1)
        
         # 2
        company_label = Label(left_smallframe, text="Hospital Name  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        company_label.grid(row=2, column=0)
        self.company_entry = Entry(left_smallframe, textvariable=self.hospital, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.company_entry.grid(row=2, column=1)
        
        # 1
        ref_label = Label(left_smallframe, text="Reference No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        ref_label.grid(row=3, column=0, sticky=W)

        conn = sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("Select Ref_no from pharma")
        row_01 = [r for r, in my_cursor]

        self.ref_combo = ttk.Combobox(left_smallframe, values=row_01, textvariable=self.refno_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")

        self.ref_combo.current(0)

        self.ref_combo.grid(row=3, column=1)

        # 3
        type_label = Label(left_smallframe, text="Type Of Medicine :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        type_label.grid(row=4, column=0, sticky=W)

        self.type_combo = ttk.Combobox(left_smallframe, textvariable=self.typemed_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.type_combo["values"] = (
            " Select  ", "Tablet", "Capsule", "Injection", "Ayurvedic", "Drops", "Inhales")
        self.type_combo.grid(row=4, column=1)
        self.type_combo.current(0)

        # 4

        medname_label = Label(left_smallframe, text="Medicine Name :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        medname_label.grid(row=5, column=0, sticky=W)
        
        self.mednamed = Entry(left_smallframe, textvariable=self.medicine_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.mednamed.grid(row=5, column=1)
        # 5
    
        lot_label = Label(left_smallframe, text=" Lot No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        lot_label.grid(row=6, column=0)

        self.lot_entry = Entry(left_smallframe, textvariable=self.lotno_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.lot_entry.grid(row=6, column=1)

        # 6

        issue_label = Label(left_smallframe, text=" Issue Date :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        issue_label.grid(row=7, column=0)

        self.issue_entry = Entry(left_smallframe, textvariable=self.issuedt_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.issue_entry.grid(row=7, column=1)

        # 7

        exp_label = Label(left_smallframe, text=" Expiry Date :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        exp_label.grid(row=8, column=0)

        self.exp_entry = Entry(left_smallframe, textvariable=self.expdt_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.exp_entry.grid(row=8, column=1)

        # 8

        use_label = Label(left_smallframe, text=" Uses :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        use_label.grid(row=9, column=0)

        self.use_entry = Entry(left_smallframe, textvariable=self.uses_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.use_entry.grid(row=9, column=1)

        # 9

        sideeffect_label = Label(left_smallframe, text=" Side Effect :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        sideeffect_label.grid(row=0, column=2)

        self.sideeffect_entry = Entry(left_smallframe, textvariable=self.sideeffect_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.sideeffect_entry.grid(row=0, column=3)

        # 10

        warn_label = Label(left_smallframe, text=" Prec & warning:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        warn_label.grid(row=1, column=2)

        self.warn_entry = Entry(left_smallframe, textvariable=self.warning_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.warn_entry.grid(row=1, column=3)

        # 11

        dosage_label = Label(left_smallframe, text=" Dosage :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        dosage_label.grid(row=2, column=2)

        self.dosage_entry = Entry(left_smallframe, textvariable=self.dosage_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.dosage_entry.grid(row=2, column=3)

        # 12

        price_label = Label(left_smallframe, text=" Tablet Price :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        price_label.grid(row=3, column=2)

        self.price_entry = Entry(left_smallframe, textvariable=self.price_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.price_entry.grid(row=3, column=3)

        # 13

        qt_label = Label(left_smallframe, text=" Tablet Quantity :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        qt_label.grid(row=4, column=2)

        self.qt_entry = Entry(left_smallframe, textvariable=self.quantity_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.qt_entry.grid(row=4, column=3)

        # 14

        total_label = Label(left_smallframe, text=" Total Price :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        total_label.grid(row=5, column=2)

        self.total_entry = Entry(left_smallframe, textvariable=self.totalp, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.total_entry.grid(row=5, column=3)
        
            # 15

        dis_label = Label(left_smallframe, text=" Discount % :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        dis_label.grid(row=6, column=2)

        self.dis_entry = Entry(left_smallframe, textvariable=self.discount, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.dis_entry.grid(row=6, column=3)
        
        # 16

        tnp_label = Label(left_smallframe, text=" Total Net Price :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        tnp_label.grid(row=7, column=2)

        self.tnp_entry = Entry(left_smallframe, textvariable=self.tnp, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.tnp_entry.grid(row=7, column=3)
        
        # 17

        amtp_label = Label(left_smallframe, text=" Amount Paid :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        amtp_label.grid(row=8, column=2)

        self.amtp_entry = Entry(left_smallframe, textvariable=self.amtp, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.amtp_entry.grid(row=8, column=3)
        
                # 18

        blnce_label = Label(left_smallframe, text=" Balance :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        blnce_label.grid(row=9, column=2)

        self.blnce_entry = Entry(left_smallframe, textvariable=self.balance, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.blnce_entry.grid(row=9, column=3)
        
        ############ right frame #########
        right_frame = LabelFrame(topframe, bg='grey', bd=10, relief=RIDGE, padx=5,
                                 text="New Medicine Add department", font=("arial", 13, "bold"), fg="white")
        right_frame.place(x=846, y=5, width=630, height=415)

        # #### label & entry in right frame ####
        
        # 1
        no_label = Label(right_frame, text="Reference No:", font=(
            "times new roman", 11, "bold"), bg="grey")
        no_label.place(x=0, y=5)

        self.no_entry = Entry(right_frame, textvariable=self.ref_variable, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.no_entry.place(x=100, y=5)
        # 2
        med_label = Label(right_frame, text="Med. Name:", font=(
            "times new roman", 11, "bold"), bg="grey")
        med_label.place(x=0, y=40)

        self.med_entry = Entry(right_frame, textvariable=self.addmed_variable, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.med_entry.place(x=100, y=42,width=150)
        
        # 3
        issuelabel = Label(right_frame, text="Issue data:", font=(
            "times new roman", 11, "bold"), bg="grey")
        issuelabel.place(x=0, y=75)

        self.issue = DateEntry(right_frame, textvariable=self.Issue_data, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.issue.place(x=100, y=75)
        
        # 4
        Expiry = Label(right_frame, text="Expiry Date:", font=(
            "times new roman", 11, "bold"), bg="grey")
        Expiry.place(x=0, y=110)

        self.Expirydfield = Label(right_frame,text=" ", textvariable=self.Expiry_data,font=(
            "times new roman", 11, "bold"), bg="grey")
        self.Expirydfield.place(x=100, y=112)
        
                # 2
        med_side = Label(right_frame, text="Side effect:", font=(
            "times new roman", 11, "bold"), bg="grey")
        med_side.place(x=0, y=145)

        self.side_entry = Entry(right_frame, textvariable=self.sideeffect, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.side_entry.place(x=100, y=148,width=150)
        
                # 2
        warning_label = Label(right_frame, text="Warning:", font=(
            "times new roman", 11, "bold"), bg="grey")
        warning_label.place(x=0, y=180)

        self.warning_entry = Entry(right_frame, textvariable=self.warning, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.warning_entry.place(x=100, y=182,width=150)
        
                # 2
        Tbprice_label = Label(right_frame, text="Tablet Price:", font=(
            "times new roman", 11, "bold"), bg="grey")
        Tbprice_label.place(x=280, y=140)
        
        ruppe_label = Label(right_frame, text=" ₹ ", font=(
            "times new roman", 20, "bold"), bg="grey")
        ruppe_label.place(x=330, y=160)

        self.Tbprice_entry = Entry(right_frame, textvariable=self.TabletPrice, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.Tbprice_entry.place(x=360, y=162,width=70,height=30)

        #### in right frame small frame #####

        newframe = Frame(right_frame, bg='darkgreen', bd=5, relief=RIDGE)
        newframe.place(x=440, y=5, width=150, height=185)

          ###### button in this frame ###
        add_date = Button(newframe, text="Exp. Date", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                            bd=3, command=self.Adddate, relief=RIDGE, activebackground="black", activeforeground="white")
        add_date.grid(row=0, column=0)  
          
        add_button = Button(newframe, text="Add", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                            bd=3, command=self.AddMed, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=1, column=0)

        updatenew_button = Button(newframe, text="Update", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                                  bd=3, command=self.Update_med, relief=RIDGE, activebackground="black", activeforeground="white")
        updatenew_button.grid(row=2, column=0)

        delnew_button = Button(newframe, text="Delete", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.Delete_med)
        delnew_button.grid(row=3, column=0)

        clr_button = Button(newframe, text="Clear", command=self.clear_med, font=("arial", 13, "bold"), width=13,
                            fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        clr_button.grid(row=4, column=0)

        ##### scrollbar frame in right frame ####
        side_frame = Frame(right_frame, bd=4, relief=RIDGE, bg="dark green")
        side_frame.place(x=0, y=225, width=600, height=150)

        ### scrollbar code ###

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        self.medicine_table = ttk.Treeview(side_frame, column=(
            "ref", "medname" ,"IssueDate", "Expdate", "sideeffect", "warning" , "TabletPrice"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")
        self.medicine_table.heading("IssueDate", text="Issue Date")
        self.medicine_table.heading("Expdate", text="Exp Date")
        self.medicine_table.heading("sideeffect", text="Side Eff.")
        self.medicine_table.heading("warning", text="Warning")
        self.medicine_table.heading("TabletPrice", text="Tblt Price")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=50)
        self.medicine_table.column("medname", width=100)
        self.medicine_table.column("IssueDate", width=70)
        self.medicine_table.column("Expdate", width=70)
        self.medicine_table.column("sideeffect", width=110)
        self.medicine_table.column("warning", width=110)
        self.medicine_table.column("TabletPrice", width=60)

        self.medicine_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_datamed()

        ######### down frame #######
        down_frame = Frame(self.root, bg='grey', bd=10, relief=RIDGE)
        down_frame.place(x=0, y=570, width=1535, height=225)

        ########## scrollbar in down frame ########
        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
        scroll_frame.place(x=0, y=0, width=1525, height=218)

        ##### scrollbar code #####
        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame, column=("Patient ID","Mobile No.","Patient Name","Hospital Name","Ref No", "Type", "Medi name", "lot no", "issue", "exp",
                                       "uses", "side effect", "warning", "dosage", "price", "product","Total Price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("Patient ID", text="Patient ID")
        self.info_table.heading("Mobile No.", text="Mobile No.")
        self.info_table.heading("Patient Name", text="Patient Name")
        self.info_table.heading("Hospital Name", text="Hospital Name")
        self.info_table.heading("Ref No", text="Ref No.")
        self.info_table.heading("Type", text="Type Of Medicine")
        self.info_table.heading("Medi name", text="Medicine Name")
        self.info_table.heading("lot no", text="Lot No.")
        self.info_table.heading("issue", text="Issue Date")
        self.info_table.heading("exp", text="Expiry Date")
        self.info_table.heading("uses", text="Uses")
        self.info_table.heading("side effect", text="Side Effects")
        self.info_table.heading("warning", text="Prec & Warning")
        self.info_table.heading("dosage", text="Dosage")
        self.info_table.heading("price", text="Medicine Price")
        self.info_table.heading("product", text="Product Qt.")
        self.info_table.heading("Total Price", text="Total Price")

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("Patient ID", width=70)
        self.info_table.column("Mobile No.", width=100)
        self.info_table.column("Patient Name", width=100)
        self.info_table.column("Hospital Name" , width=100)
        self.info_table.column("Ref No" , width=60)
        self.info_table.column("Type" , width=100)
        self.info_table.column("Medi name" , width=100)
        self.info_table.column("lot no" , width=80)
        self.info_table.column("issue" , width=80)
        self.info_table.column("exp" , width=80)
        self.info_table.column("uses", width=90)
        self.info_table.column("side effect", width=100)
        self.info_table.column("warning", width=100)
        self.info_table.column("dosage", width=70)
        self.info_table.column("price", width=90)
        self.info_table.column("product", width=80)
        self.info_table.column("Total Price", width=70)

        self.info_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_new()

    ####### MEDICINE ADD FUNCTIONALITY  DECLARATION #######
    def Adddate(self):
        self.Expiry_data.set(self.Issue_data.get())
        messagebox.showinfo("Warning", "PLEASE CHANGE THE ISSUE DATE",parent=self.root)
    
    def AddMed(self):

        if self.ref_variable.get() == "" or self.addmed_variable.get() == "" or self.Issue_data.get() == "" or self.Expiry_data.get() == "" or self.sideeffect.get() =="" or self.warning.get() == "" or self.TabletPrice.get() =="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)

        else:
            conn = sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
            my_cursor = conn.cursor()
            my_cursor.execute("Insert into pharma(Ref_no,Med_name,Issue_date,Expiry_date,Side_effect,Warning,Tablet_price) values(?,?,?,?,?,?,?)", (
                self.ref_variable.get(),
                self.addmed_variable.get(),
                self.Issue_data.get(),
                self.Expiry_data.get(),
                self.sideeffect.get(),
                self.warning.get(),
                self.TabletPrice.get(),))

            conn.commit()
            self.fetch_datamed()
            conn.close()

            messagebox.showinfo("Success", "MEDICINE ADDED",parent=self.root)

    def fetch_datamed(self):
        conn = sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("", END, values=i)

            conn.commit()
            conn.close()

    def medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.ref_variable.set(row[0])
        self.addmed_variable.set(row[1])
        self.Issue_data.set(row[2])
        self.Expiry_data.set(row[3])
        self.sideeffect.set(row[4])
        self.warning.set(row[5])
        self.TabletPrice.set(row[6])    
     
    def generate_receipt(self):
        # Create a new PDF with ReportLab
        messagebox.showinfo("Success", "PDF IS GENERATED ANS SAVED ON THE DEVICE",parent=self.root)
        pdf = canvas.Canvas("Report.pdf")
        
        conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        self.pat = StringVar()
        new_cursor.execute("select PATIENT_ID from Information where Mobileno=?",(self.Mobileno_entry.get(),))
        row=new_cursor.fetchall()
        list1=[rowq for rows in row for rowq in rows]
        print(*list1)
        self.pat.set(*list1)

        # Set up the font
        pdf.setFont("Times-Bold", 20)

        # Write the header
        pdf.drawString(210, 800, "Receipt for Order #" + str(self.pat.get()))
        pdf.line(30, 775, 570, 775)
        pdf.drawString(40, 750, "Patient Name : " + str(self.patientname.get()))
        pdf.drawString(40, 710, "Mobile No. : " + str(self.Mobileno_entry.get()))
        pdf.drawString(40, 670, "Hospital : " + str(self.hospital.get()))
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%d-%m-%Y")
        pdf.drawString(40, 630, "Date : " +formatted_date )
        pdf.line(30, 600, 570, 600)
        pdf.line(30, 565, 570, 565)

        
        pdf.drawString(35, 580, "Item ID : " )
        pdf.drawString(150, 580, "Item Name : " )
        pdf.drawString(450, 580, "Price : " )
        
        # Write the items
        y = 530
        pdf.drawString(50, y, ""+str(self.refno_var.get()))
        pdf.drawString(160, y, ""+str(self.medicine_var.get()))
        pdf.drawString(465, y, "₹" + str(self.tnp.get()))
        
        
        pdf.line(140, 600, 140, 90)
        pdf.line(440, 600, 440, 90)
        
        
        pdf.line(30, 125, 570, 125)
        pdf.line(30, 600, 30, 90)
        pdf.line(570, 600, 570, 90)
        # Write the total
        pdf.drawString(50, 100, "Total:")
        pdf.drawString(470, 100, "₹" + str(self.tnp.get()))
        pdf.line(30, 90, 570, 90)
        # Save the PDF
        pdf.showPage()
        pdf.save()
     
    def fetd(self):
        conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        num1 = int(float(self.refno_var.get()))
        new_cursor.execute('SELECT * FROM pharma where Ref_no=?;',[num1])
        row=new_cursor.fetchall()
        list1=[rowq for rows in row for rowq in rows]
        print(list1)
        self.medicine_var.set(list1[1])
        self.issuedt_var.set(list1[2])
        self.expdt_var.set(list1[3])
        self.sideeffect_var.set(list1[4])
        self.warning_var.set(list1[5])
        self.price_var.set(list1[6])
        # print(self.refno_var.get())
        
        conn.commit()
             
    def Update_med(self):
        
        if self.ref_variable.get() == "" or self.addmed_variable.get()=="" or self.Issue_data.get() == "" or self.Expiry_data.get() == "" or self.sideeffect.get() =="" or self.warning.get() == "" or self.TabletPrice.get() =="":

            messagebox.showerror("Error", "All data is required",parent=self.root)
        else:
            try:
                conn = sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
                my_cursor = conn.cursor()

                my_cursor.execute("Update pharma set Med_name=?,Issue_date=?,Expiry_date=?,Sife_effect=?,Warning=?, Tablet_price=? where Ref_no=?", (
                                                                                self.addmed_variable.get(),
                                                                                self.Issue_data.get(),
                                                                                self.Expiry_data.get(),
                                                                                self.sideeffect.get(),
                                                                                self.warning.get(),
                                                                                self.TabletPrice.get(),
                                                                                self.ref_variable.get(),
                                                                                ))

                conn.commit()
                messagebox.showinfo("Update", "Successfully Updated", parent=self.root)
                self.fetch_datamed()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)

    def Delete_med(self):
        if self.ref_variable.get()=="":
            messagebox.showerror("Error","Ref no is required",parent=self.root)
        else:
            try:
                conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
                my_cursor=conn.cursor()
            
                my_cursor.execute("Delete from pharma where Ref_no=? ",(self.ref_variable.get(),))
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_datamed()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)

    def clear_med(self):
        self.ref_variable.set("")
        self.addmed_variable.set("")
        self.Expiry_data.set("")
        self.sideeffect.set("")
        self.warning.set("")
        self.TabletPrice.set("")
        
    def deleteinfo(self):
        try:
                conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
                my_cursor=conn.cursor()
            
                my_cursor.execute("Delete from Information where Mobileno=? and REF_NO=?",(self.Mobileno_entry.get(),self.refno_var.get(),))
                
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_new()
        except Exception as e:
            messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)
  
    ######## Billing ########
    def bill(self):
        tol1 = int(float(self.quantity_var.get()))
        tol2 = int(float(self.price_var.get()))
        # self.tol= ((self.quantity_var.get())*(self.price_var.get()))
        ttp=int(float(tol1*tol2))
        self.totalp.set(ttp)
        mob=len(self.Mobileno.get())
        if mob != 10:
            messagebox.showerror("Error","Mobile Number is Invalid",parent=self.root)

    def disc(self):
        tol1 = int(float(self.totalp.get()))
        tol2 = int(float(self.discount.get()))
        # self.tol= ((self.quantity_var.get())*(self.price_var.get()))
        ttp=int(float(tol1-(tol1*(tol2/100))))
        self.tnp.set(ttp)

    def balan(self):
        tol1 = int(float(self.tnp.get()))
        tol2 = int(float(self.amtp.get()))
        # self.tol= ((self.quantity_var.get())*(self.price_var.get()))
        ttp=int(float(tol2-tol1))
        if (ttp<0):
            messagebox.showwarning("Bill Error","Amount is not paid fully",parent=self.root)
        self.balance.set(ttp)
        messagebox.showwarning("DATA STORING NOTIFICATION","Store The Information After The Notification",parent=self.root)

    ######## MEDICINE DEPARTMENT FUNCTIONALITY #######
    def addmedicine(self):
        if self.Mobileno_entry.get() == "" or self.patientname.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
            new_cursor=conn.cursor()
            
            new_cursor.execute("select * from Information where Mobileno=?",(self.Mobileno_entry.get(),))
            roww = new_cursor.fetchall()
            exist1=[rowwq for rowws in roww for rowwq in rowws]
            print(exist1)
            new_cursor.execute('select PATIENT_ID from Information;')
            row=new_cursor.fetchall()
            list1=[rowq for rows in row for rowq in rows]
            print(list1)
            if list1 == []:
                print("the list is empty")
                va = 0
            else:
                print("the list is not empty")
                va = max(list1)
                
            if exist1 == [] :
                print("the phase 1 is selected")
                print(va)
                va= va+1
                print(va)
                self.patientid.set(va)
                new_cursor.execute("Insert into Information(PATIENT_ID,Mobileno,Patient_Name,Hospital,REF_NO,TYPE_OF_MED,MED_NAME,LOT_NO,ISSUE_DT,EXP_DT,USES,SIDE_EFFECT,PRECAUTION,DOSAGE,PRICE,QUANTITY,Total_Price) values(?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                self.patientid.get(),
                self.Mobileno_entry.get(),
                self.patientname.get(),
                self.hospital.get(),
                self.refno_var.get(),
                self.typemed_var.get(),
                self.medicine_var.get(),
                self.lotno_var.get(),
                self.issuedt_var.get(),
                self.expdt_var.get(),
                self.uses_var.get(),
                self.sideeffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.quantity_var.get(),
                self.tnp.get(),
                ))
                conn.commit()
                self.fetch_new()
                messagebox.showinfo("Success"," Data Successfully added & Print the Bill ",parent=self.root)
            
            elif exist1 != [] :
                print("the phase 2 is selected")
                self.pat = StringVar()
                new_cursor.execute("select PATIENT_ID from Information where Mobileno=?",(self.Mobileno_entry.get(),))
                row=new_cursor.fetchall()
                list1=[rowq for rows in row for rowq in rows]
                print(*list1)
                self.pat.set(*list1)
                new_cursor.execute("Insert into Information(PATIENT_ID,Mobileno,Patient_Name,Hospital,REF_NO,TYPE_OF_MED,MED_NAME,LOT_NO,ISSUE_DT,EXP_DT,USES,SIDE_EFFECT,PRECAUTION,DOSAGE,PRICE,QUANTITY,Total_Price) values(?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(                                                                              
                self.pat.get(),
                self.Mobileno_entry.get(),
                self.patientname.get(),
                self.hospital.get(),
                self.refno_var.get(),
                self.typemed_var.get(),
                self.medicine_var.get(),
                self.lotno_var.get(),
                self.issuedt_var.get(),
                self.expdt_var.get(),
                self.uses_var.get(),
                self.sideeffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.quantity_var.get(),
                self.tnp.get(),
                ))
                conn.commit()
                self.fetch_new()
                
                messagebox.showinfo("Success"," Data Successfully added & Print the Bill ",parent=self.root)

    def fetch_new(self):
        conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Information")
        row=new_cursor.fetchall()

        if len(row)!=0:
            self.info_table.delete(*self.info_table.get_children())

            for i in row:
                self.info_table.insert("",END,values=i)
            conn.commit()

    def get_cursor(self,event=""):
        cursor_row=self.info_table.focus()
        content=self.info_table.item(cursor_row)
        row=content["values"]
        self.Mobileno.set(row[1])
        self.patientname.set(row[2])
        self.hospital.set(row[3])
        self.refno_var.set(row[4])
        self.typemed_var.set(row[5])
        self.medicine_var.set(row[6])
        self.lotno_var.set(row[7])
        self.issuedt_var.set(row[8])
        self.expdt_var.set(row[9])
        self.uses_var.set(row[10])
        self.sideeffect_var.set(row[11])
        self.warning_var.set(row[12])
        self.dosage_var.set(row[13])
        self.price_var.set(row[14])
        self.quantity_var.set(row[15])
        self.tnp.set(row[16])

    def update_new(self):
        
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
            new_cursor=conn.cursor()
            new_cursor.execute("Update Information set Patient_Name=?,Hospital=?,REF_NO=?,TYPE_OF_MED=?,MEDNAME=?,LOT_NO=?,ISSUE_DT=?,EXP_DT=?,USES=?,SIDE_EFFECT=?,PRECAUTION=?,DOSAGE=?,PRICE=?,QUANTITY=?,Total_Price=? where PATIENT_ID=?",(
            
            self.patientname.get(),
            self.hospital.get(),
            self.refno_var.get(),
            self.typemed_var.get(),
            self.medicine_var.get(),
            self.lotno_var.get(),
            self.issuedt_var.get(),
            self.expdt_var.get(),
            self.uses_var.get(),
            self.sideeffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.quantity_var.get(),
            self.tnp.get(),
            self.patientid.get(),

            ))
            conn.commit()
            self.fetch_new()
            self.clear_new()
            messagebox.showinfo("Success","Successfully updated",parent=self.root)

    def clear_new(self):
        self.Mobileno.set("")
        self.patientname.set("")
        self.hospital.set("")
        self.refno_var.set("")
        self.typemed_var.set("")
        self.medicine_var.set("")
        self.lotno_var.set("")
        self.issuedt_var.set("")
        self.expdt_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
        self.tnp.set("")
        self.discount.set("")
        self.amtp.set("")
        self.balance.set("")
        self.totalp.set("")
        self.patientname.set("")
        self.hospital.set("")


    def search_data(self):
        conn=sqlite3.connect(database=r'F:\pMS\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        selected = self.search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option",parent=self.root)
        else:
            if self.search_by.get()=="Mobile No.":
                new_cursor.execute("Select * from Information where Mobileno = ?",(self.search_txt.get(),))
                # row=new_cursor.fetchone()
                
                row=new_cursor.fetchall()


                if len(row)!=0:
                    
                    self.info_table.delete(*self.info_table.get_children())

                    for i in row:
                        self.info_table.insert("",END,values=i)

                    conn.commit()
                else:
                    messagebox.showwarning("ERROR","NO DATA IN THE TABLE",parent=self.root)
                    
            elif self.search_by.get()=="Patient Name":
                new_cursor.execute("Select * from Information where Patient_Name = ?",(self.search_txt.get(),))
                row=new_cursor.fetchall()

                if len(row)!=0:
                    
                    self.info_table.delete(*self.info_table.get_children())

                    for i in row:
                        self.info_table.insert("",END,values=i)

                    conn.commit()
                else:
                    messagebox.showwarning("ERROR","NO DATA IN THE TABLE",parent=self.root)
           
    def slider(self):
        if self.count>=len(self.txt):
            self.count=-1
            self.text=""
            self.heading.config(text=self.text)
        else:
            self.text=self.text+self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1
        self.heading.after(200,self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(100,self.heading_color)


if __name__ == '__main__':

    root=Tk()
    username="Admin"
    obj=AdminPage(root,username)
    root.mainloop()
