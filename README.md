# SIH-2022-AK1146
DETECTING COVID-19 SUSPECTS using THERMAL SCREENING at ENTRANCES along with
their ATTENDANCE.

• Using the CCTV feeds faces of persons entering will be recognized. For Face Detection and Recognition, We have used
dlib’s state-of-art face recognition built using Deep Learning which has an accuracy of 99.38 percent on the Labeled
Faces in the Wild benchmark.

• The persons will then be checked whether they are wearing mask or not. For mask Detection, First we are capturing the
facial data with and without mask and storing them into two Numpy files. Then we’re reducing the dimensions of the
files using PCA. We have used SVM classification to detect mask. We have used 75 percent data for training the model
and rest 25 percent for testing and got an accuracy score of 95 percent.

• The CCTV IR feeds are processed and converted into heat-map image. Then we are eroding and dilating the
heat-map image to enhance the image. Further we’re finding the contour points of the image and comparing with the
threshold temperature provided.

• The Recognized faces along with their attendance and body temperature is stored on a DataBase on a local server. The
database is created using SQLite3 and all the CRUD operations (Create-Read-Update-Delete) have been properly
managed.

• If any unknown person come across the CCTV their Demographic Data (Age range, Gender) will be stored on the
database along with the timestamp and date. We have used some pre-trained data and DNN algorithm to detect the
demographic data.


## Steps to run the application:

1. Install the dependencies using the command `pip install requirements.txt` in the terminal.
   Note: You might face some difficulties installing a few libraries like d-lib and face-recognition. Take help from stack-overflow or any other resources available.
2. Run the main file by using the Run command or by using the command `python run main.py` in the terminal.
3. The Homepage of the Application will appear where you can see different options as shown below.

![image](https://github.com/tauquirahmed/SIH-2022-PS-Code-AK1146/assets/100079429/84efbe0d-9ba5-4d30-8825-d709111597d1)

## Students Database
![image](https://github.com/tauquirahmed/SIH-2022-PS-Code-AK1146/assets/100079429/38485627-e466-4b57-b4d7-df81ff49ff18)

## Face Recognition
![image](https://github.com/tauquirahmed/SIH-2022-PS-Code-AK1146/assets/100079429/335101be-ec68-4b6d-97f7-5bd483ab2c46)

## Mask Detection
![image](https://github.com/tauquirahmed/SIH-2022-PS-Code-AK1146/assets/100079429/4ccdaa9d-5a26-4e1b-a179-ffdc402463c1)

## Temperature Detection
![image](https://github.com/tauquirahmed/SIH-2022-PS-Code-AK1146/assets/100079429/ebc03b1b-e480-481d-bacd-4a25b49878d1)

## Final Result
![image](https://github.com/tauquirahmed/SIH-2022-PS-Code-AK1146/assets/100079429/4cb37e07-3266-4884-81ad-c08d93917922)



