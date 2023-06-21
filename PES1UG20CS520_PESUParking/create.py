import streamlit as st
from database import add_data_enter,add_data_exit,add_data_student,add_data_Teacher,remove_data_ParkingLot,remove_data_student,remove_data_Teacher,add_data_Parkinglot

####################################################Security Guard ###################################################
def create_enter():
    #col1 = st.columns(2)
    #with col1:
    Enter_date = st.date_input("Date:")
    Veh_type= st.selectbox("Type:",["Two wheeler","Four wheeler"])
    Owner_type = st.selectbox("Owner Type:",["Teacher","Student"])
    Veh_No = st.text_input("Vehicle_no:")
    Parking_id = st.text_input("Parking_id:")
    id = st.text_input("ID:")
    #with col2:
    #    dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
    #    dealer_pin = st.text_input("Pin Code:")
    #dealer_street = st.text_input("Street Name:")
    if st.button("Add Vehicle"):
        add_data_enter(Enter_date, Veh_type, Owner_type, Veh_No, Parking_id,id)
        st.success(" Successfully added Vehicle record: {}".format(Veh_No))
    
def create_exit():
    #col1=st.columns(1)
    #with col1:
    Exit_date = st.date_input("Date:")
    id = st.text_input("ID:")
    # if st.button("Search Vehicle"):
        #add_data_exit(Exit_date,id)
        #st.success(" Successfully added Vehicle record: {}".format(Veh_No))

#--------------------------------------------------------------Admin------------------------------------------------------------#

def create_AddStudent():
    #col1= st.columns(1)
    #with col1:
    Contact = st.text_input("Contact:")
    ID = st.text_input("ID:")
    Name = st.text_input("Name")
    Semester = st.text_input("Semester")
    if st.button("Add Student"):
        add_data_student(Contact,ID, Name, Semester)
        st.success(" Successfully added Student record: {}".format(ID))

def create_RemoveStudent():
    #col1= st.columns(1)
    #with col1:
    ID= st.text_input("ID:")
    if st.button("Remove Student"):
        remove_data_student(ID)
        st.success(" Successfully Removed Student record: {}".format(ID))

def create_AddTeacher():
    #col1= st.columns(1)
    #with col1:
    Contact = st.text_input("Contact:")
    ID= st.text_input("ID:")
    Name = st.text_input("Name")
        
    if st.button("Add Teacher"):
        add_data_Teacher(Contact, ID, Name)
        st.success(" Successfully added Teacher record: {}".format(ID))

def create_RemoveTeacher():
    #col1= st.columns(1)
    #with col1:
        
    ID= st.text_input("ID:")
        
    if st.button("Remove Teacher"):
        remove_data_Teacher(ID)
        st.success(" Successfully removed Teacher record: {}".format(ID))


    

def create_AddParkingLot():
    #col1= st.columns(1)
    #with col1:
    Parking_id = st.text_input("Parking ID:")
    Status= st.selectbox( "Status",("Active","Occupied"))
        
    if st.button("Add Parking Lot"):
        add_data_Parkinglot(Parking_id, Status)
        st.success(" Successfully added Parking Lot: {}".format(Parking_id))

def create_RemoveParkingLot():
    #col1= st.columns(1)
    #with col1:
    Parking_id = st.text_input("Parking ID:")
        
    if st.button("Remove Parking Lot"):
        remove_data_ParkingLot(Parking_id)
        st.success(" Successfully removed Parking Lot: {}".format(Parking_id))


