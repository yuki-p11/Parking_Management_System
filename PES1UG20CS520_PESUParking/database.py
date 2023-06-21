# pip install mysql-connector-python

import mysql.connector 


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="password",
    database="pesu_parking_vehicle"
)
c = mydb.cursor()

#----------------------------------------------------Security Guard-------------------------------------------------#
def create_table_vehicleEnter():
    c.execute('CREATE TABLE IF NOT EXISTS Vehicle_in(Date DATE, Type TEXT, Owner_type TEXT, Vehicle_no varchar(50), P_id varchar(2),ID varchar(13))')
    mydb.commit()

def add_data_enter(Date, Type,Owner_type, Vehicle_no, Parking_id,id):
    c.execute('INSERT INTO Vehicle_in(Date, Type, Owner_type,Vehicle_no, P_id,ID) VALUES (%s,%s,%s,%s,%s,%s)',
              (Date, Type,Owner_type, Vehicle_no, Parking_id,id))
    c.execute('CALL StatusUpdation("{}")'.format(Parking_id)) 
    mydb.commit()
    

  
    

def add_data_exit(Date,id):
    c.execute('INSERT INTO Vehicle_out(Date,ID) VALUES (%s,%s)',(Date,id))
    mydb.commit()

def count_vehicles():
    c.execute('SELECT COUNT(P_id) from Vehicle_in')
    data=c.fetchall()
    mydb.commit()
    return data
    
#------------------------------------------------------Admin_Create---------------------------------------------------------#
def create_table_Student():
    c.execute('CREATE TABLE IF NOT EXISTS student(Contact varchar(10), ID varchar(13), Name varchar(50), Semester INT)')
    mydb.commit()

def create_table_Teacher():
    c.execute('CREATE TABLE IF NOT EXISTS faculty(Contact varchar(10), ID varchar(13), Name varchar(50))')
    mydb.commit()

def create_table_ParkingLot():
    c.execute('CREATE TABLE IF NOT EXISTS parking_space(Parking_id varchar(2), Status TEXT)')
    mydb.commit()

#-------------------------------------Admin_data---------------------------------------------------------------------------

def add_data_student(contact,ID,Name,Semester):
    c.execute('INSERT INTO student(Contact, ID , Name , Semester) VALUES (%s,%s,%s,%s)',(contact,ID,Name,Semester))
    mydb.commit()

def remove_data_student(ID):
    c.execute('DELETE FROM student WHERE ID="{}"'.format(ID))
    mydb.commit()

def add_data_Teacher(Contact,ID,Name):
    c.execute('INSERT INTO faculty(Contact , ID , Name ) VALUES (%s,%s,%s)',(Contact,ID,Name))
    mydb.commit()

def remove_data_Teacher(ID):
    c.execute('DELETE FROM faculty WHERE ID="{}"'.format(ID))
    mydb.commit()

def add_data_Parkinglot(Parking_id,Status):
    c.execute('INSERT INTO parking_space(Parking_id , Status) VALUES (%s,%s)',(Parking_id,Status))
    mydb.commit()

def remove_data_ParkingLot(Parking_id):
    c.execute('DELETE FROM parking_space WHERE Parking_id="{}"'.format(Parking_id))
    mydb.commit()

def view_ViewVehEnter():
    c.execute('SELECT Date,Type,Owner_type,Vehicle_no,P_id,faculty.ID,faculty.Name,faculty.Contact FROM Vehicle_in,faculty WHERE Owner_type="Teacher" AND Vehicle_in.id=faculty.ID UNION SELECT Date,Type,Owner_type,Vehicle_no,P_id,Vehicle_in.id,student.Name,student.Contact FROM Vehicle_in,student WHERE Owner_type="Student" AND Vehicle_in.id=student.ID')
    data = c.fetchall()
    return data

def show_vehicles():
    c.execute('SELECT * FROM parking_space')
    data=c.fetchall()
    return data

def read_amount():
    c.execute('select vehicle_no,amount_calc(owner_type,type) from vehicle_in;')
    data=c.fetchall()
    return data

def read_record_count():
    c.execute('SELECT count(*) as total_records,Owner_type,Date  FROM Vehicle_in group by date,Owner_type;')
    data=c.fetchall()
    return data    

def faculty_not():
    c.execute('Select * from faculty where faculty.ID NOT IN (Select ID from Vehicle_in);')
    data=c.fetchall()
    return data

def Student_not():
    c.execute('Select * from student where student.ID NOT IN(Select ID from Vehicle_in);')
    data=c.fetchall()
    return data