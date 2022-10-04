# -*- coding: utf-8 -*-
import sys
import csv
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QListWidget, QLabel, QLCDNumber, QSlider, QLineEdit, QCalendarWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from window import Window
#from battery_check import Battery
from check import Check


class NPU(Window):    
    '''главный класс, запускающий программу, отрисовывает главное меню приложения'''

    def open_w(self):

        btn_patients = QPushButton('Пациенты', self)
        self.grid.addWidget(btn_patients, 1, 0)
        btn_patients.clicked.connect(self.transit(Patients_main()))

        btn_scripts = QPushButton('Сценарии', self)
        self.grid.addWidget(btn_scripts, 1, 1)
        btn_scripts.clicked.connect(self.transit(Script_main()))

        btn_conclusions = QPushButton('Заключения', self)
        self.grid.addWidget(btn_conclusions, 1, 2)
        # btn_add_and_settings.clicked.connect(self.transit(Script_main()))

        btn_start = QPushButton('Начать тест', self)
        self.grid.addWidget(btn_start, 3, 1)
        btn_start.clicked.connect(self.transit(StartTest()))

        btn_sensitive_test = QPushButton('Чувствительность', self)
        self.grid.addWidget(btn_sensitive_test, 4, 1)
        btn_sensitive_test.clicked.connect(self.transit(Sens_main()))

        #self.battery = Battery()
        #self.bat = QLabel(self.battery.check())
        #self.grid.addWidget(self.bat, 4, 2)


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


class AddPat_test(AddPat):

    def a(self):
        self.transit(self, Patients_test()) 

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
        btn_back.clicked.connect(self.transit(self, NPU()))

        del_patient = QLabel('Нажмите на пациента для удаления', self) 
        self.grid.addWidget(del_patient, 6, 0, 1, 4)
        self.patients_list.itemClicked.connect(self.item_change)

    
    def add(self):
        self.transit(self, AddPat_main())



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
            self.transition(self, Sens_test())
    

    def global_patient(self):
        return self.patient_global
        

    def add(self):
        self.transit(self, AddPat_test())


class Script(Window): 
    '''Выбор сценария теста'''

    def open_w(self):

        btn_add = QPushButton('Добавить', self)
        self.grid.addWidget(btn_add, 1, 0)
        btn_add.clicked.connect(self.add)

        self.scr_list = QListWidget()
        self.grid.addWidget(self.scr_list, 2, 0, 1, 5)
        self.scr_list.addItems(self.load_data())

        self.s()


    def load_data(self): 
        with open("doc/scripts.csv", encoding='utf-8') as scr:
            table = csv.reader(scr, delimiter = ",")
            self.rows = [', '.join(row) for row in table]
        return self.rows


    def add(self):
        pass


    def delete_scr(self, item):
        inputt = open('doc/scripts.csv', 'r', encoding='utf-8')
        rows = []
        i = item.text().split(', ')
        for row in csv.reader(inputt):
            if row != i:
                rows += [row]             
        inputt.close()

        outputt = open('doc/scripts.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(outputt)
        writer.writerows(rows)
        outputt.close()


class Script_main(Script):

    def s(self):

        btn_back = QPushButton('Назад', self)
        self.grid.addWidget(btn_back, 1, 1)
        btn_back.clicked.connect(self.transition(self, NPU()))

        del_script = QLabel('Нажмите на сценарий для удаления', self) 
        self.grid.addWidget(del_script, 6, 0, 1, 4)
        self.scr_list.itemClicked.connect(self.item_change)


    def item_change(self):
        change = QMessageBox()
        change.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        change.setText("Удалить сценарий?")
        change.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret = change.exec()
        if ret == QMessageBox.Ok:
            self.delete_scr()


class Script_test(Script):

    def s(self):

        choose_script = QLabel('Нажмите на выбранный сценарий', self) 
        self.grid.addWidget(choose_script, 6, 0, 1, 4)
        self.scr_list.itemClicked.connect(self.item_choose)


    def item_choose(self, item):
        choose = QMessageBox()
        choose.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        choose.setText(item.text())
        choose.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret = choose.exec()
        if ret == QMessageBox.Ok:
            self.script_global = item.text()
            self.transit(self, Check())


    def global_script(self):
        return self.script_global


class SensTest(Window): 
    '''определение чувствительности к электростимуляции'''

    def open_w(self):

        amplitude = QLabel('Амплитуда тока', self) 
        self.grid.addWidget(amplitude, 2, 0, 1, 1)

        self.slider_amp = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_amp, 3, 0, 1, 2)

        lcd = QLCDNumber(self)
        self.grid.addWidget(lcd, 2, 3, 2, 1)
        self.slider_amp.valueChanged.connect(lcd.display)

        time = QLabel('Время, мс', self) 
        self.grid.addWidget(time, 4, 0, 1, 1)

        self.slider_time = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_time, 5, 0, 1, 2)


        lcd_time = QLCDNumber(self)
        self.grid.addWidget(lcd_time, 4, 3, 2, 1)
        self.slider_time.valueChanged.connect(lcd_time.display)


        btn_test_amp = QPushButton('Тест', self)
        self.grid.addWidget(btn_test_amp, 6, 0)
        # btn_test_amp.clicked.connect(self.test_amp)

        self.sens()


class Sens_main(SensTest):

    def sens(self):

        btn_ok = QPushButton('Назад', self)
        self.grid.addWidget(btn_ok, 6, 1)
        btn_ok.clicked.connect(self.transit(self, NPU()))


class Sens_test(SensTest):

    def sens(self):

        btn_save = QPushButton('OK', self)
        self.grid.addWidget(btn_save, 6, 1)
        btn_save.clicked.connect(self.show_amp)


    def show_amp(self):
        show_amp = QMessageBox()
        show_amp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        show_amp.setText(str(self.slider_amp.value()) + ' мА, ' + str(self.slider_time.value()) + ' мс')
        show_amp.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = show_amp.exec()
        if ret == QMessageBox.Yes:
            self.sensitive_global = str(self.slider_amp.value()) + ' мА, ' + str(self.slider_time.value()) + ' мс'
            self.transit(self, Script_test())


    def global_sensetive(self):
        return self.sensitive_global



class StartTest(Window):

    def open_w(self):

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.setFont(QFont('Sans Serif', 5))
        cal.clicked[QtCore.QDate].connect(self.showDate)
        self.grid.addWidget(cal, 2, 0, 6, 5)


    def showDate(self, date):
        showDate = QMessageBox()
        showDate.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        showDate.setText(date.toString()+', верно?')
        showDate.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = showDate.exec()
        if ret == QMessageBox.Yes:
            self.date_global = date.toString()
            self.transit(self, Patients_test())


    def global_date(self):
        return self.date_global


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NPU()
    sys.exit(app.exec_()) 