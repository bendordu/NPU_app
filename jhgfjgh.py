import random
from PyQt5.QtCore import QTime

# list = []
# tim = []
# for i in range(6):
#     list += [random.random()]
#     a = sum(list)
# for i in list:
#     tim += [round((i/a*120000), 2)]


# time = QTime.currentTime()


time_m = QTime()
time_m.start()

for i in range(20):            
    print(time_m.elapsed())