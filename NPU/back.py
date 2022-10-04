from NPU_main import NPU
from patients import Patients_main, Patients_test


class Back():
        
        def back_main_window(cls):
                cls.close()
                NPU().show()
        
        def back_to_patient(cls):
                cls.close()
                Patients_main().show()

        def back_to_patient_test(cls):
                cls.close()
                Patients_test().show()

               