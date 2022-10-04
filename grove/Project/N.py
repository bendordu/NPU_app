# -*- coding: utf-8 -*-
import sys
import csv
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QHBoxLayout, QPushButton, QMessageBox, QCalendarWidget, QToolTip, QGridLayout, QListWidget, QLCDNumber, QTextEdit, QLineEdit, QComboBox, QTableWidget, QSlider
from PyQt5 import Qt, QtCore, QtTest
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtMultimedia import QSound


class Window(QWidget):

    def __init__(self):
        super().__init__() 

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(480, 320)

        self.grid = QGridLayout()
        self.grid.setSpacing(5)      
        self.setLayout(self.grid)

        self.btn_exit = QPushButton('×', self)
        self.btn_exit.setFixedSize(40, 40)
        self.btn_exit.setStyleSheet('background-color: #B52323; color: white')
        self.grid.addWidget(self.btn_exit, 1, 4)
        self.btn_exit.clicked.connect(self.exit_app)
        self.show() 
        self.open_w()


    def exit_app(self):
        sys.exit() 


class Check(Window):

    def open_w(self):

        date = QLabel(date_global, self) 
        self.grid.addWidget(date, 1, 0)

        patient = QLabel(patient_global, self) 
        self.grid.addWidget(patient, 2, 0)

        sens = QLabel(sensitive_global, self) 
        self.grid.addWidget(sens, 3, 0)

        scr = QLabel(script_global, self) 
        self.grid.addWidget(scr, 4, 0)

        btn_start = QPushButton('Начать тест', self)
        btn_start.clicked.connect(self.start)
        self.grid.addWidget(btn_start, 5, 0)


    def start(self):
        self.close()
        self.pat = Nine_starl_prob()
        self.pat.show()  


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

        self.start()


    def start(self):
        for i in range(9):
            self.sound.play()
            self.timer.start(40)
            self.timer.timeout.connect(self.sound.stop)
            self.number = QLabel(str(i+1), self) 
            self.grid.addWidget(self.number, 3, i+1)
            QtTest.QTest.qWait(1000)

        self.close()
        self.pat = Start_test()
        self.pat.show()  


class Start_test(Window):

    def open_w(self):

        btn_stop = QPushButton('Стоп', self)
        # btn_stop.clicked.connect(self.stop)
        self.grid.addWidget(btn_stop, 1, 0)

        self.number = QLabel('Test', self) 
        self.grid.addWidget(self.number, 3, 1)

        self.sound = QSound("stimuls/whitenoise.wav")
        self.timer = QtCore.QTimer()
        self.condition_seq = ['P', 'N', 'U', 'N', 'U', 'N', 'P']   #, 'U', 'N', 'P', 'N', 'P', 'N', 'U']

        self.green = QPixmap("stimuls/green_circle.png")
        self.red = QPixmap("stimuls/red_square.jpg")
        self.blue = QPixmap("stimuls/blue_triangle.png")

        self.box = QLabel(self)
        # self.box.setPixmap(self.box)
        self.box.setGeometry(120, 80, 200, 200)
        self.box.show()

        self.timer_color = QtCore.QTimer()
        self.timer_color.timeout.connect(self.box.hide)

        self.start()


    def start(self):

        for i in range(4):

            self.sound.play()
            self.timer.start(40)
            self.timer.timeout.connect(self.sound.stop)
            QtTest.QTest.qWait(1000)

        for i in self.condition_seq:

            self.number.hide()
            self.number = QLabel(str(i), self) 
            self.grid.addWidget(self.number, 3, 1)

            if i == 'P':

                for j in range(7)[1:7]:

                    if j//2 == 1:
                        self.timer_color.start(8000)
                        self.box.setPixmap(self.red)
                        self.box.show()

                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)

                self.number.hide()

                # if i == self.condition_seq[6]:
                #     QtTest.QTest.qWait(300000)


            elif i == 'N':

                for j in range(7)[1:7]:

                    if j//2 == 1:
                        self.timer_color.start(8000)
                        self.box.setPixmap(self.green)
                        self.box.show()

                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)

                self.number.hide()


            elif i == 'U':

                for j in range(7)[1:7]:

                    if j//2 == 1:
                        self.timer_color.start(8000)
                        self.box.setPixmap(self.blue)
                        self.box.show()

                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)

                self.number.hide()

                # if i == self.condition_seq[14]:
                #     pass  


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
            global date_global
            date_global = date.toString()
            self.next_to_patient()
        

    def next_to_patient(self):
        self.close()
        self.pat = Patients_test()
        self.pat.show()    


class Script(Window):

    def open_w(self):

        btn_add = QPushButton('Добавить', self)
        btn_add.clicked.connect(self.add)
        self.grid.addWidget(btn_add, 1, 0)

        self.scr_list = QListWidget()
        self.scr_list.addItems(self.load_data())
        self.grid.addWidget(self.scr_list, 2, 0, 1, 5)

        self.s()


    def load_data(self): 
        with open("doc/scripts.csv", encoding='utf-8') as scr:
            table = csv.reader(scr, delimiter = ",")
            self.rows = [', '.join(row) for row in table]
        return self.rows


    def add(self):
        pass


    def delete_scr(self):
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
        btn_back.clicked.connect(self.back_main_window)
        self.grid.addWidget(btn_back, 1, 1)

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


    def back_main_window(self):
        self.close()
        self.back = NPU()
        self.back.show()


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
            global script_global
            script_global = item.text()
            self.next_to_check()

    
    def next_to_check(self):
        self.close()
        self.check = Check()
        self.check.show()


class Patients(Window):

    def open_w(self):
        
        btn_add = QPushButton('Добавить', self)
        btn_add.clicked.connect(self.add)
        self.grid.addWidget(btn_add, 1, 0)

        self.patients_list = QListWidget()
        self.patients_list.addItems(self.load_data())
        self.grid.addWidget(self.patients_list, 2, 0, 1, 5)

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
        inputt = open('doc/patients.csv', 'r', encoding='utf-8')
        rows = []
        i = item.text().split(', ')
        for row in csv.reader(inputt):
            if row != i:
                rows += [row]             
        inputt.close()

        outputt = open('doc/patients.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(outputt)
        writer.writerows(rows)
        outputt.close()

    
    def load_data(self): 
        with open("doc/patients.csv", encoding='utf-8') as patients:
            table = csv.reader(patients, delimiter = ",")
            self.rows = [', '.join(row) for row in table]
        return self.rows


class Patients_main(Patients):

    def pat(self):

        btn_back = QPushButton('Назад', self)
        btn_back.clicked.connect(self.back_main_window)
        self.grid.addWidget(btn_back, 1, 1)

        del_patient = QLabel('Нажмите на пациента для удаления', self) 
        self.grid.addWidget(del_patient, 6, 0, 1, 4)

        self.patients_list.itemClicked.connect(self.item_change)


    def back_main_window(self):
        self.close()
        self.back = NPU()
        self.back.show()


    def add(self):
        self.close()
        self.add_pat = AddPat_main()
        self.add_pat.show()


class Patients_test(Patients):

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
            global patient_global
            patient_global = item.text()
            self.next_to_sens()


    def next_to_sens(self):
        self.close()
        self.sens_t = Sens_test()
        self.sens_t.show()


    def back_main_window(self):
        self.close()
        self.back = NPU()
        self.back.show()


    def add(self):
        self.close()
        self.add_pat = AddPat_test()
        self.add_pat.show()


class AddPat(Window):

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
        btn_save.clicked.connect(self.save_pat)
        self.grid.addWidget(btn_save, 10, 0, 1, 4)

        btn_back = QPushButton('Назад', self)
        btn_back.setFixedSize(150, 30)
        btn_back.clicked.connect(self.back_main_window)
        self.grid.addWidget(btn_back, 10, 4, 1, 4)

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
        self.save_back()
    

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

    def back_main_window(self):
        self.close()
        self.back = Patients_main()
        self.back.show()


    def save_back(self):
        self.close()
        self.back = Patients_main()
        self.back.show()


class AddPat_test(AddPat):
    
    def back_main_window(self):
        self.close()
        self.back = Patients_test()
        self.back.show()


    def save_back(self):
        self.close()
        self.back = Patients_test()
        self.back.show()


class SensTest(Window):

    def open_w(self):

        amplitude = QLabel('Амплитуда тока', self) 
        self.grid.addWidget(amplitude, 2, 0, 1, 1)

        self.slider_amp = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_amp, 3, 0, 1, 2)

        lcd = QLCDNumber(self)
        self.slider_amp.valueChanged.connect(lcd.display)
        self.grid.addWidget(lcd, 2, 3, 2, 1)

        time = QLabel('Время, мс', self) 
        self.grid.addWidget(time, 4, 0, 1, 1)

        self.slider_time = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_time, 5, 0, 1, 2)

        lcd_time = QLCDNumber(self)
        self.slider_time.valueChanged.connect(lcd_time.display)
        self.grid.addWidget(lcd_time, 4, 3, 2, 1)

        btn_test_amp = QPushButton('Тест', self)
        btn_test_amp.clicked.connect(self.test_amp)
        self.grid.addWidget(btn_test_amp, 6, 0)

        self.sens()


    def back_main_window(self):
        self.close()
        self.back = NPU()
        self.back.show()


    def test_amp(self):
        pass


class Sens_main(SensTest):

    def sens(self):

        btn_ok = QPushButton('Назад', self)
        btn_ok.clicked.connect(self.back_main_window)
        self.grid.addWidget(btn_ok, 6, 1)


class Sens_test(SensTest):

    def sens(self):

        btn_save = QPushButton('OK', self)
        btn_save.clicked.connect(self.show_amp)
        self.grid.addWidget(btn_save, 6, 1)


    def show_amp(self):
        show_amp = QMessageBox()
        show_amp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        show_amp.setText(str(self.slider_amp.value()) + ' мА, ' + str(self.slider_time.value()) + ' мс')
        show_amp.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = show_amp.exec()
        if ret == QMessageBox.Yes:
            global sensitive_global
            sensitive_global = str(self.slider_amp.value()) + ' мА, ' + str(self.slider_time.value()) + ' мс'
            self.next_to_scr()


    def next_to_scr(self):
        self.close()
        self.scr = Script_test()
        self.scr.show()


class NPU(Window):

    def open_w(self):

        btn_patients = QPushButton('Пациенты', self)
        btn_patients.clicked.connect(self.patients)
        self.grid.addWidget(btn_patients, 1, 0)

        btn_scripts = QPushButton('Сценарии', self)
        btn_scripts.clicked.connect(self.script)
        self.grid.addWidget(btn_scripts, 1, 1)

        btn_conclusions = QPushButton('Заключения', self)
        # btn_add_and_settings.clicked.connect(self.initiate)
        self.grid.addWidget(btn_conclusions, 1, 2)

        btn_start = QPushButton('Начать тест', self)
        btn_start.clicked.connect(self.start_test)
        self.grid.addWidget(btn_start, 3, 1)

        btn_sensitive_test = QPushButton('Чувствительность', self)
        btn_sensitive_test.clicked.connect(self.sensitive_test)
        self.grid.addWidget(btn_sensitive_test, 4, 1)


    def start_test(self):
        self.close()
        self.start = StartTest()
        self.start.show()


    def sensitive_test(self):
        self.close()
        self.sens_test = Sens_main()
        self.sens_test.show()


    def patients(self):
        self.close()
        self.patients = Patients_main()
        self.patients.show()

    
    def script(self):
        self.close()
        self.scr = Script_main()
        self.scr.show()

                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NPU()
    sys.exit(app.exec_()) 