import imghdr
from readline import get_history_item
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image, ImageTk
from numpy import save
from tkinter import messagebox
import cv2
import os
import numpy as np
import face_recognition
from numpy import genfromtxt
from time import strftime
from datetime import date, datetime
import sqlite3
from realtime_demo import only_face
import demography


def face_recog():
      path = 'ImagesAttendance'
      images = []
      classNames = []
      myList = os.listdir(path)
      print(myList)
      for cl in myList:
          curImg = cv2.imread(f'{path}/{cl}')
          images.append(curImg)
          classNames.append(os.path.splitext(cl)[0])
      print(classNames)

      encodeListKnown = genfromtxt('Files/Encodings.csv', delimiter=',')
      print('Encoding complete')

      cap = cv2.VideoCapture(0)
      now=datetime.now()
      d=now.strftime("%d-%m-%Y")
      str_current_datetime = str(d)
      file_name=str_current_datetime+".csv"
      path_to_file='Attendance/'+file_name
      another_path='Attendance_photos/'+str_current_datetime
      unknown_path='Unknown/'+str_current_datetime
      print(path_to_file)
      if(os.path.exists(another_path)==False):
        os.mkdir(another_path)
      if(os.path.exists(unknown_path)==False):
        os.mkdir(unknown_path)
      if(os.path.exists(path_to_file)==False): 
        file=open(path_to_file,'w')
        print(file.name)
        file.close()
    #   print(d)

      while True:
          success, img = cap.read()
          imgS = cv2.resize(img, (0,0),None,0.25,0.25)
          imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
          facesCurFrame = face_recognition.face_locations(imgS)
          encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

          for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
              matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
              faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
              print(faceDis)
              matchIndex = np.argmin(faceDis)
              accuracy=min(faceDis)
              conn=sqlite3.connect('SQL Database/SIH.db')
              my_cursor = conn.cursor()
              if matches[matchIndex] and accuracy<0.4:
                  name = classNames[matchIndex].upper()
                  print(name)
                  y1,x2,y2,x1 = faceLoc
                  y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                  cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                  cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                  sql="SELECT StudentName FROM student WHERE StudentId=?"
                  adr=(name, )
                  mark_attendance(path_to_file,name)
                  my_cursor.execute(sql,adr)
                  data=my_cursor.fetchall()   
                  # print(data[0])
                  naam=str(data)[3:-4]
                  temp=format(only_face(cap))
                  # print(naam)
                  cv2.putText(img,naam,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                  cv2.putText(img,"{} C".format(temp),(x1+20,y1),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                  
                  post="-"+str_current_datetime
                  dtString=now.strftime("%H:%M:%S")
                  display=dtString+"  "+str_current_datetime
                  cv2.putText(img, display, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                  img_n="{}.jpeg".format(naam+post)
                  cv2.imwrite(os.path.join(another_path,img_n),img)
                  
              else:
                  name = "Unknown"
                  print(name)
                  y1,x2,y2,x1 = faceLoc
                  y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                  cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                  cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                  cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                  temp=format(only_face(cap))
                  cv2.putText(img,"{} C".format(temp),(x1+20,y1),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                  dtString=now.strftime("%H:%M:%S")
                  display=dtString+"  "+str_current_datetime
                  cv2.putText(img, display, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                  post="-"+str_current_datetime
                  img_n="{}.jpeg".format(name+post)
                  cv2.imwrite(os.path.join(unknown_path,img_n),img)
                  #============================================
                  gender, age=demography.func(cap)
                  # print(gender, age)
                  str_age=gender+" "+age
                  # print(str_age)
                  cv2.putText(img, str_age, (x1, y1-25), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


          cv2.imshow('Webcam', img)
          if(cv2.waitKey(1)%256==27):
            conn.commit()
            conn.close()
            cap.release()
            cv2.destroyAllWindows()
            break

def mark_attendance(path_to_file, student_id):
  conn=sqlite3.connect('SQL Database/SIH.db')
  my_cursor = conn.cursor()
  sql="SELECT StudentName, Course, Department  FROM student WHERE StudentId=?"
  adr=(student_id, )
  my_cursor.execute(sql,adr)
  data=my_cursor.fetchall()
  if(len(data)>0):
    n=data[0][0]
    c=data[0][1]
    d=data[0][2]
  else:
    return
  with open(path_to_file, "r+", newline="\n") as f:
    myDataList=f.readlines()
    name_list=[]
    for line in myDataList:
      entry=line.split((","))
      name_list.append(entry[0])
    if((student_id not in name_list) and (n not in name_list) and (c not in name_list) and (d not in name_list)):
      now=datetime.now()
      d1=now.strftime("%d/%m/%Y")
      dtString=now.strftime("%H:%M:%S")
      f.writelines(f"\n{student_id},{n},{c},{d},{dtString},{d1},Present")

if __name__ == "__main__":
  face_recog()