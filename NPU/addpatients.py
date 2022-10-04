# -*- coding: utf-8 -*-
import csv
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from window import Window
from patients import Patients_main, Patients_test


class AddPat(Window): 
    '''добавление пациентов работает пока только с клавиатуры'''

    def open_w(self):

        self.grid.addWidget(self.btn_exit, 1, 7)
        
        fio_patient = QLabel('ФИО', self) 
        self.grid.addWidget(fio_patient, 1, 0, 1, 4) 

        self.fio = QLineEdit()
        self.grid.addWidget(self.fio, 1, 2, 1, 5)

        age_patient = QLabel('Возраст', self) 
        self.grid.addWidget(age_patient, 2, 0, 1, 3)

        self.age = QLineEdit()
        self.grid.addWidget(self.age, 2, 2, 1, 5)

        btn_save = QPushButton('Сохранить', self)
        btn_save.setFixedSize(150, 30)
        self.grid.addWidget(btn_save, 10, 0, 1, 4)
        btn_save.clicked.connect(self.save_pat)


        btn_back = QPushButton('Назад', self)
        btn_back.setFixedSize(150, 30)
        self.grid.addWidget(btn_back, 10, 4, 1, 4)
        btn_back.clicked.connect(self, NPU())


        names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', '0', '1',
                 'Ж', 'З', 'И', 'Й', 'К', 'Л', '2', '3',
                 'М', 'Н', 'О', 'П', 'Р', 'С', '4', '5',
                 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', '6', '7',
                 'Ш', 'Щ', 'ъ', 'ы', 'ь', 'Э', '8', '9',
                 'Ю', 'Я', '', '', '', '', '-', '<-']

        positions = [(i,j) for i in range(4,10) for j in range(8)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name, self)
            button.setFixedSize(25, 25)
            self.grid.addWidget(button, *position)


    def save_pat(self):
        self.patient = [str(self.load_data()), str(self.fio.text()), str(self.age.text())]
        self.write_csv()
        self.a()
    

    def load_data(self): 
        with open("doc/patients.csv", encoding='utf-8') as tableAB:
            table = csv.reader(tableAB)
            data = list(table)
        return len(data)+1

    
    def write_csv(self): 
        with open('doc/patients.csv', "a", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.patient)


class AddPat_main(AddPat):

    def a(self):
        self.transit(self, Patients_main()) 
    # def back_main_window(self):
    #     self.close()
    #     self.back = Patients_main()
    #     self.back.show()


    # def save_back(self):
    #     self.close()
    #     self.back = Patients_main()
    #     self.back.show()
    # def save_back(self):
    #     Back.back_to_patient()


class AddPat_test(AddPat):

    def a(self):
        self.transit(self, Patients_test()) 
    
    # def back_main_window(self):
    #     self.close()
    #     self.back = Patients_test()
    #     self.back.show()


    # def save_back(self):
    #     self.close()
    #     self.back = Patients_test()
    #     self.back.show()
    # def save_back(self):
    #     Back.back_to_patient_test()