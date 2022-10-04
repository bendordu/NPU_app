# -*- coding: utf-8 -*-
import csv
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QListWidget
from PyQt5 import QtCore
from window import Window
from check import Check


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


    # def back_main_window(self):
    #     self.close()
    #     self.back = NPU()
    #     self.back.show()
    # def back_main_window(self):
    #     Back.back_main_window(self)


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

    
    # def next_to_check(self):
    #     self.close()
    #     Check().show()