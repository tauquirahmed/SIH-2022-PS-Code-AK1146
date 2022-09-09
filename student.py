from email import message_from_string
from logging import root
from multiprocessing import parent_process
from multiprocessing.context import set_spawning_popen
from os import stat
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from numpy import save
from tkinter import messagebox
import cv2
import os
import sqlite3


class Student:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Student Management System")

      # ============variables================
      self.var_studentname=StringVar()
      self.var_studentID=StringVar()
      self.var_gender=StringVar()
      self.var_Course=StringVar()
      self.var_Dept=StringVar()
      self.var_Year=StringVar()
      self.var_semester=StringVar()
      self.var_mob=StringVar()
      self.var_email=StringVar()


      #background Image
      img=Image.open(r"Images\Background.jpg")
      img=img.resize((1530,790),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      bg_img=Label(self.root,image=self.photoimg)
      bg_img.place(x=0,y=0,width=1530,height=790)

      title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman", 30, "bold"), bg="darkblue", fg="white")
      title_lbl.place(x=0, y=0, width=1530, height=50)

      main_frame=Frame(bg_img, bd=2,bg="white")
      main_frame.place(x=10, y=55, width=1500, height=720)

      #Left Frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman",15, "bold"))
      Left_frame.place(x=15, y=10, width=720, height=680)

      #Right Frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman",15, "bold"))
      Right_frame.place(x=755, y=10, width=720, height=680)

      #Current Course Frame
      Currrent_Course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current Course Details", font=("Times New Roman",15, "bold"))
      Currrent_Course_frame.place(x=5, y=10, width=705, height=150)
      #department
      dep_label=Label(Currrent_Course_frame, text="Department", font=("Times New Roman",15, "bold"))
      dep_label.grid(row=0, column=0, padx=10, sticky=W)

      dep_combo=ttk.Combobox(Currrent_Course_frame,textvariable=self.var_Dept, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      dep_combo["values"]=("Select Department", "CSBS", "IT", "ECE", "CSE")
      dep_combo.current(0)
      dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
      #course
      course_label=Label(Currrent_Course_frame,text="Course", font=("Times New Roman",15, "bold"))
      course_label.grid(row=0, column=2, padx=10)

      course_combo=ttk.Combobox(Currrent_Course_frame,textvariable=self.var_Course, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      course_combo["values"]=("Select Course", "B.Tech", "B.Sc", "M.Tech", "M.Sc")
      course_combo.current(0)
      course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

      #department
      year_label=Label(Currrent_Course_frame, text="Year", font=("Times New Roman",15, "bold"))
      year_label.grid(row=1, column=0, padx=10, sticky=W)

      year_combo=ttk.Combobox(Currrent_Course_frame,textvariable=self.var_Year, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      year_combo["values"]=("Select Year", "1st", "2nd", "3rd", "4th")
      year_combo.current(0)
      year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
      #course
      semester_label=Label(Currrent_Course_frame, text="Semester", font=("Times New Roman",15, "bold"))
      semester_label.grid(row=1, column=2, padx=10)

      semester_combo=ttk.Combobox(Currrent_Course_frame, textvariable=self.var_semester,font=("Times New Roman",15, "bold"), width=17, state="readonly")
      semester_combo["values"]=("Select Semester", "1", "2", "3", "4", "5","6","7","8")
      semester_combo.current(0)
      semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

      #Student Information
      Student_Information_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Student Information", font=("Times New Roman",15, "bold"))
      Student_Information_frame.place(x=5, y=165, width=705, height=460)

      StudentId_label=Label(Student_Information_frame, text="Student Id", font=("Times New Roman",15, "bold"))
      StudentId_label.grid(row=0, column=0, padx=10,pady=10, sticky=W)

      StudentId_entry=ttk.Entry(Student_Information_frame,textvariable=self.var_studentID, width=50, font=("times new roman", 15, "bold"))
      StudentId_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

      StudentName_label=Label(Student_Information_frame, text="Student Name", font=("Times New Roman",15, "bold"))
      StudentName_label.grid(row=1, column=0, padx=10,pady=10, sticky=W)

      StudentName_entry=ttk.Entry(Student_Information_frame, textvariable=self.var_studentname,width=50, font=("times new roman", 15, "bold"))
      StudentName_entry.grid(row=1, column=1, padx=10,pady=10, sticky=W)

      Gender_label=Label(Student_Information_frame, text="Gender", font=("Times New Roman",15, "bold"))
      Gender_label.grid(row=3, column=0, padx=10,pady=10, sticky=W)

      Gender_combo=ttk.Combobox(Student_Information_frame,textvariable=self.var_gender ,width=50, font=("times new roman", 15, "bold"), state="readonly")
      Gender_combo["values"]=("Select Gender", "Male", "Female", "Others")
      Gender_combo.grid(row=3, column=1, padx=10,pady=10, sticky=W)

      Contact_label=Label(Student_Information_frame, text="Contact Number", font=("Times New Roman",15, "bold"))
      Contact_label.grid(row=4, column=0, padx=10,pady=10, sticky=W)

      Contact_entry=ttk.Entry(Student_Information_frame,textvariable=self.var_mob ,width=50, font=("times new roman", 15, "bold"))
      Contact_entry.grid(row=4, column=1, padx=10,pady=10, sticky=W)

      Email_label=Label(Student_Information_frame, text="Email Id", font=("Times New Roman",15, "bold"))
      Email_label.grid(row=5, column=0, padx=10,pady=10, sticky=W)

      Email_entry=ttk.Entry(Student_Information_frame, textvariable=self.var_email,width=50, font=("times new roman", 15, "bold"))
      Email_entry.grid(row=5, column=1, padx=10,pady=10, sticky=W)

      #radiobuttons
      self.var_radiobtn1=StringVar()
      radiobtn1=ttk.Radiobutton(Student_Information_frame,variable=self.var_radiobtn1, text="Take Photo Sample)", value="Yes")
      radiobtn1.grid(row=6, column=0)

      radiobtn2=ttk.Radiobutton(Student_Information_frame,variable=self.var_radiobtn1, text="No Photo Sample)", value="No")
      radiobtn2.grid(row=6, column=1)

      #buttons Frame
      btn_frame=Frame(Student_Information_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=5, y=300, width=690, height=150)

      save_btn=Button(btn_frame,text="Save",command=self.add_data, width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      save_btn.grid(row=0, column=0)

      update_btn=Button(btn_frame,text="Update",command=self.update_data, width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      update_btn.grid(row=0, column=1)

      Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Delete_btn.grid(row=1, column=0)

      Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data ,width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Reset_btn.grid(row=1, column=1)

      Take_Photo_Sample_btn=Button(btn_frame,text="Take Photo Sample", command=self.generate_dataset,width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Take_Photo_Sample_btn.grid(row=2, column=0)

      Update_Photo_Sample_btn=Button(btn_frame,text="Update Photo Sample", width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Update_Photo_Sample_btn.grid(row=2, column=1)

      #=============Search System================
      # Search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 15, "bold"))
      # Search_frame.place(x=10, y=5, width=700, height=100)

      # Search_label=Label(Search_frame, text="Search by", font=("Times New Roman",15, "bold"), bg="red", fg="white")
      # Search_label.grid(row=0, column=0,padx=2, pady=10, sticky=W)

      # search_combo=ttk.Combobox(Search_frame, font=("Times New Roman",15, "bold"), width=12, state="readonly")
      # search_combo["values"]=("Select", "Name", "Student Id", "Mobile No.")
      # search_combo.current(0)
      # search_combo.grid(row=0, column=1,padx=2, pady=10, sticky=W)

      # SearchEntry=ttk.Entry(Search_frame, width=18, font=("Times New Roman",15, "bold"))
      # SearchEntry.grid(row=0, column=2,padx=2, pady=10, sticky=W)

      # search_btn=Button(Search_frame,text="Search", width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
      # search_btn.grid(row=0, column=3, padx=2, pady=10)

      # Showall_btn=Button(Search_frame,text="Show All", width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
      # Showall_btn.grid(row=0, column=4, padx=2, pady=10)

      #=============Table Frame==============
      Table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
      Table_frame.place(x=10, y=10, width=700, height=500)

      scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

      self.student_table=ttk.Treeview(Table_frame,column=("StudentName", "StudentId","Gender", "Course", "Department", "Year", "Semester", "Mobile", "Email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)

      self.student_table.heading("StudentName", text="Student Name")
      self.student_table.heading("StudentId", text="Student Id")
      self.student_table.heading("Gender", text="Gender")
      self.student_table.heading("Course", text="Course")
      self.student_table.heading("Department", text="Department")
      self.student_table.heading("Year", text="Year")
      self.student_table.heading("Semester", text="Semester")
      self.student_table.heading("Mobile", text="Mobile No.")
      self.student_table.heading("Email", text="Email Id")

      self.student_table["show"]="headings"
      self.student_table.column("StudentName", width=100)

      self.student_table.pack(fill=BOTH, expand=1)
      self.student_table.bind("<ButtonRelease>",self.get_cursor)
      self.fetch_data()

    # =================Function================
    def add_data(self):
      if self.var_studentname.get()=="" or self.var_studentID.get()=="" or self.var_Dept.get()=="Select Department":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/SIH.db')
          my_cursor = conn.cursor()
          my_cursor.execute("INSERT INTO student VALUES(?,?,?,?,?,?,?,?,?,?)", (
            self.var_studentname.get(),
            self.var_studentID.get(),
            self.var_gender.get(),
            self.var_Course.get(),
            self.var_Dept.get(),
            self.var_Year.get(),
            self.var_semester.get(),
            self.var_mob.get(),
            self.var_email.get(),
            self.var_radiobtn1.get()
          ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success", "Added Succesfully", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ==============Fetch Data========================
    def fetch_data(self):
      conn=sqlite3.connect('SQL Database/SIH.db')
      my_cursor = conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert('',END, values=i)
      conn.commit()
      conn.close()

    #===================get cursor==============
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]
      
      self.var_studentname.set(data[0])
      self.var_studentID.set(data[1])
      self.var_gender.set(data[2])
      self.var_Course.set(data[3])
      self.var_Dept.set(data[4])
      self.var_Year.set(data[5])
      self.var_semester.set(data[6])
      self.var_mob.set(data[7])
      self.var_email.set(data[8])
      self.var_radiobtn1.set(data[9])

    #=======================update================
    def update_data(self):
      if self.var_studentname.get()=="" or self.var_studentID.get()=="" or self.var_Dept.get()=="Select Department":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try:
          Update=messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
          if Update>0:
            conn=sqlite3.connect('SQL Database/SIH.db')
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE student SET StudentName=?, Gender=?, Course=?, Department=?, Year=?, Semester=?, Mobile=?, Email=?, Photo=? where StudentId=?", (
            self.var_studentname.get(),
            self.var_gender.get(),
            self.var_Course.get(),
            self.var_Dept.get(),
            self.var_Year.get(),
            self.var_semester.get(),
            self.var_mob.get(),
            self.var_email.get(),
            self.var_radiobtn1.get(),
            self.var_studentID.get()
            ))
          else:
            if not Update:
              return
          messagebox.showinfo("Success", "Student details updated", parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

    #============================delete=============
    def delete_data(self):
      if self.var_studentID.get()=="":
        messagebox.showerror("Error", "Student Id must be required", parent=self.root)
      else:
        try:
            delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
            if delete>0:
              conn=sqlite3.connect('SQL Database/SIH.db')
              my_cursor = conn.cursor()
              sql="DELETE FROM student WHERE StudentId=?"
              val=(self.var_studentID.get(),)
              my_cursor.execute(sql,val)
            else:
              if not delete:
                return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details deleted", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 
    
    def reset_data(self):
      self.var_studentname.set("")
      self.var_studentID.set("")
      self.var_gender.set("Select Gender")
      self.var_Course.set("Select Course")
      self.var_Dept.set("Select Department")
      self.var_Year.set("Select year")
      self.var_semester.set("Select Semetester")
      self.var_mob.set("")
      self.var_email.set("")
      self.var_radiobtn1.set("")

    #======================================Generate Data====================
    def generate_dataset(self):
      if self.var_studentname.get()=="" or self.var_studentID.get()=="" or self.var_Dept.get()=="Select Department":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/SIH.db')
          my_cursor = conn.cursor()
          my_cursor.execute("SELECT * FROM student")
          myresult=my_cursor.fetchall()
          
          my_cursor.execute("UPDATE student SET StudentName=?, Gender=?, Course=?, Department=?, Year=?, Semester=?, Mobile=?, Email=?, Photo=? where StudentId=?", (
            self.var_studentname.get(),
            self.var_gender.get(),
            self.var_Course.get(),
            self.var_Dept.get(),
            self.var_Year.get(),
            self.var_semester.get(),
            self.var_mob.get(),
            self.var_email.get(),
            self.var_radiobtn1.get(),
            self.var_studentID.get()
            ))
          id=self.var_studentID.get()
          img_counter=id;
          cam=cv2.VideoCapture(0)
          cv2.namedWindow("Capture Image")
          path = 'ImagesAttendance'

          while True:
            ret, frame=cam.read()
            
            if not ret:
              print("failed to grab frame")
              break

            cv2.imshow("Test", frame)

            k=cv2.waitKey(1)

            if k%256==27:
              print("Exit key pressed:")
              break

            elif k%256==32:
              img_name="{}.jpeg".format(img_counter)
              cv2.imwrite(os.path.join(path,img_name), frame)
              print("Image Captured")
              break

          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()

          cam.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result", "Generating dataset completed")
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 
    


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()