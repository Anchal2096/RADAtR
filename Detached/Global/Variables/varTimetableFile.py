# -------- values decided by governing authority -----

from GUI.GUI_ExaminationScheduling import *
main_window_obj = MainWindow()
print(main_window_obj.click_box())

totalWorkingDays = 5
total_slot_no = 3
days_list = []
slot_list = []
examination_scheduling_generation_limit = 5

for i in range(totalWorkingDays):
    j = str(i+1)
    day = "Day"+j
    days_list.append(day)
# print(days_list)

for i in range(total_slot_no):
    j = str(i+1)
    slot = "Slot"+j
    slot_list.append(slot)
# print(slot_list)

time_table_generation_limit = 5
