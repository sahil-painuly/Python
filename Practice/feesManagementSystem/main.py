import mysql.connector
from datetime import datetime

class FeeRecordManagementSystem:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS FeeRecordsclass9 (
                            StudentName VARCHAR(255) PRIMARY KEY,
                            AdmissionDate DATE NOT NULL,
                            April DECIMAL(10, 2),
                            May DECIMAL(10, 2),
                            June DECIMAL(10, 2),
                            July DECIMAL(10, 2),
                            August DECIMAL(10, 2),
                            September DECIMAL(10, 2),
                            October DECIMAL(10, 2),
                            November DECIMAL(10, 2),
                            December DECIMAL(10, 2)
                          )''')
        self.conn.commit()

    def add_fee_record(self, name, admission_date, fee_amount, month):
        cursor = self.conn.cursor()
        update_query = f'''INSERT INTO FeeRecordsclass9 (StudentName, AdmissionDate, {month}) VALUES (%s, %s, %s) 
                            ON DUPLICATE KEY UPDATE {month}=%s'''
        cursor.execute(update_query, (name, admission_date, fee_amount, fee_amount))
        self.conn.commit()
        print(f"Fee record for student {name} added/updated successfully for {month}.")

    def update_fee_record(self, name, month, new_fee_amount):
        cursor = self.conn.cursor()
        update_query = f'''UPDATE FeeRecordsclass9 SET {month}=%s WHERE StudentName=%s'''
        cursor.execute(update_query, (new_fee_amount, name))
        self.conn.commit()
        print(f"Fee record for student {name} updated successfully for {month}.")

    def display_fee_records(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM FeeRecordsclass9''')
        fee_records = cursor.fetchall()
        print("StudentName\tAdmissionDate\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember")
        for record in fee_records:
            print("\t".join(str(item) for item in record))

    def close_connection(self):
        self.conn.close()

def main():
    host = "localhost"
    user = "root" #enter your username
    password = "999***"  #enter your password 
    database = "codewithsahil"
    frms = FeeRecordManagementSystem(host, user, password, database)

    while True:
        print("\nFee Record Management System")
        print("1. Add Fee Record")
        print("2. Update Fee Record")
        print("3. Display Fee Records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            admission_date = input("Enter admission date (YYYY-MM-DD): ")
            fee_amount = float(input("Enter fee amount: "))
            month = input("Enter month (January, February, etc.): ").capitalize()
            frms.add_fee_record(name, admission_date, fee_amount, month)
        elif choice == "2":
            name = input("Enter student name: ")
            month = input("Enter month to update (January, February, etc.): ").capitalize()
            new_fee_amount = float(input("Enter new fee amount: "))
            frms.update_fee_record(name, month, new_fee_amount)
        elif choice == "3":
            frms.display_fee_records()
        elif choice == "4":
            print("Exiting program.")
            frms.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
