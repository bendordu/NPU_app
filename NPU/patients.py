# -*- coding: utf-8 -*-
import csv
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QListWidget
from PyQt5 import QtCore
from window import Window
from addpatients import AddPat_main, AddPat_test
from sensitive import Sens_test


class Patients(Window): 
    '''Просмотр пациентов'''

    def open_w(self):
        
        btn_add = QPushButton('Добавить', self)
        self.grid.addWidget(btn_add, 1, 0)

        btn_add.clicked.connect(self.add)


        self.patients_list = QListWidget()
        self.grid.addWidget(self.patients_list, 2, 0, 1, 5)

        self.patients_list.addItems(self.load_data())

        self.pat()


    def item_change(self, item):
        change = QMessageBox()
        change.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        change.setText("Удалить пациента?")
        change.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret = change.exec()
        if ret == QMessageBox.Ok:
            self.pat_del(item)        


    def pat_del(self, item):
        input_ = open('doc/patients.csv', 'r', encoding='utf-8')
        rows = []
        i = item.text().split(', ')
        for row in csv.reader(input_):
            if row != i:
                rows += [row]             
        input_.close()

        output_ = open('doc/patients.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(output_)
        writer.writerows(rows)
        output_.close()

    
    def load_data(self): 
        with open("doc/patients.csv", encoding='utf-8') as patients:
            table = csv.reader(patients, delimiter = ",")
            self.rows = [', '.join(row) for row in table]
        return self.rows


class Patients_main(Patients): #переход с главной страницы

    def pat(self):

        btn_back = QPushButton('Назад', self)
        self.grid.addWidget(btn_back, 1, 1)
    
        btn_back.clicked.connect(self.back_main_window(self, NPU()))

        del_patient = QLabel('Нажмите на пациента для удаления', self) 
        self.grid.addWidget(del_patient, 6, 0, 1, 4)

        self.patients_list.itemClicked.connect(self.item_change)

    
    def add(self):
        self.transit(self, AddPat_main())


    # def back_main_window(self):
    #     self.close()
    #     self.back = NPU()
    #     self.back.show()
    # def back_main_window(self):
    #     Back.back_main_window(self)


    # def add(self):
    #     self.close()
    #     self.add_pat = AddPat_main()
    #     self.add_pat.show()


class Patients_test(Patients): #окно уже в самом тесте

    def pat(self):

        choose_patient = QLabel('Нажмите на выбранного пациента', self) 
        self.grid.addWidget(choose_patient, 6, 0, 1, 4)

        self.patients_list.itemClicked.connect(self.show_pat)


    def show_pat(self, item):
        show_pat = QMessageBox()
        show_pat.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        show_pat.setText(item.text())
        show_pat.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = show_pat.exec()
        if ret == QMessageBox.Yes:
            self.patient_global = item.text()
            # self.next_to_sens()
            self.transition(self, Sens_test())
    

    def global_patient(self):
        return self.patient_global


    # def next_to_sens(self):
    #     self.close()
    #     self.sens_t = Sens_test()
    #     self.sens_t.show()


    # def back_main_window(self):
    #     self.close()
    #     self.back = NPU()
    #     self.back.show()
    # def back_main_window(self):
    #     Back.back_main_window(self)
        

    def add(self):
        self.transit(self, AddPat_test())