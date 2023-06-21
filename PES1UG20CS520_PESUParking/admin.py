import streamlit as st
from read import readvehicles,read_parkinglots,read_records_count,read_notF,read_notS
from create import create_AddParkingLot,create_AddStudent,create_AddTeacher,create_RemoveParkingLot,create_RemoveStudent,create_RemoveTeacher
from database import create_table_ParkingLot,create_table_Student,create_table_Teacher,view_ViewVehEnter
# def main():
#     st.title("PESU PARKING")
#     #navigate = ["Admin Login","Security Guard Login"]
#     #choice = st.sidebar.radio("User Login",navigate)
#     #if choice=="Admin Login":
#     form = st.form(key='my_form')
#     username = form.text_input(label='Enter Admin Username')
#     password = form.text_input('Enter Admin Password',type='password')
#     submit_button = form.form_submit_button(label='Submit')
#     if username=='admin' and password=='admin123':
#         main1()
def main1():
    st.title("PESU PARKING ADMIN")
    menu = ["Add Student", "Remove Student","Add Teacher","Remove Teacher","View Vehicles Entered","Add Parking Lot","Remove Parking Lot","Show Parking Lots","Number of parking lots occupied","Teachers not parked","Students not parked"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table_Student()
    create_table_Teacher()
    create_table_ParkingLot()

    if choice == "Add Student":
        st.subheader("Enter Student Details To Be Added:")
        create_AddStudent()

    
    elif choice=="Remove Student":
        st.subheader("Enter Student Details To Be Removed:")
        create_RemoveStudent()
    
    elif choice=="Add Teacher":
        st.subheader("Enter Teacher Details To Be Added:")
        create_AddTeacher()

    
    elif choice=="Remove Teacher":
        st.subheader("Enter Teacher Details To Be Removed:")
        create_RemoveTeacher()

    
    elif choice=="View Vehicles Entered":
        st.subheader("Vehices_Entered:")
        readvehicles()

    
    elif choice=="Add Parking Lot":
        st.subheader("Enter Parking Lot Details To Be Added:")
        create_AddParkingLot()

    
    elif choice=="Remove Parking Lot":
        st.subheader("Enter Parking Lot Details To Be Removed:")
        create_RemoveParkingLot()

    elif choice=="Show Parking Lots":
        st.subheader("All Parking Lots:")
        read_parkinglots()
        #create_RemoveStudent()

    elif choice=="Number of parking lots occupied":
        st.subheader("Number of parking occupied by teachers and students:")
        read_records_count()

    elif choice=="Teachers not parked":
        st.subheader("Not occupied by teachers:")
        read_notF()

    elif choice=="Students not parked":
        st.subheader("Not occupied by students:")
        read_notS()

    # else:
    #     create_table_vehicleEnter()
    #     st.subheader("Enter Details:")
# if __name__ == '__main__':
#     main()