from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import pymysql
from PIL import Image, ImageTk


# ------------------------------ Great Class -----------------------------------------------------
class Library:
    def __init__(self, lib):
        self.lib = lib
        self.lib.title('Library Management')
        self.lib.geometry('1000x550+100+100')  # تعديل الموضع ليكون أكثر وضوحاً
        self.lib.resizable(False, False)
        self.lib.iconbitmap("S:\\test\\pythonProject\\.venv\\library.ico")
        self.lib.config(background='#dcdcdc')

        # عنوان التطبيق
        title = Label(self.lib, text='Space Library of Books 🌌📚', font=('Bold', 15), bg='#d4af37', fg='#f5f5f5')
        title.pack(fill=X)

        # إضافة صورة
        try:
            img = Image.open("S:\\test\\pythonProject\\.venv\\beautiful-libraries.png")
            resized_img = img.resize((1000, 550))
            photo = ImageTk.PhotoImage(resized_img)
            panel = Label(self.lib, image=photo)
            panel.place(x=0,y=0,relwidth=1,relheight=1)
            self.photo = photo  # للحفاظ على الصورة في الذاكرة
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {str(e)}")



        #-------------------- Great primary destination ------------------------------
        self.search_var = StringVar()
        self.book_list=[]


        # ------------------------- Sign Up Books -----------------------------
        bt1 = Button(self.lib,text='Sign Up Books',font=('Bold',15),bg='#B87333',fg='black',command= self.sign_up)
        bt1.place(x=40,y=120, width=250,height=35)
        #-------------------------------- sign up membership ------------------------
        bt_mem = Button(self.lib,text='Sign Up Membership',font=('Bold',15),bg='#B87333',fg='black',command=self.sign_mem)
        bt_mem.place(x=40,y=220,width=250,height=35)
        #------------------------------------------ Borrow Books ------------------------------
        bt_borr = Button(self.lib, text='Borrow Books', font=('Bold', 15), bg='#B87333', fg='black',command=self.borrow)
        bt_borr.place(x=40, y=320, width=250, height=35)
        #--------------------------------------------- Search Books -----------------------------
        bt_search = Button(self.lib, text='Search Books',font=('Bold', 15), bg='#B87333', fg='black',command=self.search_book)
        bt_search.place(x=800,y=30,width=130,height=35)

        entry = Entry(self.lib,font=('Helvetica', 14),textvariable=self.search_var)
        entry.place(x=350,y=30,width=430)
        #-------------------------------------- Viwe Borrow Books ------------------------------
        bt_search = Button(self.lib, text='Viwe Borrow', font=('Bold', 15), bg='#B87333', fg='black',command=self.view_borrow)
        bt_search.place(x=40, y=420, width=250, height=35)
        # ------------------------------- Books comeing soon ----------------------------
        bt_com = Button(self.lib, text='Books comeing soon', font=('Bold', 15), bg='#B87333', fg='black')
        bt_com.place(x=700, y=120, width=250, height=35)
        # --------------------------------------------- Late Penalties ----------------------
        bt_late = Button(self.lib, text='Late Penalties', font=('Bold',15),bg='#B87333',fg='black',command=self.late_pena)
        bt_late.place(x=700,y=220,width=250,height=35)
        # ------------------------------------ about us ----------------------------
        bt_about = Button(self.lib, text='About US', font=('Bold', 15), bg='#B87333', fg='black',command=self.about_us)
        bt_about.place(x=700, y=320, width=250, height=35)
        # ----------------------------------- Exit -----------------------------------
        bt_late = Button(self.lib, text='Exit', font=('Bold', 16), bg='#B87333', fg='black', command=self.lib.quit)
        bt_late.place(x=700, y=420, width=250, height=35)

        # search book
    def search_book(self):
            # الحصول على مصطلح البحث
            search_term = self.search_var.get().strip().lower()
            search_results = []  # قائمة لتخزين النتائج

            # البحث في قائمة الكتب
            for book in self.book_list:  # نستخدم self.book_list هنا
                if search_term in book['name'].lower():  # البحث في العنوان
                    search_results.append(book)

            # عرض النتائج فقط
            self.display_search_results(search_results)

    def display_search_results(self, results):
            # إنشاء نافذة جديدة لعرض نتائج البحث
            result_window = Toplevel(self.lib)
            result_window.title("Search Results")
            result_window.geometry("600x400")

            # قائمة لعرض النتائج
            listbox = Listbox(result_window, width=80, height=20)
            listbox.pack(pady=20)

            # إدراج النتائج في القائمة
            for result in results:
                listbox.insert(END, f"Title: {result['name']}, Author: {result['author']}, Type: {result['type']}")

            # إذا لم تكن هناك نتائج
            if not results:
                listbox.insert(END, "No results found.")

        # def about us

    def about_us(self):
            messagebox.showinfo('About us', 'This GUI make design by Mohamed Eid ')


    # sign member
    def sign_mem(self):
        mem = Toplevel(self.lib)
        mem.geometry('650x650+1+1')
        mem.title('Sign Member')
        mem.iconbitmap("S:\\test\\pythonProject\\.venv\\my_books.ico")
        mem.config(background='#13402F')
        mem.resizable(False, False)

        # varible

        self.f_name_v = StringVar()
        self.m_name_v = StringVar()
        self.l_name_v =StringVar()
        self.email_v = StringVar()
        self.password_v = StringVar()
        self.con_password_v = StringVar()
        self.gender_v = StringVar()

        # label frist name
        l_name_fr = Label(mem,text='Frist Name',font=('semi Bold',16),bg='#53A6A6',fg='#165941')
        l_name_fr.place(x=60,y=30,width=280)
        en_name_fr = Entry(mem,font=('semi Bold',13),fg='#57A6A1',justify='center',textvariable=self.f_name_v)
        en_name_fr.place(x=60,y=70,width=280)

        # middle name

        l_name_mid = Label(mem, text='Middle Name', font=('semi Bold', 16), bg='#53A6A6', fg='#165941')
        l_name_mid.place(x=60,y=110,width=280)
        en_name_mid = Entry(mem, font=('semi Bold', 13), fg='#57A6A1', justify='center',textvariable=self.m_name_v)
        en_name_mid.place(x=60,y=150,width=280)

        # last name

        l_name_la = Label(mem, text='last Name', font=('semi Bold', 16), bg='#53A6A6', fg='#165941')
        l_name_la.place(x=60,y=190,width=280)
        en_name_la = Entry(mem, font=('semi Bold', 13), fg='#57A6A1', justify='center',textvariable=self.l_name_v)
        en_name_la.place(x=60,y=230,width=280)

        #  e-mail

        l_email = Label(mem, text='E-Mail', font=('semi Bold', 16), bg='#53A6A6', fg='#165941')
        l_email.place(x=60,y=270,width=280)
        en_email = Entry(mem, font=('semi Bold', 13), fg='#57A6A1', justify='center',textvariable=self.email_v)
        en_email.place(x=60,y=310,width=280)

        # password

        l_password = Label(mem, text='Password', font=('semi Bold', 16), bg='#53A6A6', fg='#165941')
        l_password.place(x=60,y=350,width=280)
        en_password = Entry(mem, font=('semi Bold', 13), fg='#57A6A1', justify='center',show='*',textvariable=self.password_v)
        en_password.place(x=60,y=390,width=280)

        # confirme password

        l_password_co = Label(mem, text='Confirm Password', font=('semi Bold', 16), bg='#53A6A6', fg='#165941')
        l_password_co.place(x=60,y=430,width=280)
        en_password_co = Entry(mem, font=('semi Bold', 13), fg='#57A6A1', justify='center',show='*',textvariable=self.con_password_v)
        en_password_co.place(x=60,y=470,width=280)

        # chackbox gender

        ch_gender = ttk.Combobox(mem,values=('Male','Femal','Unknow'),state='readonly',textvariable=self.gender_v)
        ch_gender.place(x=380,y=50,width=200)

        # accepte rol

        ch1 = Checkbutton(mem,text='Privacy and Data Collection')
        ch1.place(x=380,y=100,width=200)
        # ------------------------------------
        ch2 = Checkbutton(mem,text='Intellectual Property Rights')
        ch2.place(x=380,y=150,width=200)
        # ----------------------------------
        ch3 = Checkbutton(mem,text='Governing Laws')
        ch3.place(x=380,y=200,width=200)
        # -----------------------------------

        bt = Button(mem,text='Registration',font=('Bold',15),bg='#00008B',fg='#57A6A1',command=self.add_mem)
        bt.place(x=380,y=250,width=200)

        # massege confirme

    def con(self):
            messagebox.showinfo('✳','Confirme registration')

    def add_mem(self):
        if self.f_name_v.get()== "" or self.m_name_v.get()== "" or self.l_name_v.get()== "" or self.email_v.get()== "" or  self.password_v.get()== "" or self.con_password_v.get()== "" or   self.gender_v.get()== "" :
            messagebox.showinfo("Error", "All fields are required")
            return

        try:
            mem = pymysql.connect(host='localhost', user='root', password='12345', database='registration')
            cur = mem.cursor()
            cur.execute("insert into member values (%s,%s,%s,%s,%s,%s,%s)", (
                self.f_name_v.get(),
                self.m_name_v.get(),
                self.l_name_v.get(),
                self.email_v.get(),
                self.password_v.get(),
                self.con_password_v.get(),
                self.gender_v.get()

            ))
            mem.commit()
            messagebox.showinfo("Success", "Borrow added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def borrow(self):
            bor = Toplevel(self.lib)
            bor.geometry('850x500+150+150')
            bor.title('Borrow Books')
            bor.iconbitmap("S:\\test\\pythonProject\\.venv\\my_books.ico")
            bor.resizable(False, False)
            bor.config(background='#77B0AA')

            title = Label(bor, text='Borrow Books', bg='#003C43', fg='#77B0AA', font=('Bold', 16))
            title.pack(fill=X, pady=10)

            # المتغيرات
            self.name = StringVar()
            self.email = StringVar()
            self.phone = StringVar()
            self.gender = StringVar()
            self.book = StringVar()
            self.type = StringVar()
            self.author = StringVar()
            self.time_book = StringVar()

            # معلومات المستخدم
            l_name = Label(bor, text='Name', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            l_name.place(x=30, y=50, width=200)
            en_name = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.name)
            en_name.place(x=250, y=50, width=200)

            l_email = Label(bor, text='E-mail', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            l_email.place(x=30, y=110, width=200)
            en_email = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.email)
            en_email.place(x=250, y=110, width=200)

            l_phone = Label(bor, text='Phone', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            l_phone.place(x=30, y=170, width=200)
            en_phone = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.phone)
            en_phone.place(x=250, y=170, width=200)

            l_gender = Label(bor, text='Gender', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            l_gender.place(x=30, y=230, width=200)
            com_gender = ttk.Combobox(bor, values=('Male', 'Female', 'Unknown'), state='readonly',
                                      textvariable=self.gender)
            com_gender.place(x=250, y=230, width=200)

            # معلومات الاستعارة
            book_name = Label(bor, text='Name Book', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            book_name.place(x=480, y=50, width=150)
            en_book = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.book)
            en_book.place(x=650, y=50, width=150)

            book_type = Label(bor, text='Type Book', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            book_type.place(x=480, y=110, width=150)
            en_type = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.type)
            en_type.place(x=650, y=110, width=150)

            book_author = Label(bor, text='Author Book', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            book_author.place(x=480, y=170, width=150)
            en_author = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.author)
            en_author.place(x=650, y=170, width=150)

            book_time = Label(bor, text='Borrowing Time', font=('semiBold', 14), bg='#135D66', fg='#77B0AA')
            book_time.place(x=480, y=230, width=150)
            en_time = Entry(bor, font=('semiBold', 12), fg='#003C43', justify='center', textvariable=self.time_book)
            en_time.place(x=650, y=230, width=150)

            # زر التأكيد
            bt_con = Button(bor, text='Confirm Order', bg='#E3FEF7', fg='#135D66', font=('Bold', 16),
                            command=self.add_borrow)
            bt_con.place(x=345, y=330)

            # رسالة للمستخدم
            m_l = Label(bor, font=('semiBold', 14), bg='#003C43', fg='#77B0AA', text=
            'Dear subscriber, when you confirm the borrowing information, please check your email.')
            m_l.place(x=30, y=400, width=750, height=60)

    def add_borrow(self):
            if (self.name.get() == "" or self.email.get() == "" or self.phone.get() == "" or
                    self.gender.get() == "" or self.book.get() == "" or self.type.get() == "" or
                    self.author.get() == "" or self.time_book.get() == ""):
                messagebox.showinfo("Error", "All fields are required")
                return

            try:
                # الاتصال بقاعدة البيانات باستخدام with لضمان الإغلاق التلقائي
                with pymysql.connect(host='localhost', user='root', password='12345', database='borrow') as bor:
                    with bor.cursor() as cur:
                        cur.execute("""
                            INSERT INTO borr (name, email, phone, gender, book, type, author, time) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                            self.name.get(),
                            self.email.get(),
                            self.phone.get(),
                            self.gender.get(),
                            self.book.get(),
                            self.type.get(),
                            self.author.get(),
                            self.time_book.get()
                        ))
                    bor.commit()
                    messagebox.showinfo("Success", "Borrow added successfully")

                # تحديث عرض الاستعارات إذا كانت النافذة مفتوحة
                if hasattr(self, 'borrow') and self.borrow.winfo_exists():
                    self.fetch_borrow()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")

        # ----------------------- Late Penalties --------------------------

    def late_pena(self):
            late = Toplevel(self.lib)
            late.geometry('1000x770+150+150')
            late.resizable(False, False)
            late.title('Late Penalty')
            late.iconbitmap("S:\\test\\pythonProject\\.venv\\my_books.ico")
            late.config(background='#17153B')

            title = Label(late, text='Late Penalty', bg='#C8ACD6', fg='#2E236C', font=('Bold', 20))
            title.pack(fill=X, pady=10)

            # قواعد المكتبة
            r = Label(late, text='Library Terms of Use', bg='#C8ACD6', fg='#433D8B', font=('Bold', 18))
            r.place(x=30, y=70, width=350)

            r1 = Label(late, text='1- You must register a membership to use the library', bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r1.place(x=30, y=130, width=500)

            r2 = Label(late, text='2- You must abide by the library\'s rules and privacy', bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r2.place(x=30, y=190, width=500)

            r3 = Label(late, text='3- You must adhere to the terms and conditions for borrowing books', bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 14))
            r3.place(x=30, y=250, width=580)

            r4 = Label(late, text='4- You can return borrowed books to any nearest branch', bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r4.place(x=30, y=310, width=500)

            r5 = Label(late,
                       text='5- All borrowers must respect library rules and avoid causing any disturbance to others while using the library',
                       bg='#433D8B', fg='#C8ACD6', font=('semiBold', 12))
            r5.place(x=30, y=370, width=750)

            # غرامات التأخير
            r_b = Label(late, text='Late Penalties', bg='#C8ACD6', fg='#433D8B', font=('Bold', 18))
            r_b.place(x=30, y=430, width=350)

            r6 = Label(late, text='1- Book can be borrowed for a period of 14 to 30 days depending on the type of book',
                       bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r6.place(x=30, y=490, width=750)

            r7 = Label(late, text='2- A small fine will be imposed for each day of delay after the loan period ends',
                       bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r7.place(x=30, y=550, width=720)

            r8 = Label(late, text='3- A maximum of 3-5 books can be borrowed at the same time per reader', bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r8.place(x=30, y=610, width=650)

            r9 = Label(late, text='4- Unavailable books can be reserved for up to 7 days once they become available',
                       bg='#433D8B',
                       fg='#C8ACD6', font=('semiBold', 15))
            r9.place(x=30, y=670, width=750)

            r10 = Label(late,
                        text='5- Books must be returned in the same condition as they were borrowed. In case of damage or loss, the borrower must compensate for the book',
                        bg='#433D8B', fg='#C8ACD6', font=('semiBold', 11))
            r10.place(x=30, y=730, width=950)

        # ----------------------- View Borrow --------------------------

    def view_borrow(self):
            viw = Toplevel(self.lib)
            viw.geometry('1100x600+150+150')
            viw.iconbitmap("S:\\test\\pythonProject\\.venv\\my_books.ico")
            viw.config(background='#9B3922')
            viw.title('View Borrow')
            viw.resizable(False, False)

            # عنوان النافذة
            title = Label(viw, text='View Borrowed Books', font=('Bold', 20), bg='#0C0C0C', fg='#F2613F')
            title.pack(fill=X, pady=10)

            # إنشاء نمط مخصص لعناوين الأعمدة
            style = ttk.Style()
            style.theme_use("clam")  # استخدم "clam" أو "default" أو "alt" لتسهيل تخصيص الأنماط

            # تخصيص نمط عناوين الأعمدة
            style.configure("Custom.Treeview.Heading",
                            background='#F2613F',
                            foreground='#481E14',
                            font=('Bold', 12))

            # يمكن أيضاً تخصيص خلفية الجسم إذا رغبت
            style.configure("Custom.Treeview",
                            background="#D3D3D3",
                            foreground="black",
                            fieldbackground="#D3D3D3")

            # إطار يحتوي على Treeview وأشرطة التمرير
            frame = Frame(viw, bg='#0C0C0C')
            frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

            # أشرطة التمرير الرأسية والأفقية
            scrollbar_y = Scrollbar(frame, orient=VERTICAL)
            scrollbar_y.pack(side=RIGHT, fill=Y)

            scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)
            scrollbar_x.pack(side=BOTTOM, fill=X)

            # إنشاء Treeview وربطه بأشرطة التمرير مع استخدام النمط المخصص
            self.borrow = ttk.Treeview(frame,
                                       columns=("Name", "Type", "Author", "Time"),
                                       show='headings',
                                       yscrollcommand=scrollbar_y.set,
                                       xscrollcommand=scrollbar_x.set,
                                       style="Custom.Treeview")

            # تعريف رؤوس الأعمدة مع استخدام النمط المخصص للعناوين
            self.borrow.heading("Name", text="Name Book", anchor=CENTER)
            self.borrow.heading("Type", text="Type Book", anchor=CENTER)
            self.borrow.heading("Author", text="Author Book", anchor=CENTER)
            self.borrow.heading("Time", text="Borrowing Time", anchor=CENTER)

            # تحديد أعرض الأعمدة (اختياري)
            self.borrow.column("Name", anchor=CENTER, width=250)
            self.borrow.column("Type", anchor=CENTER, width=200)
            self.borrow.column("Author", anchor=CENTER, width=250)
            self.borrow.column("Time", anchor=CENTER, width=200)

            # تعبئة Treeview في الإطار بالكامل
            self.borrow.pack(fill=BOTH, expand=True)

            # ربط أشرطة التمرير بوظائف Treeview
            scrollbar_y.config(command=self.borrow.yview)
            scrollbar_x.config(command=self.borrow.xview)

            # جلب البيانات وعرضها
            self.fetch_borrow()

    def fetch_borrow(self):
            try:
                # الاتصال بقاعدة البيانات باستخدام with لضمان الإغلاق التلقائي
                with pymysql.connect(host='localhost', user='root', password='12345', database='borrow') as bor:
                    with bor.cursor() as cur:
                        cur.execute("SELECT book, type, author, time FROM borr")
                        rows = cur.fetchall()
                        if rows:
                            self.borrow.delete(*self.borrow.get_children())
                            for row in rows:
                                self.borrow.insert("", END, values=row)
            except Exception as e:
                messagebox.showerror("Error", f"Error fetching borrow records: {str(e)}")

        # -------------------------------------- page sign books ----------------------------
    def sign_up(self):
        sin = Toplevel(self.lib)
        sin.geometry('500x500+1+1')
        sin.title('Confirm membreship')
        sin.iconbitmap("S:\\test\\pythonProject\\.venv\\my_books.ico")
        sin.config(background='#13402F')
        sin.resizable(False,False)
        # ------------- ID mem-----------------------
        id_mem = Label(sin,text='Enter The ID ', font=('semi Bold',13),bg='#53A6A6',fg='#165941')
        id_mem.pack(pady=10)
        self.en_id = Entry(sin,font=('semi Bold',13),fg='#57A6A1',justify='center')
        self.en_id.pack(pady=10)
        #----------------------- Name -------------------
        na_mem = Label(sin,text='Username ', font=('semi Bold',13),bg='#53A6A6',fg='#165941')
        na_mem.pack(pady=10)
        self.en_mem = Entry(sin, font=('semi Bold', 13), fg='#57A6A1', justify='center')
        self.en_mem.pack(pady=10)
        #--------------------------- password ---------------------------------
        p_mem = Label(sin,text='Enter Password', font=('semi Bold',13),bg='#53A6A6',fg='#165941')
        p_mem.pack(pady=10)
        self.en_p = Entry(sin, font=('semi Bold', 13), fg='#57A6A1', justify='center',show='*')
        self.en_p.pack(pady=10)
        #------------------------------- button confirm ----------------------------
        self.bt_co = Button(sin,text='Confirme',font=('semi Bold',14),bg='#898C30',fg='#8C5C32',command=self.conf)
        self.bt_co.pack(pady=10)

        #--------------------- function confirme ---------------------




    def conf(self):
        username = self.en_mem.get()
        password = self.en_p.get()
        id = self.en_id.get()
        if username == "m10" and password == "2002" and id == "1234":

            self.sign_books()

        else:
            messagebox.showinfo('!', 'You can not that')

    def sign_books(self):
        class Sign:
            def __init__(self, book, search_var):
                self.book = book
                self.book.title('Sign Books')
                self.book.geometry('1300x650+1+1')
                self.book.iconbitmap("S:\\test\\pythonProject\\.venv\\my_books.ico")
                self.book.config(background='#344C64')

                self.search_var = search_var

                # Variables
                self.id_var = StringVar()
                self.name_var = StringVar()
                self.type_var = StringVar()
                self.author_var = StringVar()
                self.rating_var = StringVar()
                self.country_var = StringVar()
                self.delete_var = StringVar()

                self.search_com = StringVar()



                # Title Label
                title = Label(self.book, text='New Book Registration', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                title.pack(fill=X)

                # Frame for input fields
                fr = Frame(self.book, bg='#577B8D')
                fr.place(x=1, y=30, width=1300, height=200)

                # ID Book
                id_books = Label(fr, text='ID Book', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                id_books.place(x=30, y=30, width=150)
                en_id = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.id_var)
                en_id.place(x=30, y=70, width=150)


                # Book Name
                name_books = Label(fr, text='Name of Book', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                name_books.place(x=30, y=110, width=150)
                en_name = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.name_var)
                en_name.place(x=30, y=150, width=150)

                # Type of Book
                ty_books = Label(fr, text='Type of Book', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                ty_books.place(x=250, y=30, width=150)
                en_ty = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.type_var)
                en_ty.place(x=250, y=70, width=150)

                # Author Name
                ath_books = Label(fr, text='Author of Book', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                ath_books.place(x=250, y=110, width=150)
                en_ath = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.author_var)
                en_ath.place(x=250, y=150, width=150)

                # Country of Author
                cun_lab = Label(fr, text='Country of Author', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                cun_lab.place(x=500, y=30)
                cun_en = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.country_var)
                cun_en.place(x=500, y=70, width=165)

                # Book Rating
                rat_lab = Label(fr, text='Book Rating', font=('Bold', 15), bg='#240750', fg='#57A6A1')
                rat_lab.place(x=500, y=110, width=150)
                en_ret = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.rating_var)
                en_ret.place(x=500, y=150, width=150)

                # Delete Book
                dele_lab = Label(fr, text='Delete Book', font=('semiBold', 15), bg='#C0C0C0', fg='#191970')
                dele_lab.place(x=680, y=30, width=150)
                en_dele = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.delete_var)
                en_dele.place(x=680, y=70, width=150)

                # Delete Button
                bt_dele = Button(fr, text='Delete ', font=('Bold', 15), bg='#98FF98', fg='#191970',command=self.delete_book)

                bt_dele.place(x=680, y=105, width=150)

                # Add Button
                bt_add = Button(fr, text='Add', font=('Bold', 15), bg='#98FF98', fg='#191970',command=self.add_book)
                bt_add.place(x=680, y=155, width=150)

                # Clear Button
                bt_clear = Button(fr,text='Clear', font=('Bold', 15), bg='#98FF98', fg='#191970',command=self.clear)
                bt_clear.place(x=860,y=30,width=150)

                # Updata Button
                # Updata Button (Corrected Typo and Added Command)
                bt_udata = Button(fr, text='Update', font=('Bold', 15), bg='#98FF98', fg='#191970',
                                  command=self.update_book)
                bt_udata.place(x=860, y=80, width=150)

                # Search

                la_search = Label(fr,text='Search', font=('semiBold', 15), bg='#C0C0C0', fg='#191970')
                la_search.place(x=860,y=120,width=150)
                en_search = Entry(fr, font=('Bold', 15), fg='#57A6A1', justify='center',textvariable=self.search_var)
                en_search.place(x=860,y=160,width=150)

                # chackbox search
                com_cearch = ttk.Combobox(fr, values=
                ('id','name','type','author','country','rating'),
                                          state='readonly',textvariable=self.search_com)
                com_cearch.place(x=1050,y=30)
                com_button = Button(fr,text='Search',font=('Bold', 15), bg='#98FF98', fg='#191970',command=self.search)
                com_button.place(x=1050,y=80,width=150)

                # Frame for details
                d_fr = Frame(self.book, bg='#16325B')
                d_fr.place(x=1, y=235, width=1300, height=415)

                # Scrollbars
                sc_x = Scrollbar(d_fr, orient=HORIZONTAL)
                sc_y = Scrollbar(d_fr, orient=VERTICAL)

                # Treeview
                self.book_table = ttk.Treeview(d_fr, columns=(
                    'id','name', 'type', 'author', 'country', 'rating'),
                                               xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)
                self.book_table.place(x=15, y=1, width=1300, height=400)
                sc_x.pack(side=BOTTOM, fill=X)
                sc_y.pack(side=LEFT, fill=Y)
                sc_x.config(command=self.book_table.xview)
                sc_y.config(command=self.book_table.yview)

                # Show headings
                self.book_table['show'] = 'headings'
                self.book_table.heading('id',text='id')
                self.book_table.heading('name', text='name')
                self.book_table.heading('type', text='type')
                self.book_table.heading('author', text='author')
                self.book_table.heading('country', text='country')
                self.book_table.heading('rating', text='rating')
                self.book_table.bind("<ButtonRelease-1>", self.get_cur)


                self.fetch_all()
            def add_book(self):
                # Check if all fields are filled
                if self.name_var.get() == "" or self.type_var.get() == "" or self.author_var.get() == "" or self.country_var.get() == "" or self.rating_var.get() == "":
                    messagebox.showerror("Error", "All fields are required")
                    return  # Stop the function if any field is empty

                try:
                    con = pymysql.connect(host='localhost', user='root', password='12345', database='mylibrary')
                    cur = con.cursor()
                    cur.execute("insert into mylib (id, name, type, author, country, rating) values (%s, %s, %s, %s, %s, %s)", (
                        self.id_var.get(),
                        self.name_var.get(),
                        self.type_var.get(),
                        self.author_var.get(),
                        self.country_var.get(),
                        self.rating_var.get()

                    ))
                    con.commit()
                    self.fetch_all()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success", "Book added successfully")
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}")

            def fetch_all(self):
                try:
                    con = pymysql.connect(host='localhost', user='root', password='12345', database='mylibrary')
                    cur = con.cursor()
                    cur.execute("select * from mylib")
                    rows = cur.fetchall()
                    if rows:
                        self.book_table.delete(*self.book_table.get_children())
                        for row in rows:
                            self.book_table.insert("", END, values=row)
                    con.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}")

            def clear(self):
                self.id_var.set("")
                self.name_var.set("")
                self.type_var.set("")
                self.author_var.set("")
                self.country_var.set("")
                self.rating_var.set("")

            def update_book(self):
                selected = self.book_table.focus()
                if not selected:
                    messagebox.showerror("Error", "No book selected to update")
                    return

                values = self.book_table.item(selected, 'values')
                if not values:
                    messagebox.showerror("Error", "No data found for the selected book")
                    return

                # Ensure all fields are filled
                if self.name_var.get() == "" or self.type_var.get() == "" or self.author_var.get() == "" or self.country_var.get() == "" or self.rating_var.get() == "":
                    messagebox.showerror("Error", "All fields are required")
                    return

                try:
                    con = pymysql.connect(host='localhost', user='root', password='12345', database='mylibrary')
                    cur = con.cursor()
                    cur.execute("""
                        UPDATE mylib 
                        SET name=%s, type=%s, author=%s, country=%s, rating=%s 
                        WHERE id=%s
                    """, (
                        self.name_var.get(),
                        self.type_var.get(),
                        self.author_var.get(),
                        self.country_var.get(),
                        self.rating_var.get(),
                        self.id_var.get()
                    ))
                    con.commit()
                    self.fetch_all()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success", "Book updated successfully")
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}")

            def get_cur(self, ev):
                cur_row = self.book_table.focus()
                contents = self.book_table.item(cur_row)
                row = contents['values']
                self.id_var.set(row[0]),
                self.name_var.set(row[1]),
                self.type_var.set(row[2]),
                self.author_var.set(row[3]),
                self.country_var.set(row[4]),
                self.rating_var.set(row[5])

            def delete_book(self):
                con = pymysql.connect(host='localhost',user='root',password='12345',database='mylibrary')
                cur = con.cursor()
                cur.execute("delete from mylib where name = %s",self.delete_var.get())
                con.commit()
                self.fetch_all()
                con.close()

            def search(self):
                con = pymysql.connect(host='localhost', user='root', password='12345', database='mylibrary')
                cur = con.cursor()
                search_value = "%" + str(self.search_var.get()).strip() + "%"  # القيمة المدخلة من الواجهة الرئيسية
                try:
                    query = f"SELECT * FROM mylib WHERE `name` LIKE %s"
                    cur.execute(query, (search_value,))
                    rows = cur.fetchall()

                    self.book_table.delete(*self.book_table.get_children())  # حذف الصفوف الحالية في الجدول
                    if rows:
                        for row in rows:
                            self.book_table.insert("", END, values=row)
                    else:
                        # إدارة حالة عدم العثور على بيانات
                        self.book_table.insert("", END, values=("No results found",))
                except pymysql.MySQLError as e:
                    messagebox.showerror("Error", f"Error: {str(e)}")
                finally:
                    con.close()

        # فتح نافذة التسجيل وتفعيل البحث
        book = Toplevel(self.lib)
        Sign(book, self.search_var)









if __name__ == "__main__":
    root = Tk()
    app = Library(root)
    root.mainloop()