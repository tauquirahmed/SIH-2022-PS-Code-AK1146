from dataclasses import field
from email import message_from_string
from importlib.metadata import metadata
from logging import root
from multiprocessing import parent_process
from multiprocessing.context import set_spawning_popen
from os import stat
import statistics
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image, ImageTk
from numpy import save
from tkinter import messagebox
import pyodbc
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Attendance Sheet")

      img=Image.open(r"Images\att.png")
      img=img.resize((1530,790),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      bg_img=Label(self.root,image=self.photoimg)
      bg_img.place(x=0,y=0,width=1530,height=790)

      title_lbl=Label(bg_img,text="ATTENDANCE SHEET", font=("Times New Roman", 30, "bold"), bg="darkblue", fg="white")
      title_lbl.place(x=0, y=0, width=1530, height=50)

      main_frame=Frame(bg_img, bd=2,bg="white")
      main_frame.place(x=10, y=55, width=1500, height=720)

      Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Attendance Details", font=("Times New Roman",15, "bold"))
      Left_frame.place(x=15, y=10, width=720, height=680)

      Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Attendance Details", font=("Times New Roman",15, "bold"))
      Right_frame.place(x=755, y=10, width=720, height=680)

      Left_inside_frame=Frame(Left_frame, bd=2,relief=RIDGE,bg="white")
      Left_inside_frame.place(x=5, y=5, width=700, height=600)

      Attendance_label=Label(Left_inside_frame, text="Student Id", font=("Times New Roman",15, "bold"))
      Attendance_label.grid(row=0, column=0, padx=10,pady=10, sticky=W)

      Attendance_entry=ttk.Entry(Left_inside_frame, width=50, font=("times new roman", 15, "bold"))
      Attendance_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

      StudentName_label=Label(Left_inside_frame, text="Student Name", font=("Times New Roman",15, "bold"))
      StudentName_label.grid(row=1, column=0, padx=10,pady=10, sticky=W)

      StudentName_entry=ttk.Entry(Left_inside_frame,width=50, font=("times new roman", 15, "bold"))
      StudentName_entry.grid(row=1, column=1, padx=10,pady=10, sticky=W)

      dep_label=Label(Left_inside_frame, text="Department", font=("Times New Roman",15, "bold"))
      dep_label.grid(row=3, column=0, padx=10, sticky=W)

      dep_combo=ttk.Combobox(Left_inside_frame, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      dep_combo["values"]=("Select Department", "CSBS", "IT", "ECE", "CSE")
      dep_combo.current(0)
      dep_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)
      #course
      course_label=Label(Left_inside_frame,text="Course", font=("Times New Roman",15, "bold"))
      course_label.grid(row=4, column=0, padx=10)

      course_combo=ttk.Combobox(Left_inside_frame, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      course_combo["values"]=("Select Course", "B.Tech", "B.Sc", "M.Tech", "M.Sc")
      course_combo.current(0)
      course_combo.grid(row=4, column=1, padx=2, pady=10, sticky=W)

      attendance_label=Label(Left_inside_frame,text="Attendance", font=("Times New Roman",15, "bold"))
      attendance_label.grid(row=5, column=0, padx=10)

      attendance_combo=ttk.Combobox(Left_inside_frame, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      attendance_combo["values"]=("Select Course", "Present", "Absent")
      attendance_combo.current(0)
      attendance_combo.grid(row=5, column=1, padx=2, pady=10, sticky=W)

      btn_frame=Frame(Left_inside_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=5, y=300, width=690, height=200)

      import_btn=Button(btn_frame,text="Import csv",command=self.importCSV, width=58,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      import_btn.grid(row=0, column=0)

      # export_btn=Button(btn_frame,text="Export csv", width=58,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      # export_btn.grid(row=1, column=0)

      # Update_btn=Button(btn_frame,text="Update", width=58,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      # Update_btn.grid(row=2, column=0)

      # Reset_btn=Button(btn_frame,text="Reset",width=58,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      # Reset_btn.grid(row=3, column=0)

      table_frame=Frame(Right_frame, bd=2,relief=RIDGE,bg="white")
      table_frame.place(x=5, y=5, width=705, height=620)

      #==========scroll bar============
      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

      self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("Student ID","Student Name", "Course", "Department","time", "date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)

      scroll_x.config(command=self.AttendanceReportTable.xview)
      scroll_y.config(command=self.AttendanceReportTable.yview)

      self.AttendanceReportTable.heading("Student ID", text="Student ID")
      self.AttendanceReportTable.heading("Student Name", text="Student Name")
      self.AttendanceReportTable.heading("Course", text="Course")
      self.AttendanceReportTable.heading("Department", text="Department")
      self.AttendanceReportTable.heading("time", text="Time")
      self.AttendanceReportTable.heading("date", text="Date")
      self.AttendanceReportTable.heading("Attendance", text="Attendance")

      self.AttendanceReportTable["show"]="headings"

      self.AttendanceReportTable.column("Student ID", width=100)
      self.AttendanceReportTable.column("Student Name", width=200)
      self.AttendanceReportTable.column("Course", width=100)
      self.AttendanceReportTable.column("Department", width=100)
      self.AttendanceReportTable.column("time", width=100)
      self.AttendanceReportTable.column("date", width=100)
      self.AttendanceReportTable.column("Attendance", width=100)

      self.AttendanceReportTable.pack(fill=BOTH, expand=1)

    #============Fetch Data========
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("", END, values=i)
    
    def importCSV(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File", "*.*")), parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile, delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)

    # def exportCSV(self):
    #   try:
    #     if len(mydata)<1:
    #       messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
    #       return False
    #   fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File", "*.*")), parent=self.root)
    #   with open(fln, mode="w", newline="") as myfile:
    #     exp_write=csv.writer(myfile, delimiter=",")
    #     for i in mydata:
    #       exp_write.writerow(i)
    #     messagebox.showinfo("Data Export", "Your Data Exported to "+os.path.basename(fln)+" successfully")
      
    #   except Exception as es:
    #     messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()