from cgitb import text
import cv2
import numpy as np
import face_recognition
from numpy import genfromtxt
import os
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

def train_classifier():
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

      def findEncodings(images):
        encodeList = []
        for img in images:
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          encode = face_recognition.face_encodings(img)[0]
          encodeList.append(encode)
        return encodeList

      encodeListKnown = findEncodings(images)
      # print(encodeListKnown)

      np.savetxt("Files/Encodings.csv", 
                encodeListKnown,
                delimiter =", ", 
                fmt ='% s')

      print('Encoding complete')
      messagebox.showinfo("Result", "Training Datasets Completed")