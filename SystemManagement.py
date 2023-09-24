import datetime
import time

class SystemManagement:
    id: str
    name: str
    email: str
    deptartment: str
    first_in: int
    total_in_time: int
    total_out_time: int
    flag: int
    start_out_time: int
    start_in_time: int

    def __init__(self, id = "emp123", name = "test", email = "test", department = "test"):
        self.id = id
        self.name = name
        self.email = email
        self.deptartment = department
        self.flag = 0
        self.first_in = 0

    def display(self):
        print("Name : ", self.name, " Email : ", self.email, " department : ", self.deptartment)        

    def log_time(self):
        if self.first_in == 0:
            # when employee first in office
            self.first_in = time.time()
            self.start_in_time = time.time()
            self.total_in_time = 0
            self.total_out_time = 0
            self.flag = 1
        elif self.flag == 1:
            # when employee scan for out
            calculate_in_time = time.time() - self.start_in_time
            self.total_in_time += int(calculate_in_time)
            self.start_out_time = time.time()
            self.flag = 0
        elif self.flag == 0:
            # when employee scan for in
            calculate_out_time = time.time() - self.start_out_time
            self.total_out_time += int(calculate_out_time)
            self.start_in_time = time.time()
            self.flag = 1

    def total_in_out(self):
        hrs = "Hours Completed" if self.total_in_time > 90 else "Pending Hours"
        brk = "Long Break" if self.total_out_time > 30 else "Short Break"
        display = f"\t{self.id} \t{datetime.datetime.fromtimestamp(self.first_in)} \t\t {self.total_in_time} \t\t\t {self.total_out_time} \t\t {hrs} \t\t {brk}"
        return display