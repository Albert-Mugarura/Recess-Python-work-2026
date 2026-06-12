import csv, json, os, logging
from datetime import datetime

logging.basicConfig(filename="student_system.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

class StudentError(Exception):
    pass

def init_files():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["RegNo", "Name", "Age", "Program"])
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump({}, f)

def add_student():
    reg = input("Reg No: ").strip()
    if not reg:
        raise StudentError("Reg No cannot be empty")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    if not age.isdigit():
        raise StudentError("Age must be a number")
    prog = input("Program: ").strip()
    addr = input("Address: ").strip()
    contact = input("Contact: ").strip()

    with open(CSV_FILE, "a", newline="") as f:
        csv.writer(f).writerow([reg, name, age, prog])

    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    data[reg] = {"address": addr, "contact": contact}
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)

    logging.info(f"Added student: {reg}")
    print("Student added!")

def view_students():
    with open(CSV_FILE, "r") as f:
        rows = list(csv.reader(f))
    if len(rows) <= 1:
        print("No students found.")
        return
    for r in rows:
        print(f"{r[0]:<12} {r[1]:<20} {r[2]:<5} {r[3]:<15}")

def search_student():
    reg = input("Enter Reg No: ").strip()
    with open(CSV_FILE, "r") as f:
        for r in csv.reader(f):
            if r and r[0] == reg:
                with open(JSON_FILE, "r") as jf:
                    extra = json.load(jf).get(reg, {})
                print(f"Reg: {r[0]}, Name: {r[1]}, Age: {r[2]}, Program: {r[3]}")
                print(f"Address: {extra.get('address','')}, Contact: {extra.get('contact','')}")
                return
    print("Student not found.")

def update_student():
    reg = input("Enter Reg No to update: ").strip()
    rows = []
    found = False
    with open(CSV_FILE, "r") as f:
        rows = list(csv.reader(f))
    for i, r in enumerate(rows):
        if r and r[0] == reg:
            r[1] = input(f"Name ({r[1]}): ") or r[1]
            r[2] = input(f"Age ({r[2]}): ") or r[2]
            r[3] = input(f"Program ({r[3]}): ") or r[3]
            found = True
            break
    if not found:
        raise StudentError("Student not found")
    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    if reg in data:
        addr = input(f"Address ({data[reg]['address']}): ") or data[reg]['address']
        contact = input(f"Contact ({data[reg]['contact']}): ") or data[reg]['contact']
        data[reg] = {"address": addr, "contact": contact}
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=2)
    logging.info(f"Updated student: {reg}")
    print("Updated!")

def delete_student():
    reg = input("Enter Reg No to delete: ").strip()
    rows = []
    with open(CSV_FILE, "r") as f:
        rows = list(csv.reader(f))
    new_rows = [r for r in rows if r and r[0] != reg]
    if len(new_rows) == len(rows):
        raise StudentError("Student not found")
    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerows(new_rows)
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    data.pop(reg, None)
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)
    logging.info(f"Deleted student: {reg}")
    print("Deleted!")

def main():
    init_files()
    while True:
        print("\n=== STUDENT MANAGEMENT ===")
        print("1. Add  2. View  3. Search  4. Update  5. Delete  6. Exit")
        try:
            ch = input("Choice: ")
            if ch == "1": add_student()
            elif ch == "2": view_students()
            elif ch == "3": search_student()
            elif ch == "4": update_student()
            elif ch == "5": delete_student()
            elif ch == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
        except StudentError as e:
            print(f"Error: {e}")
            logging.error(f"StudentError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            logging.error(f"Exception: {e}")
        finally:
            pass

if __name__ == "__main__":
    main()
