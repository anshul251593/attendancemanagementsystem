import json

class AttendanceSystem:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, student_name):
        if student_name in self.attendance:
            self.attendance[student_name] += 1
        else:
            self.attendance[student_name] = 1
        print(f"Attendance marked for {student_name}.")

    def view_attendance(self):
        if not self.attendance:
            print("No attendance records found.")
        else:
            for student, days in self.attendance.items():
                print(f"{student}: {days} days")

    def save_data(self, filename="attendance_data.json"):
        with open(filename, 'w') as file:
            json.dump(self.attendance, file)
        print(f"Attendance data saved to {filename}.")

    def load_data(self, filename="attendance_data.json"):
        try:
            with open(filename, 'r') as file:
                self.attendance = json.load(file)
            print(f"Attendance data loaded from {filename}.")
        except FileNotFoundError:
            print(f"No data file found with the name {filename}.")

def main():
    system = AttendanceSystem()
    while True:
        print("\n1. Mark Attendance")
        print("\n2. View Attendance")
        print("\n3. Save Data")
        print("\n4. Load Data")
        print("\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student name: ")
            system.mark_attendance(student_name)
        elif choice == '2':
            system.view_attendance()
        elif choice == '3':
            system.save_data()
        elif choice == '4':
            system.load_data()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
