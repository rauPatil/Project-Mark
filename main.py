
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtGui import QMovie
import sys
from unittest import result
import requests
import os
from datetime import datetime
import os
import random
import pyttsx3 

time.sleep(10)
print("Initializing")
time.sleep(10)
print("Loading current directory..")
time.sleep(10)
print("Importing preferences and setting up virtual environment..")
time.sleep(10)
print("Virtual environment setup complete..")
time.sleep(10)
print("Getting online..")
time.sleep(10)
print("Connecting to servers..")
time.sleep(10)
print("Collecting data..")
time.sleep(10)
print("Necessary data collected..")

location = input("Enter Location: ")
time.sleep(3)
target_height = int(input("Enter Target Height: "))
time.sleep(3)
proj_vel = int(input("Enter projectile velocity: "))

print("Configuring system..")
time.sleep(10)
print("Completed..")

time.sleep(10)
print("Setting system preferences..")


time.sleep(10)
print("All checkes completed, system is online and ready..")
time.sleep(10)

# print("system is online and ready")
# time.sleep(2)

print("mark m1, ready to engage! ")
time.sleep(5)

user_api = "6e8aa28bcb02bde3f4126cc02fbb5c9e"
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invaild City {}, Please Check Your City Name".format(location))
else:
    city_temp = round(((api_data['main']['temp']) - 273.15),2)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    

city_temp=str(city_temp)
weather_desc = str(weather_desc)
hmdt= str(hmdt)
wind_spd = str(wind_spd)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.intergration_label = QtWidgets.QLabel(self.centralwidget)
        self.intergration_label.setGeometry(QtCore.QRect(20, 30, 311, 51))
        self.intergration_label.setStyleSheet("font: 12pt \"JetBrains Mono\";\n"
"color: rgb(255,255,255);")
        self.intergration_label.setObjectName("intergration_label")
        self.horiz_label_right = QtWidgets.QLabel(self.centralwidget)
        self.horiz_label_right.setGeometry(QtCore.QRect(1750, 510, 201, 61))
        self.horiz_label_right.setStyleSheet("font: 25 72pt \"JetBrains Mono NL Light\";")
        self.horiz_label_right.setFrameShape(QtWidgets.QFrame.Panel)
        self.horiz_label_right.setText("")
        self.horiz_label_right.setPixmap(QtGui.QPixmap("Images/linepng.png"))
        self.horiz_label_right.setScaledContents(True)
        self.horiz_label_right.setObjectName("horiz_label_right")
        self.hundredyard_label = QtWidgets.QLabel(self.centralwidget)
        self.hundredyard_label.setGeometry(QtCore.QRect(50, 815, 261, 41))
        self.hundredyard_label.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.hundredyard_label.setObjectName("hundredyard_label")
        self.horiz_label_left = QtWidgets.QLabel(self.centralwidget)
        self.horiz_label_left.setGeometry(QtCore.QRect(-40, 510, 201, 61))
        self.horiz_label_left.setFrameShape(QtWidgets.QFrame.Panel)
        self.horiz_label_left.setText("")
        self.horiz_label_left.setPixmap(QtGui.QPixmap("Images/linepng.png"))
        self.horiz_label_left.setScaledContents(True)
        self.horiz_label_left.setObjectName("horiz_label_left")
        self.velocity_label = QtWidgets.QLabel(self.centralwidget)
        self.velocity_label.setGeometry(QtCore.QRect(50, 725, 241, 41))
        self.velocity_label.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.velocity_label.setObjectName("velocity_label")
        self.los_label = QtWidgets.QLabel(self.centralwidget)
        self.los_label.setGeometry(QtCore.QRect(50, 770, 141, 41))
        self.los_label.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.los_label.setObjectName("los_label")
        self.height_label = QtWidgets.QLabel(self.centralwidget)
        self.height_label.setGeometry(QtCore.QRect(50, 680, 241, 41))
        self.height_label.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.height_label.setObjectName("height_label")
        self.mildotnum_label = QtWidgets.QLabel(self.centralwidget)
        self.mildotnum_label.setGeometry(QtCore.QRect(1400, 680, 201, 41))
        self.mildotnum_label.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255,255,255);")
        self.mildotnum_label.setObjectName("mildotnum_label")
        self.square_lable_left = QtWidgets.QLabel(self.centralwidget)
        self.square_lable_left.setGeometry(QtCore.QRect(445, 299, 111, 311))
        self.square_lable_left.setStyleSheet("font: 0 28pt \"JetBrains Mono NL Thin\";\n"
"color: rgb(85, 170, 255);\n"
"font: 0 72pt \"JetBrains Mono Thin\";")
        self.square_lable_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.square_lable_left.setObjectName("square_lable_left")
        self.square_label_right = QtWidgets.QLabel(self.centralwidget)
        self.square_label_right.setGeometry(QtCore.QRect(1380, 299, 111, 311))
        self.square_label_right.setStyleSheet("font: 0 28pt \"JetBrains Mono NL Thin\";\n"
"color: rgb(85, 170, 255);\n"
"font: 0 72pt \"JetBrains Mono Thin\";")
        self.square_label_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.square_label_right.setObjectName("square_label_right")
        self.center_label = QtWidgets.QLabel(self.centralwidget)
        self.center_label.setGeometry(QtCore.QRect(519, 405, 871, 121))
        self.center_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.center_label.setText("")
        self.center_label.setPixmap(QtGui.QPixmap("Images/r3.png"))
        self.center_label.setScaledContents(True)
        self.center_label.setObjectName("center_label")
        self.neg_label = QtWidgets.QLabel(self.centralwidget)
        self.neg_label.setGeometry(QtCore.QRect(295, 30, 135, 60))
        self.neg_label.setText("")
        self.neg_label.setPixmap(QtGui.QPixmap("Images/-ve3.gif"))
        self.neg_label.setScaledContents(True)
        self.neg_label.setObjectName("neg_label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1525, 685, 113, 31))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.cal_moa())
        self.pushButton.setGeometry(QtCore.QRect(1650, 685, 61, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(74, 74, 74);")
        self.pushButton.setObjectName("pushButton")
        self.height_labelR = QtWidgets.QLabel(self.centralwidget)
        self.height_labelR.setGeometry(QtCore.QRect(390, 690, 241, 21))
        self.height_labelR.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.height_labelR.setObjectName("height_labelR")
        self.velocity_labelR = QtWidgets.QLabel(self.centralwidget)
        self.velocity_labelR.setGeometry(QtCore.QRect(390, 735, 241, 21))
        self.velocity_labelR.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.velocity_labelR.setObjectName("velocity_labelR")
        self.los_labelR = QtWidgets.QLabel(self.centralwidget)
        self.los_labelR.setGeometry(QtCore.QRect(390, 782, 241, 21))
        self.los_labelR.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.los_labelR.setObjectName("los_labelR")
        self.hundredyard_labelR = QtWidgets.QLabel(self.centralwidget)
        self.hundredyard_labelR.setGeometry(QtCore.QRect(390, 825, 245, 25))
        self.hundredyard_labelR.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.hundredyard_labelR.setObjectName("hundredyard_labelR")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1170, 360, 201, 41))
        self.label.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1190, 390, 221, 41))
        self.label_2.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.weatherTitle_label = QtWidgets.QLabel(self.centralwidget)
        self.weatherTitle_label.setGeometry(QtCore.QRect(1350, 0, 321, 61))
        self.weatherTitle_label.setStyleSheet("font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.weatherTitle_label.setObjectName("weatherTitle_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1685, 20, 211, 21))
        self.label_3.setStyleSheet("font: 14.5pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1350, 60, 241, 31))
        self.label_4.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1350, 100, 250, 31))
        self.label_5.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1350, 140, 201, 31))
        self.label_6.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1350, 180, 215, 31))
        self.label_7.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1660, 60, 241, 31))
        self.label_8.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1660, 100, 241, 31))
        self.label_9.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1660, 140, 241, 31))
        self.label_10.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1660, 180, 241, 31))
        self.label_11.setStyleSheet("font: 10pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1210, -10, 141, 111))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Images/gif3.gif"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(735, 30, 441, 271))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Images/gif4.gif"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 540, 111, 31))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Tahoma\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(610, 670, 681, 181))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Images/gi2.gif"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(560, 370, 400, 41))
        self.label_16.setStyleSheet("font: 9pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(560, 400, 400, 41))
        self.label_17.setStyleSheet("font: 9pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cal_moa(self):
       height_mil = self.lineEdit.text()
       int_height_mil = int(height_mil)

       dis_meter = (target_height * 10)/int_height_mil
       dis_yards = dis_meter * 1.0936

       r_meter = round(dis_meter,1)
       r_yard = round(dis_yards,1)
       print(r_yard)

       travel_time = r_yard/proj_vel
       drop = (9.8/2) * travel_time*travel_time
       drop_in = drop * 12
       r_drop = round(drop_in, 1)

       one_min = dis_yards/100
       MOA = drop_in/one_min
       r_moa = round(MOA,-1)




#        time.sleep(2)
       self.label_16.setText("Target is at a distance of " + str(r_yard) + " yards")
       
       self.label_17.setText("Travel time for projectitle " + str(round(travel_time,0)) + "sec")
       
       self.label.setText(str(r_moa) + " Mil Up")
       
#        

       
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.intergration_label.setText(_translate("MainWindow", "System Intergration > "))
        self.hundredyard_label.setText(_translate("MainWindow", "Drop at Hundred Yard :"))
        self.velocity_label.setText(_translate("MainWindow", "Projectile Velocity :"))
        self.los_label.setText(_translate("MainWindow", "LOS :"))
        self.height_label.setText(_translate("MainWindow", "Target Height :"))
        self.mildotnum_label.setText(_translate("MainWindow", "MIL DOTs : "))
        self.square_lable_left.setText(_translate("MainWindow", "]"))
        self.square_label_right.setText(_translate("MainWindow", "["))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.height_labelR.setText(_translate("MainWindow", str(target_height) +" CM"))
        self.velocity_labelR.setText(_translate("MainWindow", str(proj_vel)+ " m/s"))
        self.los_labelR.setText(_translate("MainWindow", "0 Degree"))
        self.hundredyard_labelR.setText(_translate("MainWindow", "NA"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.weatherTitle_label.setText(_translate("MainWindow", "Weather Stats for : "))
        self.label_3.setText(_translate("MainWindow", (location.upper())))
        self.label_4.setText(_translate("MainWindow", "Current Temperature is :"))
        self.label_5.setText(_translate("MainWindow", "Current Weather desc :"))
        self.label_6.setText(_translate("MainWindow", "Current Humidity :"))
        self.label_7.setText(_translate("MainWindow", "Current Wind Speed :"))
        self.label_8.setText(_translate("MainWindow", city_temp+" deg C"))
        self.label_9.setText(_translate("MainWindow", weather_desc))
        self.label_10.setText(_translate("MainWindow", hmdt+"%"))
        self.label_11.setText(_translate("MainWindow", wind_spd+" km/hr"))
        self.label_14.setText(_translate("MainWindow", "Horizon lock"))
        self.label_16.setText(_translate("MainWindow", ""))
        self.label_17.setText(_translate("MainWindow", ""))

        self.mlabel12 = QMovie("Images\gif3.gif")
        self.label_12.setMovie(self.mlabel12)
        self.mlabel12.start()
        
        self.mlabel15 =QMovie("Images\gi2.gif")
        self.label_15.setMovie(self.mlabel15)
        self.mlabel15.start()

        self.mlabel13 =QMovie("Images\gif4.gif")
        self.label_13.setMovie(self.mlabel13)
        self.mlabel13.start()

        self.mneglabel =QMovie("Images\-ve3.gif")
        self.neg_label.setMovie(self.mneglabel)
        self.mneglabel.start()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
