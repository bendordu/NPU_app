# -*- coding: utf-8 -*-
from PyQt5 import QtCore
# import grove_gsr_sensor
# import grove_emg_detector
# import ear_HR_sensor

class Detect(QtCore.QObject):

    running = False

    def run(self):
        # global emg_data
        # global gsr_data
        # global hr_data

        emg_data = []
        gsr_data = []
        hr_data = []
        
        # while True:            
        #     emg_data += [grove_emg_detector.main()]
        #     gsr_data += [grove_gsr_sensor.main()]
            # hr_data += [[str(ear_HR_sensor.main())]]



