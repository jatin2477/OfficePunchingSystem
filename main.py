import datetime
import time
from SystemManagement import SystemManagement

company_name = "Radixweb"
current_time = datetime.datetime.now()
start_time = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
end_time = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
employees_id = [1, 2, 3]
latest_time = time.time()

#print(datetime.datetime.timestamp(currentTime))
#print(currentTimeFromTime)

emp1 = SystemManagement("emp1", "Jatin", "jatin.wadhwani@radixweb.com", "Python")
emp2 = SystemManagement("emp2", "Kunal", "kunal.singh@radixweb.com", "QA")
emp3 = SystemManagement("emp3", "Deepal", "deepak.shukla@radixweb.com", "Python")
#emp1.display()

print(" ======= Welcome To Radixweb ======= ")
while True:

    print("1. Want to scan ? ")
    print("2. Want to see report ? ")
    print("3. Exit ?")
    choice = int(input("Select one option : "))

    if choice == 1:
        employee_id = int(input("Who Scanned Now ? "))
        if employee_id not in employees_id:
            print("Employee Id Not Found... :(")

        if employee_id == 1:        
            emp1.log_time()
        elif employee_id == 2:
            emp2.log_time()
        elif employee_id == 3:
            emp3.log_time()

    elif choice == 2:
        print("\n# ==================================================================================== #\n")
        print("\n\tEmp Id \t\t First In \t\t\t Total In \t\t Total Out \t\t Hours \t\t Break  \n")
        print(emp1.total_in_out())
        print(emp2.total_in_out())
        print(emp3.total_in_out())
        print("\n\n# ==================================================================================== #\n")

    elif choice == 3:
        break



