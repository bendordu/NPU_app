# -*- coding: utf-8 -*-
import csv
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtCore, QtTest
from PyQt5.QtMultimedia import QSound
from window import Window
# from test_start import Start_test
# from detect import Detect
# from patients import Patients_test
# from start_test import StartTest


class Nine_starl_prob(Window):

    def open_w(self):

        self.grid.addWidget(self.btn_exit, 1, 10)

        btn_stop = QPushButton('Стоп', self)
        # btn_stop.clicked.connect(self.stop)
        self.grid.addWidget(btn_stop, 1, 0)

        self.number = QLabel('1', self) 
        self.grid.addWidget(self.number, 3, 1)

        self.sound = QSound("stimuls/whitenoise.wav")
        self.timer = QtCore.QTimer()

        self.thread = QtCore.QThread()
        self.detect = Detect()
        self.detect.moveToThread(self.thread)
        self.thread.started.connect(self.start)
        self.thread.started.connect(self.detect.run)
        self.thread.start()

                
    @QtCore.pyqtSlot()
    def start(self):     
        
        for i in range(9):
            self.sound.play()
            self.timer.start(40)
            self.timer.timeout.connect(self.sound.stop)
            self.number = QLabel(str(i+1), self) 
            self.grid.addWidget(self.number, 3, i+1)
            QtTest.QTest.qWait(1000)   

        self.thread.quit()
        self.write_csv()

    
    # def write_csv(self): 
        
    #     path = "doc/results/" + str(date_global) + '-' + str(patient_global) + ".csv"
    #     with open(path, "w", newline='', encoding='utf-8') as csv_file:
    #         writer = csv.writer(csv_file)
    #         writer.writerow([str(date_global), str(patient_global)])
    #         writer.writerow(['EMG', 'GSR(Om)', 'HR'])
    #         writer.writerows(list(zip(emg_data, gsr_data)))
    #         print('hi')
                       
    #         # self.next_step()
    
    
    def write_csv(self): 
        
        path = "doc/results/" + str(StartTest.global_date) + '-' + str(Patients_test.global_patient) + ".csv"
        with open(path, "w", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([str(StartTest.global_date), str(Patients_test.global_patient)])
            writer.writerow(['EMG', 'GSR(Om)', 'HR'])
            writer.writerows(list(zip(emg_data, gsr_data)))
            print('hi')


    def next_step(self):
        self.close()
        self.pat = Start_test()
        self.pat.show() 